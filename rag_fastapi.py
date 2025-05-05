 # rag_fastapi.py
"""FastAPI backend для автономного RAG‑сервиса по документам ФСТЭК."""

import os
import logging
import warnings
import importlib.util
from typing import List

import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    pipeline,
    BitsAndBytesConfig,
)
from transformers.utils.import_utils import is_flash_attn_2_available

from langchain_community.document_loaders import (
    PyPDFDirectoryLoader,
    DirectoryLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredMarkdownLoader,
    UnstructuredFileLoader,
)
from langchain_text_splitters import TokenTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
)

# ──────────────────────────────────────────────────────────────────────────────
# НАСТРАИВАЕМЫЕ КОНСТАНТЫ
# ──────────────────────────────────────────────────────────────────────────────
PDF_DIRECTORY = "fstec_docs"
VECTORSTORE_PATH = "fstec_faiss.idx"

EMBEDDING_MODEL_NAME = "intfloat/multilingual-e5-large"
# LLM_MODEL_NAME = "Vikhrmodels/Vikhr-Llama3.1-8B-Instruct-R-21-09-24"
LLM_MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.3"

MAX_NEW_TOKENS = 1024
TEMPERATURE = 0.3
TOP_P = 0.9

CHUNK_TOKENS = 384
CHUNK_OVERLAP = 64
RETRIEVAL_K = 20
SCORE_THRESHOLD = 0.25

# ──────────────────────────────────────────────────────────────────────────────
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ──────────────────────────────────────────────────────────────────────────────

def optimal_device() -> str:
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"

DEVICE = optimal_device()


def _is_module_available(module: str) -> bool:
    return importlib.util.find_spec(module) is not None


def load_documents(directory: str) -> List[Document]:
    """Загрузка документов различных форматов из каталога."""
    loaders = {".pdf": PyPDFDirectoryLoader(directory, glob="**/*.pdf", recursive=True)}

    if _is_module_available("docx"):
        loaders[".docx"] = DirectoryLoader(
            directory,
            glob="**/*.docx",
            loader_cls=UnstructuredWordDocumentLoader,
            recursive=True,
        )
    else:
        logging.warning("python-docx не установлен — пропускаем .docx")

    if _is_module_available("markdown"):
        loaders[".md"] = DirectoryLoader(
            directory,
            glob="**/*.md",
            loader_cls=UnstructuredMarkdownLoader,
            recursive=True,
        )
    else:
        logging.warning("markdown не установлен — .md будет трактоваться как текст")
        loaders[".md"] = DirectoryLoader(
            directory,
            glob="**/*.md",
            loader_cls=UnstructuredFileLoader,
            recursive=True,
        )

    loaders[".txt"] = DirectoryLoader(
        directory, glob="**/*.txt", loader_cls=UnstructuredFileLoader, recursive=True
    )

    docs: List[Document] = []
    for ext, loader in loaders.items():
        try:
            part = loader.load()
            docs.extend(part)
            logging.info("Загружено %s документов с расширением %s", len(part), ext)
        except Exception as exc:
            logging.warning("Не удалось загрузить %s: %s", ext, exc)

    if not docs:
        raise FileNotFoundError(f"В каталоге {directory} не найдено подходящих документов")
    return docs


def split_documents(documents: List[Document]) -> List[Document]:
    """Разбивка документов на перекрывающиеся чанки."""
    splitter = TokenTextSplitter(
        chunk_size=CHUNK_TOKENS,
        chunk_overlap=CHUNK_OVERLAP,
        encoding_name="cl100k_base",
        add_start_index=True,
    )
    return splitter.split_documents(documents)


def build_embeddings() -> HuggingFaceEmbeddings:
    """Создание модели эмбеддингов."""
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={"device": DEVICE},
        encode_kwargs={"normalize_embeddings": True},
    )


def create_vectorstore(chunks: List[Document], embeddings: HuggingFaceEmbeddings):
    """Создание и сохранение FAISS‑индекса."""
    vs = FAISS.from_documents(chunks, embeddings)
    vs.save_local(VECTORSTORE_PATH)
    return vs


def load_vectorstore(embeddings: HuggingFaceEmbeddings):
    """Загрузка ранее сохранённого индекса."""
    if not os.path.isdir(VECTORSTORE_PATH):
        raise FileNotFoundError("Индекс не найден — необходимо провести ingest")
    return FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        normalize_L2=True,
        allow_dangerous_deserialization=True,
    )


def _load_llama_model(model_name: str,
                      quant_cfg: BitsAndBytesConfig,
                      model_dtype: torch.dtype):
    """
    Сначала пытаемся загрузить всю модель в GPU (без offload).
    При нехватке памяти — та же 4‑битная версия, но целиком на CPU.
    Это устраняет двойную квантовацию uint8 → 4‑bit.
    """
    if torch.cuda.is_available():
        try:
            logging.info("Загружаю модель целиком в GPU…")
            return AutoModelForCausalLM.from_pretrained(
                model_name,
                quantization_config=quant_cfg,
                torch_dtype=model_dtype,
                device_map={"": 0},                 # всё на cuda:0
                attn_implementation=(
                    "flash_attention_2"
                    if is_flash_attn_2_available()
                    else "sdpa"
                ),
                low_cpu_mem_usage=True,
            )
        except RuntimeError as exc:
            logging.warning(
                "GPU‑памяти не хватило (%s). Переключаюсь на CPU‑4bit…", exc
            )

    # Fallback: полностью на CPU
    return AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=quant_cfg,            # 4‑bit, но без offload
        torch_dtype=torch.float32,
        device_map={"": "cpu"},
        low_cpu_mem_usage=True,
    )



def init_llm(model_name: str) -> HuggingFacePipeline:
    quant_cfg = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=(
            torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        ),
        bnb_4bit_use_double_quant=True,
        llm_int8_enable_fp32_cpu_offload=True,
    )
    model_dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = _load_llama_model(model_name, quant_cfg, model_dtype)

    text_gen = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=MAX_NEW_TOKENS,
        temperature=TEMPERATURE,
        top_p=TOP_P,
        do_sample=True,
        return_full_text=False,
    )
    return HuggingFacePipeline(pipeline=text_gen)


# ──────────────────────────────────────────────────────────────────────────────
# PROMPT & RAG CHAIN
# ──────────────────────────────────────────────────────────────────────────────
SYSTEM_MSG = (
    "Ты — эксперт по документам ФСТЭК и настройке межсетевых экранов. "
    "Отвечай строго на русском, используя только предоставленный контекст."
)
PROMPT_TMPL = ChatPromptTemplate.from_messages(
    [("system", SYSTEM_MSG), ("user", "Контекст: {context}\n\nВопрос: {question}")]
)


def create_rag(llm: HuggingFacePipeline, vs: FAISS):
    retriever = vs.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": RETRIEVAL_K, "score_threshold": SCORE_THRESHOLD},
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": PROMPT_TMPL},
    )


# ──────────────────────────────────────────────────────────────────────────────
# FASTAPI
# ──────────────────────────────────────────────────────────────────────────────

app = FastAPI(title="FSTEC RAG API", version="0.1.0", root_path="")

class Query(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str


@app.on_event("startup")
async def startup_event() -> None:
    """Однократная инициализация модели, индекса и цепочки RAG."""
    global rag
    logging.info("Запуск инициализации RAG‑сервиса…")

    embeddings = build_embeddings()

    if not os.path.isdir(VECTORSTORE_PATH):
        logging.info("Индекс не найден — выполняем ingest документов…")
        docs = load_documents(PDF_DIRECTORY)
        chunks = split_documents(docs)
        vs = create_vectorstore(chunks, embeddings)
    else:
        vs = load_vectorstore(embeddings)

    llm = init_llm(LLM_MODEL_NAME)
    rag = create_rag(llm, vs)

    logging.info("RAG‑сервис готов к работе")


@app.post("/ask", response_model=Answer)
async def ask(query: Query):
    """Единая точка обращения к модели."""
    try:
        result = rag.invoke({"query": query.question})
        return {"answer": result["result"].strip()}
    except Exception as exc:
        logging.exception("Ошибка при обработке запроса")
        raise HTTPException(status_code=500, detail=str(exc))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("rag_fastapi:app", host="0.0.0.0", port=8000, reload=False)
