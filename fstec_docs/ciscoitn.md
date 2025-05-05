# Introduction to Networks Bible 📖 

## Chapter 1: Explore the Network
- **Ways of communication using networks**
    - Texting
    - Social Media
    - Collaboration Tools
    - Blogs
    - Wikis
    - Podcasting
    - Peer-to-Peer (P2P) File Sharing
- **Network types by size**
    - Small Home Network
    - Small Office/Home Office Networks
    - Medium to Large Networks
    - World Wide Networks
### Servers
Servers are computers with software that enable them to provide information, like email or web pages, to 
other end devices on the network. Each service requires separate server software.

### Clients
Clients are computers with software installed that enable them to request and display the information
obtained from the server.

### Peer-to-Peer
Peer-to-Peer is the capacity of a computer to carry out both roles at the same time. In small businesses
and homes, many computers function as the servers and clients on the network.
##### Advantages
- Easy to set up
- Less complexity
- Lower cost since network devices and dedicated servers may not be required
- Can be used for simple tasks such as transferig files and sharing printers
#### Disadvantages
- No centralized administration
- Not as secure
- Not scalable
- All devices may act as both clients and servers which can slow their performance

### Network Components
- Physical
    - Devices
        - End Devices
            - Laptop
            - PC
            - Mobile Phone
        - Intermediary Network Devices
            - LAN Switch
            - Multilayer Switch
            - Router
            - Wireless Router
            - Firewall Appliance
    - Network Media
        - Metallic wires within cables
        - Glass or plastic fibers (fiber optic cable)
        - Wireless transmission
- Non-Physical
    - Services
        - Applications

### Connection Terms
##### Network Interface Card
A NIC, or LAN adapter, provides the physical connection to the network at the PC or other end device.
The media that are connecting the PC to the networking device, plug directly into the NIC.
##### Physical Port
A connector or outlet on a networking device where the media is connected to an end device or another networking
device
##### Interface
Specialized ports on a networking device that connect to individual networks. Because routers are used to
interconnect networks, the ports on a router are referred to as network interfaces.

### Topology Diagrams
- Physical topology diagrams (Show physical devices and connections)
- Logical topology diagrams (Show configuration parameters i.e. IP Address)

### Types of Networks
##### Local Area Network (LAN)
- LANs interconnect end devices in a limited area such as home, school, office building, or campus
- A LAN is usually administered by a single organization or individual. The administrative control that governs
the security and access control policies are enforced on the network level
- LANs provide high speed bandwidth to internal end devices and intermediary devices
##### Wide Area Network (WAN)
- WANs interconnect LANs over wide geographical areas such as between cities, states, provinces, countries, or continents
- WANs are usually administered by multiple service providers
- WANs typically provide slower speed links between LANs
##### Metropolitan Area Network (MAN)
A network infrastructure that spans a physical area larger than a LAN but smaller than a WAN. MANs are typically
operated by a single entity such as a large organization.
##### Wireless LAN (WLAN)
Similar to a LAN but wirelessly interconnects users and end points in a small geographical area.
##### Storage Area Network (SAN)
A network infrastructure designed to support file servers and provide data storage, retrieval, and replication.

### The Internet
- The Internet is a worldwide collection of interconnected networks
- The Internet is not owned by any individual or group.
- Uses a group of standards and recognized technologies
- There are organizations that have bene devloped for the purpose of helping to maintain structure and
standardization of Internet protocols and processes, like:
    - Internet Engineering Task Force (IETF)
    - Internet Corporation for Assigned names and Numbers (ICANN)
    - Internet Architecture Board (IAB)

### Intranets and Extranets
##### Intranet
Intranet is a private connection of LANs and WANs that belongs to an organization, and is designed to be 
accesible only by the organization's members, employees, or other with autorization.
##### Extranet
Provide secure and safe access to individuals who work for a different organization, but require access
to the organization's data.

### Home and Small Office Internet Connections
##### Cable
Typically offered by cable television service providers, the Internet data signal is carried on the same
cable that delivers cable television. It provides a high bandwidth, always on, connection to the Internet.
##### DSL
Digital Subscriber lines provide a high bandwidth, always on, connection to the Internet. DSL runs over
a telephone line. In general, small office and home office users connect using Asymmetrical DSL (ADSL),
which means that the download speed is fater than the upload speed
##### Cellular
Cellular Internet access uses a cell phone network to connect. Wherever you can get a celullar signal.
##### Satellite
The availability of satellite Internet access is a real benefit in those areas that would otherwise have no 
Internet connectivity at all. Satellite dishes require a clear line of sight to the satellite.
##### Dial-up Telephone
An inexpensive option that uses any phone line and a modem. The low bandwidth provided by a dial-up modem
connection is usually not sufficient for large data transfer, although it is useful for mobile access while
traveling.
### Businesses Internet Connections
##### Dedicated Leased Line
Leased lines are actually reserved circuits within the service provider's network that connect geographically
separated offices for private voice and/or data networking. The circuits are typically rented at a monthly
or yearly rate. They can be expensive.

## Chapter 2: Configure a Network Operating System
### Operating Systems
- **Parts**
    - **Hardware:** The physical part of a computer including underlying electronics.
    - **Kernel:** Is the portion of the OS that interacts directly with computer hardware
    - **Shell:** Is the portion that interfaces with applications and the user

User can interact with the shell using a command-line interface (CLI) or a graphical user interface (GUI)

- **CLI:** Usually is a text-based environment where user enter commands on the keyboard at a command prompt.
It requires that the user have knowledge of the underlying structure that control the system.
- **GUI:** Allows the user to interact with the system using an environment of graphical icons, menus and windows.
However, this may not always be able to provide all of the features available at the CLI. GUIs can also fail,
crash, or simply not operate as specified.

The network operating system used on Cisco devices is called the Cisco Internetwork Operating System (IOS).
Cisco IOS is used for most Cisco devices regardless of the type or size of the device.

**NOTE:** The OS on home routers is usually called firmware. The most common method for configuring a home
router is by using a web browser-based GUI.

#### Purpose of OS

- **GUI enables to**
    - Use a mouse to make selections and run programs
    - Enter text and text-based commands
    - View output on a monitor
- **CLI enables to**
    - Use a keyboard to run CLI-based network programs
    - Use a keyboard to enter text and text-based commands
    - View output on a monitor

The IOS version is dependent on the type of device being used and the required features. While all devices come
with a default IOS and feature set, it is possible to upgrade the IOS version or feature set to obtain
additional capabilities

#### Access Methods
- **Console:** This is a physical management port that provides out-of-band access to a Cisco device. Out-of-band
access  refers to access via a dedicated management channel that is used for device maintenance purposes only.
- **SSH:** Secure Shell is a method for remotely establishing a secure CLI connection through a virtual interface,
over a network. Unlike a console connection, SSH connections require active networking services on the device
including an active interface configured with an address.
- **Telnet:** Telnet is an insecure method of remotely establishing a CLI session through a virtual interface,
over a network. Unlike SSH, Telnet does not provide a securely encrypted connection. User authentication,
passwords, and commands are sent over the network in plaintext.

**NOTE:** Some devices, such as routers, may also support a legacy auxiliary port that was used to establish
a CLI session remotely using a modem. Similar to a console connection, the AUX port is out-of-band and does
not require networking services to be configured or available.

#### Terminal Emulation Programs
- PuTTY
- Tera Term
- SecureCRT
- OS X Terminal

### IOS
#### Primary Command Modes

- **User EXEC Mode:** This mode has limited capabilities but is useful for basic operations. 
Identified by '\>' CLI prompt.
- **Privileged EXEC Mode:** This mode has high level configuration modes, like global configuration mode, which
can only be reached from privileged EXEC mode.
Identified by '#' CLI prompt.

#### Configuration Command Modes
- **Privileged EXEC Mode E/L:** `enable / disable`
- **Global Configuration Mode E/L:** `configure terminal / exit`
- **Subconfiguration Mode:** *(*`end` *jumps to Privileged EXEC Mode)*
    - **Interface:** `interface [interfaceType] [number] / exit`
    - **Line:** `line [lineType] [number] / exit`

#### Basic IOS Command Structure
```
[Prompt] [Command]  [Keyword or Argument]
Switch>    show        ip      protocols
Switch#    ping         192.168.10.5

```
- **Argument types:**
    - **Keyword:** A specific parameter defined in the operating system
    - **Argument:** Not predefined; a value or variable defined by the user

#### IOS Command Syntax
A command might require one or more arguments. To determine the keywords and arguments required for a command,
refer to the command syntax. The syntax provides the pattern or format that must be used when entering a command.

Convention | Description
--- | --- 
**boldface** | Boldface text indicates commands and keywords that you enter literally as shown
*italics* | Italic text indicates arguments for which you supply values
[x] | Square brackets indicate an optional element (keyword or agument)
{x} | Braces indicate a required element (keyword or argument)
[x {y \| z}] | Braces and vertical lines within square brackets indicate a required choice within an optional element

#### IOS Help Features
- **Context-Sensitive Help:** Enables you to quickly find which commands are available
in each command mode. To access context-sensitive help, simply enter a question mark '**?**'
- **Command Syntax Check:** Verifies that a valid command was entered by the user. it will provide feedback 
describing what is wrong with the command

#### Hotkeys and Shorcuts
The IOS CLI provides hot keys and shortcuts that make configuring, monitoring, and troubleshooting easier.

Key | Function
--- | ---
Tab | Completes a partial command name entry
Backspace | Erases the character to the left of the cursor
Ctrl + D | Erases the character at the cursor
Ctrl + K | Erases all characters from the cursor to the end of the command line
Esc + D | Erases all characters from the cursor to the end of the word
Ctrl + U / Ctrl + X | Erases al characters from the cursor back to the beginning of the command line
Ctrl + W | Erases the word to the left of the cursor
Ctrl + A | Moves the cursor to the beginning of the line
Left Arrow / Ctrl + B | Moves the cursor one character to the left
Esc + B | Moves the cursor back one word to the left
Esc + F | Moves the cursor forward one word to the right
Right Arrow / Ctrl + F | Moves the cursor one character to the right
Ctrl + E | Moves the cursor to the end of command line
Up Arrow / Ctrl + P | Recalls command in the history buffer beginning with the most recent commands
Ctrl + R / Ctrl + I / Ctrl + L | Redisplays the system prompt and command line after a console message is received
Ctrl + C | When in any configuration mode, ends the configuration mode and returns to privileged EXEC mode. When in setup mode, aborts back to the command prompt
Ctrl + Z | When in any configuration mode, ends the configuration mode and returns to privileged EXEC mode
Ctr + Shift + 6 | All-purpose break sequence. Use to abort DNS lookups, traceroutes, pings

Commands and keywords can be shortened to the minimum number of characters that identify a unique selection.
**Example:** `configure` command can be shortened to `conf`

### Device Names
When configuring a networking device, one of the first steps is configuring a unique device name or hostname.
Hostnames that appear in CLI prompts can be used in various authentication processes between devices, and
should be used on topology diagrams.

They should:
 - Start with a letter
 - Contain no spaces
 - End with a letter or digit
 - Use only letters, digits, and dashes
 - Be less than 64 characters in length

**Steps to configure a hostname (Privileged EXEC mode required)**
1. `configure terminal`
2. `hostname typeHostNameHere`

**NOTE:** To remove the configured hostname and return the switch to the default prompt, use the `no hostname`
global config command.

### Secure Device Access
Cisco IOS can be configured to use hierarichical mode passwords to allow different access privileges to a 
network device.

- **Securing Administrative Access**
    - Secure privileged EXEC access with a password
    - Secure user EXEC access with a password
    - Secure remote Telnet access with a password
- **Other tasks**
    - Encrypt all passwords
    - Provide legal notification

### Configure Passwords
Enter to the Privileged EXEC mode using `enable`, and then to the Global configuration using `configure terminal`
- **Configure the Privileged EXEC mode password**
    - Put `enable secret hereIsYourPassword`
- **Configure the User EXEC password**
    - Enter to console line using `line console 0`
    - Enter your password using `password hereIsYourPassword`
    - Enter `login`
- **Configure VTY password**
    - Enter to VTY line using `line vty 0 15` *(Many Cisco switches support up to 16 VTY lines that are numbered 0 to 15)*
    - Enter your password using `password hereIsYourPassword`
    - Enter `login`

### Encrypt Passwords
Use the `service password-encryption` global config command. The command applies weak encryption to all 
unencrypted passwords. This encryption applies only to passwords in the configuration file, not to passwords
as they are sent over the network.

To see the encrypted password, use `show running-config`

### Banner Messages
- **Set Message Of The Day**
    - In Global configuration mode, enter `banner motd "theMessageOfTheDay"`

### Save the Running Configuration File
There are two system files that store the device configuration:
- **startup-config**: Stored in NVRAM. Contains all the commands that will be used by the device upon startup or reboot.
NVRAM doesn't lose its contents when the device is powered off
- **running-config**: Stored in RAM. Reflects the current configuration. Modifying a running configuration affects
the operation of a Cisco device immediately. It loses all of its content when the device is powered off or restarted

To view one of the configuration files, use `show nameOfTheConfigurationFile`. To save all the running configuration
files, use `copy running-config startup-config`

### Alter the Running Configuration
- **Restore the device to its previous configuration**
    - Use `reload` with privileged EXEC mode

The downside to using the reload command to remove an unsaved running configuration is the brief amount of time
the device will be offline, causing network downtime.

- **Fabric device startup-configuration**
    - Use `erase startup-config` with privileged EXEC mode

After removing the startup configuration from NVRAM, reload the device to remove the current running configuration
file from RAM. On reload, a switch will load the default startup configuration that originally shipped with the device

### IP Addresses
- Enable devices to locate one another and establish end-to-end communication on the Internet
- The structure of an IPv4 address is called dotted decimal notation and is represented by four decimal numbers
between 0 and 255.
- An IPv4 subnet mask is a 32-bit value that separates the network portion of the address from the host portion.
Determines which particular subnet the device is a member
- The default gateway address is the IP address of the router that the host will use to access remote networks,
including the Internet.
- IP addresses can be assigned to both physical ports and virtual interfaces on devices. A virtual interface means
that there is no physical hardware on the device associated with it

### Interfaces and Ports
Network commnications depend on end user device interfaces, networking device interfaces, and the cables that
connect them. Each physical interface has specifications, or standards, that define it. A cable connecting to the
interface must be designed to match the physical standards of the interface. Types of network media include
twisted-pair copper cables, fiber-optic cables, coaxial cables, or wireless.

Different types of network media have different features and benefits. Not all network media has the same 
characteristics and is appropiate for the same purpose. Some of the differences between various types
of media include:

- Distance the media can successfully carry a signal
- Environment in which the media is to be installed
- Amount of data and the speed at which it must be transmitted
- Cost of the media and installation

Cisco IOS Layer 2 switches have physical ports for devices to connect. These ports don't suport Layer 3 IP addresses.
Therefore, switches have one or more switch virtual interfaces (SVIs). These are virtual interfaces because there is no phyisical
hardware on the device associated with it. An SVI is created in software.

The virtual interface provides a means to remotely manage a switch over a network using IPv4. Each switch comes
with one SVI appearing in the default configuration "out-of-the-box". The default SVI is interface VLAN1.

**NOTE:** A Layer 2 switch does not need an IP address. The IP address assigned to the SVI is used to remotely
access the switch. An IP address is not necessary for the switch to perform its operations.

### Manual IP Address Configuration for End Devices
In order for an end device to communicate over the network, it must be configured with a unique IPv4 address
and subnet mask. IP address information can be entered into end devices manually, or automatically using
Dynamic Host Configuration Protocol (DHCP).

- **Windows**
    - **Control Panel > Network Sharing Center > Change adapter settings**
    - Choose adapter settings and click **Properties** to display the **Local Area Connection Properties**
    - Highlight Internet Protocol Version 4 (TCP/IPv4) and click **Properties** to open **Internet Protocol Version 4 (TCP/IPv4) Properties**

**NOTE:** The DNS server addresses are the IPv4 addresses of the Domain Name System (DNS) servers, which are
used to translate IP addresses to domain names.

### Automatic IP Address Configuration for End Devices
- PCs typically default to using DHCP for automatic IPv4 address configuration
- DHCP is a technology that is used in almost every network
- DHCP enables automatic IPv4 address configuration for every end device that has DHCP enabled
- To display IP configuration settings on a Windows PC use `ipconfig` on CMD

### Switch Virtual Interface Configuration
To configure an SVI on a switch:
- Use the `interface vlan 1` global configuration command *(VLAN 1 is not a physical interface, but is a virtual one)*
- Assign an PIv4 address using the `ip address hereIsTheIpAddress hereIsTheSubnetMask`
- Enable the virtual interface using `no shutdown`

### Interface Addressing Verification
To verify the interfaces and address settings of intermediary devices like switches and routers: 
- Use `show ip interface brief`

### End-to-End Connectivity Test
The command to test connectivity to another device on the network or a website on the Internet is `ping`

## Chapter 3: Network Protocols and Communications
### Communication Fundamentals
Devices must know "how" to communicate. By this, communication has these elements:
- Message source or Sender
- Channel
- Destination or Receiver

Communication begins with a message, or information, that must be sent from a source to a destination. The sending
of this message, whether by face-to-face communication or over a network, is governed by rules called protocols.

### Rule Establishment
Before communicating with one another, individuals must use established rules or agreements to govern the conversation.
Protocols must account for the following requirements:
- An identified sender and receiver
- Common language and grammar
- Speed and timing of delivery
- Confirmation or acknowledgment requirements

The protocols that are used in network communications share many of these fundamental traits. in addition
to identifying the source and destination, computer and network protocols define the details of how a message
is transmitted across a network.

### Message Encoding
One of the first steps to sending a message is encoding. Encoding is the process of converting information into
another acceptable form, for transmission. Decoding reverses this process in order to interpret the information.
Encoding between hosts must be in an appropiate format for the medium. Messages sent across the network are
first converted into bits by the sending host. Each bit is encoded into a pattern of sounds, light waves, or electrical
impulses depending on the network media over which the bits are transmitted. The destination host receives and
decodes the signals in order to interpret the message.

### Message Formatting and Encapsulation
When a message is sent from source to destination, it must use a specific format or structure. Message formats
depend on the type of message and the channel that is used to deliver the message.\
A message that is sent over a computer network follows specific format rules for it to be delivered
and processed. Just as a letter is encapsulated in an envelope for delivery, so too are computer messages.
- Each computer message is encapsulated in a specific format, called a frame, before it is sent over the network.
    - It provides the address of the destination and the address of the source host
    - A frame has a source and destination in both the frame addressing portion and in the encapsulated message
    - The format and contents of a frame are determined by the type of message being sent and the channel
    over which it is communicated.
    - Messages that are not correctly formatted are not successfully delivered to or processed by the destination
    host.

### Message Size
When a long message is sent from one host to another over a network, it is necessary to break the message into
smaller pieces. The rules that govern the size of the pieces, or frames, communicated across the network are very
strict. They can also be different, depending on the channel used. Frames that are too long or too short are not delivered.\
The size restrictions of frames require the source host to break a long message into individual pieces that meet both the minimum and maximum
size requirements. The long message will be sent in separate frames, with each frame containing a piece of the original message.
Each frame will also have its own addressing information. At the receiving host, the individual pieces of the message
are reconstructed into the original message.

### Message Timing
- **Access Method**
    - Determines when someone is able to send a message
    - If two people talk at the same time, a collision of information occurs and it is necesarry for the two to back off
    and start again
    - Hosts on a network need an access method to know when to begin sending messages and how to respond when collisions occur
- **Flow Control**
    - Timing also affects how much information can be sent and the speed that it can be delivered
    - Source and destination hosts use flow control methods to negotiate correct timing for succesful communication
- **Response Timeout**
    - Hosts on the network also have rules that specify how long to wait for responses and what action to take
    if a response timeout occurs

### Message Delivery Options
- **Ways to deliver a message**
    - **Unicast:** There is only a single destination for the message
    - **Multicast:** Delivers the same message to a group of host destinations simultaneously
    - **Broadcast:** All hosts on the network receive the message at the same time

There are times when the sender of a message needs to be sure that the message is delivered succesfully to the 
destination. In these cases, it is necessary for the recipient to return an acknowledgment to the sender. If no 
acknowledgment is required, the delivery option is referred to as unacknowledged.\
Some protocols use a special multicast message that is sent to all devices, making it essentially same as broadcast.\
Additionally, hosts may be required to acknowledge the receipt of some messages while not needing to acknowledge others.

### Rules that Govern Communications
A group of inter-related protocols necessary to perform a communication function is called a protocol suite.
Protocol suites are implemented by hosts and networking devices in software, hardware or both.
- Protocols are viewed in terms of layers, with each higher level service depending on the functionality defined
by the protocols shown in the lower levels.
- The lower layer of the stack are concerned with moving data over the network and providing services to the upper layers,
which are focused on the content of the message being sent.

### Network Protocols
Networking protocols define a common format and set of rules for exchanging messages between devices. Some common
networking protocols are:
- Hypertext Transfer Protocol **(HTTP)**
- Transmission Control Protocol **(TCP)**
- Internet Protocol **(IP)**

### Protocol Interaction
- Application $\rarr$ HTTP
- Transport $\rarr$ TCP
- Internet $\rarr$ IP
- Network Access $\rarr$ Ethernet

#### HTTP
Is an application protocol that governs the way a web server and a web client interact. HTTP defines the content
and formatting of the requests and responses that are exchanged between the client and server. Both the client and
the web server software implement HTTP as part of the application. HTTP relies on other protocols to govern how the messages
are transported between the client and server.

#### TCP
Is the transport protocol that manages the individual conversations. TCP divides the HTTP messages into smaller pieces, 
called segments. These segments are sent between the web server and client processes running at the destination host.
TCP is also responsible for controlling the size and rate at which messages are exchanged between the server and the client.

#### IP
Is responsible for taking the formatted segments from TCP, encapsulating them into packets, assigning them the appropriate
addresses, and delivering them to the destination host.

#### Ethernet
Is a network access protocol that describes two primary functions:
- Communication over a data link and the physical transmission of data on the network media
- Network access protocols are responsible for taking the packets from IP and formatting them to be transmitted over the media

### Protocol Suites and Industry Standards
A protocol suite is a set of protocols that work together to provide comprehensive network communication services.
A protocol suite may be specified by a standards organization or developed by a vendor.

The TCP/IP protocol suite is an open standard, meaning these protocols are freely available to the public,
and any vendor is able to implement these protocols on their hardware or in their software.

A standards-based protocol is a process that has been endorsed by the networking industry and approved by a standards
organization. The use of standards in developing and implementing protocols ensures that products from different
manufactruers can interoperate successfully. If a protocol is not rigidly observed by a particular manufacturer,
their equipment or software may not be able to succesfully communicate with products made by other
manufacturers.

Some protocols are proprietary which means one company or vendor controls the definition of the protocol and how it functions.

**Layer Name** | **TCP/IP** | **ISO** | **AppleTalk** | **Novell Netware**
--- | --- | --- | --- | ---
*Application* | HTTP, DNS, DHCP, FTP | ACSE, ROSE, TRSE, SESE | AFP | NDS
*Transport* | TCP, UDP | TP0, TP1, TP2, TP3, TP4 | ATP, AEP, NBP, RTMP | SPX
*Internet* | IPv4, IPv6, ICMPv4, ICMPv6 | CONP/CMNS, CLNP/CLNS | AARP | IPX
*Network Access* | Ethernet PPP Frame Relay ATM WLAN

### Development of TCP/IP
The first packet switching network and predecessor to today's Internet was the Advanced Research Projects
Agency Network (ARPANET), which came to life in 1969 by connecting mainframe computers at four locations. ARPANET
was funded by the U.S. Department of Defense for use by universities and research laboratories.
- On October 29, 1969, the first message is transmitted from an SDS Sigma 7 mainframe computer at
University of California, Los Angeles (UCLA) to an SDS 940 mainframe computer at Stanford Research Insitute
- ALOHAnet becomes operational, the first packet radio network, developed by Norman Abramson, University of Hawaii
- Ray Tomlinson chooses the @ sign to signify the recipient's destination
- Larry Roberts writes the first email management program
- Telnet specification written (RFC 318)
- The TCP and IP protocols are formalized (RFC 793 and RFC 791)
- The Exterior Gateway Protocol (EGP) is developed to allow routers to exchange network information (RFC 827)
- In 1984, the Domain Name Service (DNS) is introduced
- In 1985, the File Transfer Protocol (FTP) is documented (RFC 765)
- In 1986, Cisco launches its first routing innovation, the AGS multi-protocol router
- In 1988, The Internet Relay Chat (IRC) is developed by Jarkko Oikarinen
- In 1991, Tim Berners-Lee and Robert Cailliau release the specifications for WWW.
- In 1993, the first web browser, MOSAIC, is developed by Marc Andreessen at the University of Illlinois, Champaign-Urbana
- In 1995, the first specifications for IPv6 (the eventual successor to IPv4) released (RFC 1883)
- In 2011, the first World IPv6 Day (June 8, 2011), many websites and Internet service providers around the world,
including Google, Facebook, and Yahoo!, participated with more than 1,000 other companies for a worldwide trial of IPv6

### TCP/IP Protocol Suite
The TCP/IP protocol suite includes many protocols. The individual protocols are organized in layers using
the TCP/IP protocol model: Application, Transport, Internet, and Network Access Layers. TCP/IP protocols are specific
to the Application, Transport and Internet layers. The network access layer protocols are responsible for delivering
the IP packet over the physical medium. These lower layer protocols are developed by various standards organizations.\
The TCP/IP protocol suite is implemented as a TCP/IP stack on both the sending and receiving hosts to provide
end-to-end delivery of applications over a network. The Ethernet protocols are used to transmit the IP packet
over the physical medium used by the LAN

#### Application Layer
##### Name System
###### DNS (Domain Name System/Service)
- Translates domain names such as cisco.com, into IP addresses
##### Host Config
###### BOOTP (Bootstrap Protocol)
- Enables a diskless workstation to discover its own IP address, the IP address of a BOOTP server on the network,
and a file to be loaded into memory to boot the machine
- BOOTP is being superseded by DHCP

###### DHCP (Dynamic Host Configuration Protocol)
- Dynamically assigns IP addresses to client stations at start-up
- Allows the addresses to be re-used when o longer needed

##### Email
###### SMTP (Simple Mail Transfer Protocol)
- Enables clients to send email to a mail server
- Enables servers to send email to other servers

###### POP (Post Office Protocol)
- Enables clients to retrieve email from a mail server
- Downloads email from the mail server to the desktop

###### IMAP (Internet Message Access Protocol)
- Enables clients to access email stored on a mail server
- Maintains email on the server

##### File Transfer
###### FTP (File Transfer Protocol)
- Sets rules that enable a user on one host to access and transfer files to and from another
host over a network
- A reliable, connection-oriented, and acknowledged file delivery protocol

###### TFTP (Trivial File Transfer Protocol)
- A simple, connectionless file transfer protocol
- A best-effort, unacknowledged file delivery protocol
- Utilizes less overhead than FTP

##### Web
###### HTTP (Hypertext Transfer Protocol)
- Set of rules for exchanging text, graphic images, sound, video, and other multimedia files on the World Wide Web

#### Transport Layer
##### UDP (User Datagram Protocol)
- Enables a process running on one host to send packets to a process running on another host
- Does not confirm successful datagram transmission

##### TCP (Transmission Control Protocol)
- Enables reliable communication between processes running on separate hosts
- Reliable, acknowledged transmissions that confirm successful delivery

#### Internet Layer
##### IP (Internet Protocol)
- Receives message segments from the transport layer
- Packages messages into packets
- Addresses packets for end-to-end delivery over an internetwork

##### NAT (Network Address Translation)
- Translates IP addresses from a private network into globally unique public IP addresses

##### IP Support
###### ICMP
- Provides ffeedback from a destination host to a source host about errors in packet delivery

##### Routing Protocols
###### OSPF (Open Shortest Path First)
- Link-state routing protocol
- Hierarchical design based on areas
- Open standard interior routing protocol

###### EIGRP (Enhanced Interior Gateway Routing Protocol)
- Cisco proprietary routing protocol
- Uses composite metric based on bandwidth, delay, load and reliability

#### Network Access Layer
##### ARP (Address Resolution Protocol)
- Provides dynamic address mapping between an IP address and a hardware address

#### PPP (Point-to-Point Protocol)
- Provides a means of encapsulating packets for transmission over a serial link

#### Ethernet
- Defines the rules for wiring and signaling standards of the network access layer

#### Interface Driver
- Provides instruction to a machine for the control of a specific interface on a network device

### TCP/IP Communication Process
- Web server prepares Hypertext Markup language (HTML) page as data to be sent
- The application protocol HTTP header is added to the front of the HTML data. The header contains
various information, including the HTTP version the server is using and a status code indicating it has information
for the web client
- The HTTP application layer protocol delivers the HTML-formatted web page data to the transport layer
- The TCP transport layer protocol is used to manage individual conversations
- The IP information is added to the front of the TCP information. IP assigns the appropiate source and destination IP
addresses. This information is known as an IP packet
- The Ethernet protocol adds information to both ends of the IP packet, known as a data link frame. This frame is delivered
to the neares router along th epath towards the web client. This router removes the Ethernet information analyzes the IP packet, 
determines the best path for the packet, inserts the packet into a new frame, and sends it to the next neighboring router towards the destination. 
Each router removes and adds new data link information before forwarding the packet.
- This data is now transported through the internetwork, which consists of media and intermediary devices
- In Web Client, each protocol header is processed and then removed in the opposite order it was added. The Ethernet
information is processed and removed, followed by the IP protocol information, the TCP information, and finally the HTTP information.
- The web page information is then passed on to the client's web browser software

### Open Standards
Open standards encourage interoperability, competition, and innovation. They also guarantee that no single 
company's product can monopolize the market, or have an unfair advantage over its competition.

Standards organizations are important in maintaining an open Internet with freely accessible specifications and 
protocols that can be implemented by any vendor. A standards organization may draft a set of rules enterely on its own
or in other cases may select a proprietary protocol as the basis for the standard. If a proprietary protocol is
used, it usually involves the vendor who created the protocol.

Standards organizations are usually vendor-neutral, non-profit organizations established to develop and promote
the concept of open standards.

### Internet Standards
Various organizations have different responsibilities for promoting and creating standards for the TCP/IP protocol.

- **Internet Society (ISOC)**: Responsible for promoting the open development and evolution of Internet use throughout the world
- **Internet Architecture Board (IAB)**: Responsible for the overall management and development of Internet standards
- **Internet Engineering Task Force (IETF)**: Develops, updates, and maintains Internet and TCP/IP technologies. 
This includes the process and documents for developing new protocols and updating existing protocols know as Request for Comments (RFC) documents
- **Internet Research Task Force (IRTF)**: Focused on long-term research related to Internet and TCP/IP protocols such
as Anti-Spam Research group (ASRG), Crypto Forum Research Group (CFRG), and Peer-to-Peer Research Group (P2PRG)
- **Internet Corporation for Assigned Names and Numbers (ICANN)**: Based in the United States, coordinates IP address allocation, 
the management of domain names, and assignment of other information used TCP/IP protocols
- **Internet Assigned Numbers Authority (IANA)**: Responsible for overseeing and managing IP address allocation,
domain name management, and protocol identifiers for ICANN

### Electronics and Communications Standard Organizations
- **Institute of Electrical and Electronics Engineers (IEE)**: Organization of electrical engineering and electronics
dedicated to advancing technological innovation and creating standards in a wide area of industries including power and energy,
healthcare, telecommunications, and networking
- **Elecronic Industries Alliance (EIA)**: Best known for its standards related to electrical wiring, connectors,
and the 19-inch racks used to mount networking equipment
- **Telecommunications Industry Association (TIA)**: Responsible for developing communication standards in a variety of areas
including radio equipment, cellular towers, Voice over IP (VoIP), devices, satellite communications, and more
- **International Telecommunications Union-Telecommunication Standardtization Sector (ITU-T):** One of the largest and oldest communication standard
organizations. The ITU-T defines standards for video compression, Internet Protocol Television (IPTV), and broadband communications, such as a digital subscriber line (DSL)

### The Benefits of Using a Layered Model
- Assisting in protocol design because protocols that operate at a specific layer have defined information that
they act upon a defined interface to the layers above and below
- Fostering competition because products from different vendors can work together
- Preventing technology or capability changes in one layer from affecting other layers above and below
- Providing a common language to describe networking functions and capabilities

#### Protocol Model
This type of model closely matches the structure of a particular protocol suite. The TCP/IP model is a protocol
model because it describes the functions that occur at each layer of protocols within the TCP/IP suite. TCP/IP is also used as a reference model.

#### Reference model
This type of model provides consistency within all types of network protocols and services by describing what has to be done
at a particular layer, but not prescribing how it should be accomplished. The OSI model is a widely known internetwork 
reference model, but is also a protocol model for the OSI protocol suite.

### The OSI Reference Model
The OSI model provides an extensive list of functions and services that can occur at each layer. It also describes 
the interaction of each layer with the layers directly above and below. The TCP/IP protocols discussed in this course
are structured around both the OSI and TCP/IP models.

- **Application (7):** The application layer contains protocols used for process-to-process communications
- **Presentation (6):** The presentation layer provides for common representation of the data transferred between application layer services
- **Session (5):** The session layer provides services to the presentation layer to organize its dialogue and to manage data exchange
- **Transport (4):** The transport layer defines services to segment, transfer, and reassemble the data for individual 
communications between the end devices
- **Network (3):** The network layer provides services to exchange the individual pieces of data over the network between identified end devices
- **Data Link (2):** The data link layer protocols describe methods for exchanging data frames between devices over a common media
- **Physical (1):** The physical layer protocols describe the mechanical, electrical, functional, and procedural means 
to activate, maintain, and de-activate physical connections for bit transmission to and from a network device

The functionality of each layer and the relationship between layers will become more evident throughout this course as the protocols
are dicussed in more detail.

**NOTE:** Whereas the TCP/IP model layers are referred to only by name, the seven OSI model layers are more often referred ttao by number
rather than by name.

### The TCP/IP Protocol Model
The TCP/IP protocol model for internetwork communications was created in the early 1970s and is sometimes referred to as the Internet model.
- **Application:** Represents data to the user, plus encoding and dialog control
- **Transport:** Supports communication between various devices across diverse networks
- **Internet:** Determines the best path through the network
- **Network Access:** Controls the hardware devices and media that make up the network

### Message Segmentation
Segmentation is the process of dividing the data into smaller, more manageable pieces to send over the network. 
Segmenting messages has two primary benefits:
- Many conversations can be interleaved on the network, called multiplexing
- Increase the efficiency of network communications. If part of the message fails to make it to the destination, due
to failure in the network or network congestion, only the missing parts need to be retransmitted

### Protocol Data Units
The form that a piece of data takes at any layer is called a protocol data unit (PDU). During encapsulation, each succeeding layer
encapsulates the PDU that it receives from the layer above in accordance with the protocol being used. At each stage of the process, a PDU
has a different name to reflect its new functions. Altough there is no universal naming convention for PDUs.
- **Data:** The general term for the PDU used at the application layer
- **Segment:** Transport layer PDU
- **Packet:** Network layer PDU
- **Frame (medium dependent):** Data Link layer PDU
- **Bits:** Physical layer PDU, used when physically transmitting data over the medium

### Network Addresses
The network and data link layers are responsible for delivering the data from the source device to the destination device.

- **Network layer source and destination addresses:** Responsible for delivering the IP packet from the original source 
to the final destination, either on the same network or to a remote network
- **Data link layer source and destination addresses:** Responsible for delivering the data link frame from one network 
interface card (NIC) to another NIC on the same network

An IP address is the network layer, or Layer 3, logical address used to deliver the IP packet from the original source
to the final destination.

The IP packet contains two IP addresses:
- **Source IP address**
- **Destination IP address**

### Data Link Addresses
The data link, or Layer 2, physical address has a different role. The purpose of the data link address is to deliver
the data link frame from one network interface to another network interface on the same network.

Before an IP packet can be sent over a wired or wireless network, it must be encapsulated in a data link frame 
so it can be transmitted over the physical medium.

As the IP packet travels from host-to-router, router-to-router, and finally router-to-host, at each point
along the way the IP packet is encapsulated in a new data link frame. Each data link frame contains the source
data link address of the NIC card sending the frame, and the destination data link address of the NIC card receiving the frame.

The Layer 2, data link protocol is only used to deliver the packet from NIC-to-NIC on the same network. The router removes
the Layer 2 information as it is received on one NIC and adds new data link information before forwarding out the exit NIC on its
way towards the final destination.

The IP packet is encapsulated in a data link frame that contains data link information, including a:
- **Source data link address:** The physical address of the device's NIC that is sending the data link frame
- **Destination data link address:** The physical address of the NIC that is receiving the data link frame. This address
is either the next hop router or of the final destination device

### Devices on the Same Network
#### Role of the Network Layer Addresses
The network layer addresses, or IP addresses, indicate the original source and final destination. An IP address contains two parts:
- **Network portion:** The left-most part of the address that indicates which network the IP address is a member. 
All devices on the same network will have the same network portion of the address
- **Host portion:** The remaining part of the address that identifies a specific device on the network. 
The host portion is unique for each device on the network.

**NOTE:** The subnet mask is used to identify the network portion of an address from the host portion.

#### Role of the Data Link Layer Addresses
When the sender and receiver of the IP packet are on the same network, the data link frame is sent directly to the receiving device.
On an Ethernet network, the data link addresses are known as Ethernet (Media Access Control) addresses. 
MAC addresses are physically embedded on the Ethernet NIC.
- **Source MAC address:** This is the data link address, or the Ethernet MAC address, of the device that sends the data
link frame with the encapsulated IP packet.
- **Destination MAC address:** When the receiving device is on the same network as the sending device, this is the 
data link address of the receiving device.

### Devices on a Remote Network
#### Role of the Network Layer Addresses
When the sender of the packet is on a different network from the receiver, the source and destination IP addresses
will represent hosts on different networks. This will be indicated by the network portion of the IP address of the destination host.
- **Source IP address:** The IP address of the sending device
- **Destination IP address:** The IP address of the receiving device

#### Role of the Data Link Layer Addresses
When the sender and receiver of the IP packet are on different networks, the Ethernet data link frame cannot be sent directly
to the destination host because the host is not directly reachable in the network of the sender. The Ethernet frame must be sent to another
device known as the router or default gateway.
- **Source MAC address:** The Ethernet MAC address of the sending device
- **Destination MAC address:** When the receiving device, the destination IP address, is on different network from 
the sending device, the sending device uses the Ethernet MAC address of the default gateway or router.

It is important that the IP address of the default gateway be configured on each host on the local network. All packets to a destination
on remote networks are sent to the default gateway.

## Chapter 4: Network Access
### The Physical Layer
The OSI physical layer provides the means to transport the bits that make up a data link layer frame across
the network media. This layer accepts a complete frame from the data link layer and encodes it as a series
of signals that are transmitted onto the local media. The encoded bits that comprise a frame are received by
either an end device or an intermediate device.

- User data is segmented by the trasport layer
- Placed into packets by the network layer
- Encapsulated into frames by the data link layer
- The physical layer encodes the frames and creates the electrical, optical, or radio wave signals that represent 
the bits in each frame
- These signals are then sent on the media, one at a time.
- The destination node physical layer retrieves these individual signals from the media, restores them to their
bit representations, and passes the bits up to the data link layer as a complete frame

### Physical Layer Media
#### Types of network media
- **Copper cable:** The signals are patterns of electrical pulses
- **Fiber-optic cable:** The signals are patterns of light
- **Wireless:** The signals are patterns of microwave transmissions

To enable physical layer interoperability, all aspects of these functions are governed by standards organizations.

### Physical Layer Standards
The services and protocols in the TCP/IP suite are defined by the Internet engineering Task Force (IETF).\
The physical layer consists of electronic curcuitry, media, and connectors developed by engineers. Therefore,
it is appropriate that the standards governing this hardware are defined by the relevant electrical and communications
engineering organizations.\
There are many different international and national organizations, regulatory government organizations, and private
companies involved in establishing and maintaining physical layer standards.
- International Organization for Standardization (**ISO**)
- Telecommunications Industry Association/Electronic Industries Association (**TIA/EIA**)
- International Telecommunication Union (**ITU**)
- American National Standards Institute (**ANSI**)
- Institute of Electrical and Electronics Engineers (**IEEE**)
- National telecommunications regulatory authorities including the Federal Communication Commission (**FCC**) in
the USA and the European Telecommunications Standards Institute (**ETSI**)

In addition to these, there are often regional cabling standards groups such as **CSA** (Canadian Standards Association),
**CENELEC** (European Commitee for Electrotechnical Standardization), and **JSA/JIS** (Japanese Standards Association),
developing local specifications.

### Functions
#### Physical Components
The physical components are the electronic hardware devices, media, and other connectors that transmit and carry the signals
to represent the bits. Hardware components such as NICs, interfaces and connectors, cable materials, and
cable designs are all specified in standards associated with the physical layer.

#### Encoding
Encoding is the method or pattern used to represent digital information that can be recognized by both the sender
and the receiver.

#### Signaling
The physical layer standards must define what type of signal represents a "1" and what type of signal represents
a "0". This can be as simple as a change in the level of an electrical signal or optical pulse.

There are many ways to transmit signals. A common method to send data is using modulation techniques. Modulation
is the process by which the characteristic of one wave (the signal) modifies another wave (the carrier).

The nature of the actual signals representing the bits on the media will depend on the signaling method in use.

### Bandwidth
Bandwidth is the capacity of a medium to carry data. Digital bandwidth measures the amount of data that can flow 
from one place to another in a given amount of time. Bandwith is typically measured in kb/s, Mb/s, or Gb/s.

A combination of factors determines the practical bandwidth of a network:
- The properties of the physical media
- The technologies chosen for signaling and detecting network signals

**NOTE:** In a 10Mb/s and 100Mb/s Ethernet, the bits are sent at the speed of electricity. The difference is the 
number of bits that are transmitted per second.

### Throughput
Throughput is the measure of the transfer of bits across the media over a given period of time.

Dute to a number of factors, throughput usually does not match the specified bandwidth in physical layer 
implementations. Many factors influence throughput, including:
- The amount of traffic
- The type of traffic
- The latency created by the number of network devices encountered between source and destination

Latency refers to the amount of time, to include delays, for data to travel from one given point to another.

In an internetwork or network with multiple segments, throughput cannot be faster than the slowest link in the path
from source to destination. Even if all or most of the segments have high bandwidth, it will only take one
segment in the path with low throughput to create a bottleneck to the throughput of the entire network.

There is a third measurement to assess the transfer of usable data. Goodput is the measure of usable data transferred
over a given period of time. Goodput is throughput minus traffic overhead for establishing sessions, acknowledgments, 
and encapsulation.

### Types of Physical Media
Various standards organizations have contributed to the definition of the physical, electrical, and mechanical
properties of the media available for different data communications. These specifications guarantee that
cables and connectors will function as anticipated with different data link layer implementations.

As an example, standards for copper media are defined for the:
- Type of copper cabling used
- Bandwidth of the communication
- Type of connectors used
- Pinout and color codes of connections to the media
- Maximum distance of the media (100 mts)

### Characteristics of Copper Cabling
Networks use copper media because it is inexpensive, easy to install, and has low resistance to electrical current.
However, copper media is limited by distance and signal interference.

Data is transmitted on copper cables as electrical pulses. A detector in the network interface of a destination device
must receive a signal that can be successfully decoded to match the signal sent. However, the longer the signal travels,
the more it deteriorates. This is referred to as signal attenuation. For this reason, all copper media must follow
strict distance limitations as specified by the guiding standards.

The timing and voltage values of the electrical pulses are also susceptible to interference from two sources:
- **Electromagnetic Interference (EMI) or radio frequency interference (RFI)** - EMI and RFI signals can distort 
and corrupt the data signals being carried by copper media. Potential sources of EMI and RFI include radio waves
and electromagnetic devices, such as flourescent lights or electric motors.

- **Crosstalk** - Crosstalk is a disturbance caused by the electric or magnetic fields of a signal on one wire to
the signal in an adjacent wire. When an electrical current flows through a wire, it creates a small, circular magnetic
field around the wire, which can be picked up by an adjacent wire.

To counter the negative effects of EMI and RFI, some types of copper cables are wrapped in metallic shielding 
and require proper grounding connections.

To counter the neggative effects of crosstalk, some types of copper cables have opposing circuit wire pairs 
twisted together, which effectively cancels the crosstalk.

The susceptibility of copper cables to electronic noise can also be limited by:
- Selecting the cable type or category most suited to a given networking environment.
- Designing a cable infrastructure to avoid known and potential sources of interference in the building structure.
- Using cabling techniques that include the proper handling and termination of the cables.

### Copper Media
There are three main types of copper media used in networking:
- **Unshielded Twisted-Pair (UTP)**
- **Shielded Twisted-Pair (STP)**
- **Coaxial**

These cables are used to interconnect nodes on a LAN and infrastructure devices such as switches, routers, and 
wireless access points. Each type of connection and the accompanying devices has cabling requirements stipulated
by physical layer standards.

Different physical layer standards specify the use of different connectors. Networking media use modular jacks
and plugs to provide easy connection and disconnection. Also, a single type of physical connector may be used
for multiple types of connections.

### Unshielded Twisted-Pair Cable (UTP)
UTP cabling, terminated with RJ-45 connectors, is used for interconnecting network hosts with intermediate 
networking devices, such as switches and routers.

In LANs, UTP cable consists of four pairs of color-coded wires that have been twisted together and then encased
in a flexible plastic sheath that protects from minor physical damage. The twisting of wires helps protect
against signal interference from other wires.

- **Outer Jacket**: Protects the copper wire from physical damage
- **Twisted-Pair**: Protects the signal from interference
- **Color-Coded Plastic Insulation**: Electrically isolates wires from each other and identifies each pair

### Shielded Twisted-Pair Cable (STP)
STP provides better noise protection than UTP cable. However, STP is significantly more expensive and difficult
to install. Like UTP cable, STP uses an RJ-45 connector.

STP cables combine the techniques of shielding to counter EMI and RFI, and wire twisting to counter crosstalk.
To gain the full benefit of the shielding, STP cables are terminated with special shielded STP data connectors.
If the cable is improperly grounded, the shield may act as an antenna and pick up unwanted signals.

The STP cable uses:
- Four twisted pairs of wires
- Foil Shield
- Braided or Foil Shield
- Jacket

### Coaxial Cable
Coaxial cable, or coax for short, gets its name from the fact that there are two conductors that share the 
same axis.
- A copper conductor used to transmit the electronic signals
- A layer of flexible plastic insulation sorrounding a copper conductor
- The insulating material is surrounded in a woven copper braid, or metallic foil, that acts as the second wire
in the circuit and as a shield for the inner conductor. This second layer, or shield, also reduces the amount
of outside electromagnetic interference
- The entire cable is covered with a cable jacket to prevent minor physical damage

UTP cable has esentially replaced coaxial cable in modern Ethernet installations, the coaxial cable design
is used in:

- **Wireless Installations:** Coaxial cables attach antennas to wireless devices. The coaxial cable carries radio
frequency (RF) energy between the antennas and the radio equipment
- **Cable Internet Installations:** Cable service providers provide Internet connectivity to their customers by
replacing portions of the coaxial cable and supporting amplification elements with fiber-optic cable. However,
the wiring inside the customer's premises is still coax cable.

### Copper Media Safety
Electrical hazards are a potential problem because copper wires can conduct electricity in undesirable ways.
This could subject personnel and equipment to a range of electrical hazards.

The result of undesirable voltages and currents can include damage to network devices and connected computers,
or injury to personnel. It is important that copper cabling be installed appropriately, and according to the
relevant specifications and building codes, in order t oavoid potentially dangerous and damaging situations.

### Properties of UTP Cabling
UTP cable does not use sihelding to counter the effects of EMI and RFI. Instead, cable designers have discovered
that they can limit the negative effect of crosstalk by:
- **Cancellation:** Designers now pair wires in a circuit. When two wires in an electrical circuit are placed close
together, their magnetic fields are the exact opposite of each other. Therefore, the two magnetic fields cancel
each other and also cancel out any outside EMI and RFI signals
- **Varying the number of twists per wire pair:** To further enhance the cancellation effect of paired circuit wires,
designers vary the number of twists of each wire pair in a cable. UTP cable must follow precise specifications
governing how many twists or braids are permitted per meter (3.28 feet) of cable. Each colored pair is twisted a different
number of times.

UTP cable relies solely on the cancellation effect produced by the twisted wire pairs to limit signal degradation
and effectively provide self-shielding for wire pairs within the network media.

### UTP Cabling Standards
UTP cabling conforms to the standards established jointly by the TIA/EIA.  Some of the elements defined are:
- Cable types
- Cable lengths
- Connectors
- Cable termination
- Methods of testing cable

IEEE rates UTP cabln according to its performance. Cables are placed into categories based on their ability
to carry higher bandwidth rates.

Cables in higher categories are designed and constructed to support higher data rates. As new gigabit speed Ethernet
technologies are being developed and adopted, Cat5e is now the minimally acceptable cable type, with Cat6 being
the recommended type for new building installations.

- **Category 3 Cable (UTP)**
  - Used for voice communication
  - Most often used for phone lines
- **Category 5 and 5e Cable (UTP)**
  - Used for data transmission
  - Cat5 supports 100 Mb/s and can support 1000 Mb/s, but it is not recommended
  - Cat5e supports 1000 Mb/s
- **Category 6 Cable (UTP)**
  - Used for data transmission
  - An added separator is between each pair of wires allowing it to function at higher speeds
  - Supports 1000 Mb/s - 10 Gb/s, though 10 Gb/s is not recommended

Some manufacturers are making cables exceeding the TIA/EIA Category 6a specifications and refer to these as
Category 7.

### UTP Connectors
UTP cable is usually terminated with an RJ-45 connector. This connector is used for a range of physical layer
specifications, one of which is Ethernet. The TIA/EIA-568 standard describes the wire color codes to pin
assignments (pinouts) for Ethernet cables.

Each time copper cabling is terminated; there is the possibility of signal loss and the introduction of noise
into the communication circuit. When terminated improperly, each cable is a potential source of physical
layer performance degradation. It is essential that all copper media terminations be of high quality to ensure
optimum performance with current and future network technologies.

### Types of UTP Cable
The following are the main cable types that are obtained by using specific wiring conventions:
- **Ethernet Straight-through:** The most common type of networking cable. It is commonly used to interconnect
a host to a switch and a switch to a router
- **Ethernet Crossover:** A cable used to interconnect similar devices. For example to connect a switch
to a switch, a host to a host, or a router to a router
- **Rollover:** A Cisco proprietary cable used to connect a workstation to a router or switch console port

**Wire Pairs:**
- **T568A**
  - PAIR 1 **BLUE** SOL/STR - 4, 5
  - PAIR 2 **YELLOW** STR/SOL - 3, 6
  - PAIR 3 **GREEN** STR/SOL - 1, 2
  - PAIR 4 **BROWN** STR/SOL - 7, 8
- **T568B**
  - PAIR 1 **BLUE** SOL/STR - 4, 5
  - PAIR 2 **YELLOW** STR/SOL - 1, 2
  - PAIR 3 **GREEN** STR/SOL - 3, 6
  - PAIR 4 **BROWN** STR/SOL - 7, 8

Cable Type | Standard | Application
--- | --- | ---
Ethernet Straight-through | Both ends T58A or both ends T568B | Connects a network host to a network device such as a switch or hub
Ethernet Crossover | One end T568A, Other end T568B | Connects two network hosts or two network intermediary devices (switch to switch, or router to router)
Rollover | Cisco proprietary | Connects a workstation serial port to a router console port, using an adapter

Ussing a crossover or straight-through cable incorrectly between devices may not damage the devices, but connectivity
and communication between the devices will not take place.

### Testing UTP Cables
After installation, a UTP cable tester should be used to test for the following parameters:
- Wire map
- Cable length
- Signal loss due to attenuation
- Crosstalk

It is recommended to check thoroughly that all UTP installation requirements have been met.

### Properties of Fiber-Optic Cabling
Optical fiber cable transmits data over longer distances and at higher bandwidths than any other networking 
media. Unlike copper wires, fiber-optic cable can transmit signals with less attenuation and is completely
immune to EMI and RFI. Optical fiber is commonly used to interconnect network devices.

Optical fiber is a flexible, but extremely thin, transparent strand of very pure glass, not much bigger than
a human hair. Bits are encoded on the fiber as light impulses. The fiber-optic cable acts as a waveguide,
or "light pipe", to transmit light between the two ends with minimal loss of signal.

Fiber-optic cabling is now being used in four types of industry:
- **Enterprise Networks:** Used for backbone cabling applications and interconnecting infrastructure devices
- **Fiber-to-the-Home (FTTH):** Used to provide always-on broadband services to homes and small businesses
- **Long-Haul networks:** Used by service providers to connect countries and cities
- **Submarine Cable Networks:** Used to provide reliable high-speed, high-capacity solutions capable of surviving
in harsh undersea environments up to transoceanic distances.

### Fiber Media Cable Design
Optical fiber is composed of two kinds of glass (core and cladding) and a protective outer shield (jacket).

- **Jacket:** Typically a PVC jacket that protects the fiber against abrasion, moisture, and other contaminants.
This outer jacket composition can vary depending on the cable usage
- **Strenghtening Material:** Surrounds the buffer, prevents the fiber cable from eing stretched when it is 
being pulled. The material used is often the same material used to produce bulletproof vests
- **Buffer:** Used to help shield the core and cladding from damage
- **Cladding:** made from slightly different chemicals than those used to create the core. It tends to act like
a mirror by reflecting light back into th ecore of the fiber. This keeps light in the core as it travels down 
the fiber.
- **Core:** The core is actually the light transmission element at the center of the optical fiber. This core
is typically silica or glass. Light pulses travel through the fiber core

### Types of Fiber Media
Light pulses representing the transmitted data as bits on the medi aare generated by either:
- Lasers
- Light emitting diodes (LEDs)

Electronic semiconductor devices called photodiodes detect the light pulses and convert them to voltages.

Fiber-optic cables are broadly classified into two types:
- **Single-mode fiber (SMF):** Consists of a very small core and uses expensive laser technology to send a
single ray of light. Less dispersion. Popular in long-distance situations spanning hundreds of kilometers, such as those
required in long haul telephony and cable TV applications.
- **Multimode fiber (MMF):** Consists of a larger core and uses LED emitters to send light pulses. Allows greater 
dispersion and therefore, loss of signal. Light from an LED enters the multimode fiber at different angles. 
Popular in LANs because they can be powered by low-cost LEDs. It provides bandwidth up to 10Gb/s over link lengths of up to 550 meters.

One of the highlighted differences between multimode and single-mode fiber is the amount of dispersion.
Dispersion refers to the spreading out of a light pulse over time. The more dispersion there is, the greater 
the loss of signal strength.

### Fiber-Optic Connectors
A variety of optical fiber connectors are available. The main differences among the types of connectors are
dimensions and methods of coupling. Businesses decide on the types of ocnnectors that will be used, based on their
equipment.

- **Straight-Tip (ST):** One of the first connector types used. The connector locks securely with a "twist-on/
twist-off" bayonet style mechanism
- **Subscriber Connector (SC):** Sometimes referred to as square connector or standard connector. It is a widely
adopted LAN and WAN connector that uses a push-pull mechanism to ensure positive insertion. This connector
type is used with multimode and single-mode fiber
- **Lucent Connector (LC) Simplex:** A smaller version of the fiber-optic SC connector. It is sometimes called
a little or local connector and is quickly growing in popularity due to its smaller size
- **Duplex Multimode LC:** Similar to a LC simplex connector, but using a duplex connector

Until recently, light could only travel in one direction over optical fiber, two fibers were required to suport the
full duplex operation. Therefore, fiber-optic patch cables bundle together two optical fiber cables and terminate
them with a pair of standard, single fiber connectors. Some fiber connectors accept both the transmitting and
receiving fibers in a single connector known as a duplex connector.

Fiber patch cords are required for interconnecting infrastructure devices. The use of color distinguishes between
single-mode and multimode patch cords.
- **Single-mode:** YELLOW JACKET
- **Multimode:** ORANGE JACKET

Fiber cables should be protected with a small plastic cap when not in use.

### Testing Fiber Cables
Terminating and splicing fiber-optic cabling requires special training and equipment. Incorrect termination of
fiber-optic media will result in diminished signaling distances or complete transmission failure.

Three common types of fiber-optic termination and splicing errors are:
- **Misalignment:** The fiber-optic media are not precisely aligned to one another when joined
- **End gap:** The media does not completely touch at the splice or connection
- **End finish:** The media ends are not well polished or dirt is present at the termination

A quick and easy field test can be performed by shining a bright flashlight into one end of the fiber while 
observing the other end. If light is visible, the fiber is capable of passing light. Although this does not
ensure performance, it is a quick and inexpensive way to find a broken fiber.

An Optical Time Domain Reflectometer (OTDR) can be used to test each fiber-optic cable segment. This device
injects a test pulse of light into the cable and measures backscatter and reflection of light detected as a
function of time. The OTDR will calculate the approximate distance at which these faults are detected along
the length of the cable.

### Fiber versus Copper
There are many advantages to using fiber-optic cable compared to copper cables.

Implementation Issues | UTP Cabling | Fiber-optic Cabling
--- | --- | ---
Bandwidth supported | 10 Mb/s - 10 Gb/s | 10 Mb/s - 100 Gb/s
Distance | Relatively short (1 - 100 meters) | Relatively high (1 - 100, 000 meters)
Immunity to EMI and RFI | Low | High (Completely immune)
Immunity to electrical hazards | Low | High (Completely immune)
Media and connector costs | Lowest | Highest
Installation skills required | Lowest | Highest
Safety precautions | Lowest | Highest

At present, in mos tenterprise environments, optical fiber is primarily used as backbone cabling for high-traffic
point-to-point connections between data distribution facilities and for the interconnection of buildings in
multi-building campuses. Because optical fiber does not conduct electricity and has a low signal loss, it is
well suited for these uses.

### Properties of Wireless Media
Wireless media carry electromagnetic signals that represent the binary digits of data communications using
radio or microwave frequencies.

Wireless media provides the greatest mobility options of all media, and the number of wireless-enabled devices
continues to increase. As network bandwidth options increase, wireless is quickly gaining in popularity
in enterprise networks.

Wireless does have some areas of concern, including:
- **Coverage area:** Wireless data communication technologies work well in open environments. However, certain
construction materials used in buildings and structures, and the local terrain, will limit th eeffective coverage
- **Interference:** Wireless is susceptible to interference and can be disrupted by such common devices as household
cordless phones, some types of fluorescent lights, microwave ovens, and other wireless communications
- **Security:** Wireless communication coverage requires no access to a physical strand of media. Therefore,
devices and users, not authorized for access to the netowrk, can gain access to the transmission. Network 
security is a major component of wireless network administration
- **Shared medium:** WLANs operate in half-duplex, which means only one device can send or receive at a time.
The wireless medium is shared amongst all wireless users. The more users needing to access the WLAN simultaneously,
results in less bandwidth for each user.

Although wireless is increasing in popularity for desktop ocnnectivity, copper and fiber are the most popular
phyiscal layer media for network deployments.

### Types of Wireless Media
The IEE and telecommunications Industry standards for wireless data communications cover oth th edata link
and physical layers.

- **Wi-Fi: Standard IEE 802.11**:
Wireless LAN (WLAN) technology, commonly referred to as Wi-Fi. WLAN uses a contention-based protocol known as
Carrier Sense Multiple Access/Collision Avoidance (CSMA/CA). The wireless NIC must first listen before transmitting
to determine if the radi ochannel is clear. if another wireless device is transmitting, then the NIC must wait until
the channel is clear.

- **Standard IEEE 802.15: Bluetooth**:
Wireless Personal Area Netowrk (WPAN) standard, commonly known as "Bluetooth", uses a device pairing process
to communicate over distances from 1 to 100 meters.

- **Standard IEEE 802.16: WiMAX**:
Commonly known as Worldwide Interoperability for Microwave Access (WiMAX), uses a point-to-multipoint topology
to provide wireless broadband access.

**NOTE:** Other wireless technologies such as cellular and satellite communications can also provide data
network connectivity.

In each of these standards, physical layer specifications are applied to areas that include:
- Data to radio signal encoding
- Frequency and power of tranmission
- Signal reception and decoding requirements
- Antenna design an dconstruction

Wi-Fi is a trademark of the Wi-Fi Alliance. Wi-Fi is used with certified products that belong to WLAN devices
that are based on the IEEE 802.11 standards.

### Wireless LAN
A common wireless data implementation is enabling devices to connect wirelessly via a LAN. In general, a wireless
LAN requires the following network devices:
- **Wireless Access Point (AP):** Concentrates the wireless signals from users and connects to the existing
copper-based network infrastructure, such as Ethernet. Home and small business wireless routers integrate the
functions of a router, switch, and access point into one device as shown in the figure.
- **Wireless NIC adapters:** Provide wireless communication capability to each network host

### The Data Link Layer
The data link layer of the OSI model (Layer 2) is responsible for:
- Allowing the upper layers to access the media
- Accepting Layer 3 packets and packaging them into frames
- Preparing network data for the physical network
- Controlling how data is placed and received on the media
- Exchanging frames between nodes over a physical network media, such as UTP or fiber-optic
- Receiving and directing packets to an upper layer protocol
- Performing error detection

The Layer 2 notation for network devices connected to a common media is called a node. Nodes build and forward 
frames. The OSI data link layer is responsible for the exchange of Ethernet frames between source and destination 
nodes over a physical network media.

The data link layer effectively separates the media transitions that occur as the packet is forwarded from the
communication processes of the higher layers.

### Data Link Sublayers
The data link layer is divided into two sublayers:
- **Logical Link Control (LLC):** This upper sublayer communicates with the network layers. It places information
in the frame that identifies which network layer protocol is being used for the frame. This information allows
multiple Layer 3 protocols, such as IPv4 and IPv6, to utilize the same network interface and media
- **Media Access Control (MAC):** This lower sublayer defines the media access processes performed by the
hardware. It provides data link layer addressing and access to various network technologies

### Media Access Control
As packets travel from th esource host to the destination host, they typically traverse over different physical 
networks. These physical networks can consists of different types of physical media such as copper wires,
optical fibers, and wireless consisting of electromagnetic signals, radio and microwave frequencies and satellite
links.

Without the data link layer, network layer protocols such as IP, would have to make provisions for connecting to
every type of media that could exist along a delivery path. Moreover, IP would have to adapt eveyr time a new
network technology or medium was developed. This process would hamper protocol and network media innovation and
development. This is a key reason for using a layered approach to networking.

### Providing Acccess to Media
Different media access control methods may be required during a single communication. Each network environment that
packets encounter as they travel from a local host to a remote host can have different characteristics.

Router interfaces encapsulate the packet into th eappropiate frame, and a suitable media access control method
is used to access each link. In any given exchange of network layer packets, there may be numerous data link
layers and media transitions.

At each hop along the path, a router:
- Accepts a frame from a medium
- De-encapsulates the frame
- Re-encapsulates the packet into a new frame
- Forwards the new frame appropriate to the medium of that segment of the physical network

### Data Link Layer Standards
The Internet Engineering Task Force (IETF) maintains the functional protocols and services for the TCP/IP protocol
suite in the upper layers, the IETF does not define the functions and operatoin of that model's network access
layer.

Engineering organizations that define open standards and protocols that apply to the network access layer include:
- Institute of Electrical and Electronics Engineers **(IEEE)**
- International Telecomunication Union **(ITU)**
- International Organization for Standardization **(ISO)**
- Americna National Standards Institute **(ANSI)**

### Controlling Access to the Media
Media access control is the quivalent of traffic rules that regulate the the entrance of motor vehicles onto
roadway. The absence of any media access control would be the equivalent of vehicles ignoring all other traffic
and entering th eroad without regard to other vehicles. However, not all roads and entrances are the same.
Traffic can enter the road by merging, by waiting for its turn at a stop sign, or by obeyin signal lights. 
A driver follows a different set of rules for each type of entrance.

In the same way, there are different methods to regulate placing frames onto the media. The protocols at the
data link layer define the rules for access to different media. These media access control techniques define
if and how the nodes share the media.

The actual media access control method used depends on:
- **Topology -** How the connection between the nodes apears to the data link layer.
- **Media sharing -** How the nodes share the media. The media sharing can be point-to-point, such as in WAN
connections, or shared such as in LAN networks.

### Physical and Logical Topologies
The topology of a network is the  arrangement or relationship of the network devices and the interconnections
between them. LAN and WAN topologies can be viewed in two ways:
- **Physical topology -** Refers to the physical connections and identifies how end devices and infrastructure
devices such as routers, switches, and wireless access points are interconnected. Physical topologies are
usually point-to-point or star
- **Logical topology -** Refers to the way a network transfers frames from one node to the next. This arrangement
onsists of virtual connections between the nodes of a network. These logical signal paths are defined by data
link layer protocols. The logical topology of point-to-point links is relatively simple while shared media offers
different access control methods.

The data link layer "sees" the logical topology of a network when controlling data access to the media. It is
the logical topology that influences the type of network framing and media access control used.

### Common Physical WAN Topologies
WANs are commonly interconnected using the following physical topologies:
- **Point-to-Point -** This is the simplets topology that consists of a permanent link between two endpoints.
For this reaon, this is a very popular WAN topology.
- **Hub and Spoke -** A WAN version of the star topology in which a central site interconnects branch sites using
point-to-point links.
- **Mesh -** This topology providees high avaliability, but requires that every end system be interconnected to
every other system. Therefore, the administrative and physical costs can be significant. Each link is essentially
a point-to-point link to the other node.

A hybrid is a variation or combination of any of the above topologies.

### Physical Point-to-Point Topology
Physical point-to-point topologies directly connect two nodes.
- Two nodes do not have to share the media with other hosts
- A node does not have to make any determination about whether an incoming frame is destined for it or another 
node
- The logical data link protocols can be very simple, as all frames on the media can only travel to or from the two nodes.
- The frames are placed on the media by the node at one end and taken from the media by the node at the other end
of the point-to-point circuit

### Logical Point-to-Point Topology
The end nodes communicating in a point-to-point network can be physically connected via a number of intermediate
devices. However, the use of physical devices in the network does not affect the logical topology.

A virtual circuit is a logical connection created within a network between two network devices. The two nodes
on either end of the virtual circuit exchange the frames with each other. This occurs even if the frames
are directed through intermediary devices. Virtual circuits are important logical communication constructs
used by some Layer 2 technologies.

The media access method used by the data link protocol is determined by the logical point-to-point topology,
not the physical topology. This means that the logical point-to-point connection between two nodes may not
necessarily be between two physical nodes at each end of a single physical link.

### Physical LAN Topologies
In shared media LANs, end devices can be interconnected using the following physical topologies:
- **Star -** End devices are connected to a central intermediate device. Early star topologies interconnected
end devices using Ethernet hubs. However, star topologies now use Ethernet switches. The star topology is easy
to install, very scalable (easy to add and remove end devices), and easy to troubleshoot
- **Extended Star -** In a extended star topology, additional Ethernet switches interconnect other star topologies.
An extended star is an example of a hybrid topology
- **Bus -** All end systems are chained to each other and terminated in some form on each end. Infrastructure
devices such as switches are not rquired to interconnect the end devices. Bus topologies using coax cables were
used in legacy Ethernet networks because it was inexpensive and easy to set up
- **Ring -** End systems are connected to their respective neighbor forming a ring. Unlike the bus topology, the
ring does not need to be terminated. Ring topologies were used in legacy Fiber Distributed Data Interface (FDDI)
and Token Ring networks

### Half and Full Duplex
Duplex communications refer to the direction of data transmission between two devices.
- **Half-duplex communication -** Both devices can transmit and receive on the media but cannot do so simultaneously.
- **Full-duplex communication -** Both devices can transmit and receive on the media at the same time.

It is important that two interconnected interfaces, such as a host's NIC and an interface on an Ethernet switch
opearte using the same duplex mode. Otherwise, there will be a duplex mismatch creating inefficiency and latency
on the link.

### Media Access Control Methods
Some network topologies share a common medium with multiple nodes. These are called multi-access networks. Ethernet
LANs and WLANs are examples of a multi-access network. At any one time, there may be a number of devices attempting
to send and receive data using the same network media.

Some multi-access networks require rules to govern how devices share the physical media. There are two basic
access control methods for shared media:
- **Contention-based access -** All nodes operating in half-duplex compete for the use of the medium, but only one
device can send at a time. However, there is a process if more than one device transmits at the same time. Ethernet LANs
using hubs and WLANs are examples of this type of access control

- **Controlled access -** Each node has its own time to use the medium. These deterministic types of networks
are inefficient because a device must wait its turn to access the medium. Legacy Token Ring LANs are an example
of this type of access control

By default, Ethernet switches operate in full-duplex mode. This allows the switch and the full-duplex connected
device to send and receive simultaneously.

### Contention-Based Access - CSMA/CD
WLANs, Ethernet LANs with hubs, and legacy Ethernet bus networks are all examples of contention-based access
networks. All of these networks operate in half-duplex mode. This requires a process to govern when a device
can send and what happens when multiple devices send at the same time.

The Carrier Sense Multiple Access/Collision Detection process is used in half-duplex Ethernet LANs. The CSMA
process is as follows:

- PC1 has an Ethernet frame to send to PC3
- PC1's NIC needs to determine if anyone is transmitting on the medium. If it does not detect a carrier signal,
it will assume the network is available to send
- PC1's NIC sends the Ethernet Frame
- The Ethernet hub receives the frame. An Ethernet hub is also known as a multiport repeater. Any bits received
on an incoming port are regenerated and sent out all other ports
- If another device, such as PC2, wants to transmit, but is currently receiving a frame, it must wait until the channel
is clear
- All devices attached to the hub will receive the frame. Because the frame has a destination data link address for PC3,
only that device will accept and copy in the entire frame. ALl other devices' NICs will ignore the frame.

If two devices transmit at the same time, a collision will occur. Both devices will detect the collision on the
network, this is the collision detection (CD). This is done by the NIC comparing data transmitted with data received,
or by recognizing the signal amplitude is higher than normal on the media. The data sent by both devices
will be corrupted and will need to be resent.

### Contention-Based Access - CSMA/CA
Another form of CSMA that is used by IEEE 802.11 WLANs is Carrier Sense Multiple Access/Collision Avoidance (CSMA/CA).
CMSA/CA uses a method similar to CSMA/CD to detect if the media is clear. CMSA/CA also uses additional
techniques. CMSA/CA does not detect collisions but attempts to avoid them by waiting before trnasmitting. Each
device that transmits includes the time duration that it needs for the transmission. All other wireless devices
receive this information and know how long the medium will be unavailable. After a wireless device sends an 802.11 
frame, the receiver returns an acknowledgment so that the sender knows the frame arrived.

Whether it is an Ethernet LAN using hubs, or a WLAN, contention-based systems do not scale well under heavy media use.
It is important to note that Ethernet LANs using switches do not use a contention-based system because the
switch and the host NIC operate in full-duplex mode.

### The Frame
Is a key element of each data link layer protocol. Altough there are may different data link layer protocols
that describe data link layer frames, each frame type has three basic parts:
- Header
- Data
- Trailer

### Frame Fields
Framing breaks the stream into decipherable groupings, with control information inserted in the header
and trailer as values in different fields. This format gives the physical signals a structure than can be
received by nodes and decoded into packets at the destination.

Generic frame field types include:
- **Frame start and stop indicator flags -** Used to identify the beginning and end limits of the frame
- **Addressing -** Indicates the source and destination nodes on the media
- **Type -** Indentifies the Layer 3 protocol in the data field
- **Control -** Identifies special flow control services such as quality of service (QoS). QoS is used to give forwarding
priority to certain types of messages. Data link frames carrying voice over IP (VoIP) packet normally receive
priority because they are sensitive to delay
- **Data -** Contains the frame payload (i.e., packet header, segment header, and the data)
- **Error Detection -** These frame fields are used for error detection and are included after the data to form the trailer

Not all protocols include all of these fields. The standards for a specific data link protocol define the 
actual frame format.

Data link layer protocols add a trailer to the end of each frame. The trailer is used to determine if the frame
arrived without error. This process i scalled error detection and is accomplished by placing a logical or mathematical
summary of the bits that comprise the frame in the trailer. Error detection is added at the data link layer because
the signals on the media could be subject to interference, distortion, or loss that would substantially change
the bit values that those signals represent.

A transmitting node creates a logical summary of the contents of the frame, known as the cyclic redundancy check (CRC) value.
This value is placed in the Frame Check Sequence (FCS) field to represent the contents of the frame. In the Ethernet
trailer, the FCS provides a method for the receiving node to determine whether the frame experienced transmission
errors.

### Layer 2 Address
The data link layer provides addressing that is used in transporting a frame across a shared local media. Device
addresses at this layer are referred to as physical addresses. Data link layer addressing is contained within
the frame header and specefies the frame destination node on the local network. The frame header may also
contain the source address of the frame.

The physical address is unique to the specific device. If the device is moved to another network or subnet,
it will still function with the same Layer 2 physical address.

Each data link frame contains the source data link address of the NIC card sending the frame, and the destination
data link address of the NIC card receiving the frame.

An address that is device-specific and non-hierarchical cannot be used to locate a device on large networks or the internet.
This would be like trying to find a single house within the entire world, with nothing more than a house number
and street name. The physical address however, can be used to locate a device within a limited area. For this reason,
the data link layer address is only used for local delivery. Addresses at this layer have no meaning beyond
the local network. Compare this to Layer 3, where addresses in the packet header are carried from the source
host to the destination host, regardless of the number of network hops along the route.

If the data must pass onto another network segment, an intermediate device, such as a router, is necessary.
The router must accept the frame based on the physical address and de-encapsulate the frame in order to examine
the hierarchical address, or IP address. Using the IP address, the router is able to determine the network location
of the destination device and the best path to reach it. When it knows where to forward the packet, the router
then creates a new frame for the packet, and the new frame is sent on to the next network segment toward its
final destination.

### LAN and WAN Frames
In a TCP/IP network, all OSI Layer 2 protocols work with IP at OSI Layer 3. However, the Layer 2 protocol used depends
on the logical topology and the physical media.

Each protocol performs media access control for specified Layer 2 logical topologies. This means that a number of
different network devices can act as nodes that operate at the data link layer when implementing these protocols.
These devices include the NICs on computers as well as the interfaces on routers and Layer 2 switches.

The Layer 2 protocol used for a particular network topology is determined by the technology used to implement
that topology. The techonology is, in turn, determined by the size of the network - in terms of the number of
hosts and the geographic scope - and the services to be provided over the network.

A LAN typically uses a high bandwidth technology that is capable of supporting large numbers of hosts. A LAN's
relatively small geographic area (a single building or a multi-building campus) and its high density of users,
make this technology cost-effective.

However, using a high bandwidth technology is usually not cost-effective for WANs that cover large geographic
areas (cities or multiple cities, for example). The cost of the long distance physical links physical links
and the technology used to carry the signals over those distances typically results in lower bandiwdth capacity.

The difference in bandwidth normally results in the use of different protocols for LANs and WANs.

Data link layer protocols include:
- Ethernet
- 802.11 Wireless
- Point-to-Point Protocol (PPP)
- HDLC
- Frame Relay

## Chapter 5: Ethernet
### Ethernet Encapsulation
Ethernet operates in the data link layer and the physical layer. It is a family of networking technologies that
are defined in the IEEE 802.2 and 802.3 standards. Ethernet supports data bandwidths of:
- 10 Mb/s
- 100 Mb/s
- 1000 Mb/s (1 Gb/s)
- 10,000 Mb/s (10 Gb/s)
- 40,000 Mb/s (40 Gb/s)
- 100,000 Mb/s (100 Gb/s)

Ethernet standards define both the Layer 2 protocols and the Layer 1 technologies. For the Layer 2 protocols, as
with all 802 IEEE standards, Ethernet relies on the two separate sublayers of the data link layer to operate, the Logical
Link Control (LLC) and the MAC sublayers.

#### LLC sublayer
The Ethernet LLC sublayer handles the communication between the upper layers and the lower layers. This is typically
between the networking software and the device hardware. The LLC sublayer takes the network protocol data, which is
typically an IPv4 packet, and adds control information to help deliver the packet to the destination node. The
LLC is used to communicate with the upper layers of the application, and transition the packet to the lower
layers for delivery.

LLC is implemented in software, and its implementation is independent of the hardware. In a computer, the LLC can
be considered the driver software for the NIC. The NIC driver is a program that interacts directly with the
hardware on the NIC to pass the data between the MAC sublayer and the physical media.

#### MAC sublayer
MAC constitutes the lower sublayer of the data link layer. MAC is implemented by hardware, typically in the
computer NIC. The specifics are listed in the IEEE 802.3 standards.

### MAC Sublayer
The Ethernet MAC sublayer has two primary responsibilities:
- Data encapsulation
- Media access control

#### Data encapsulation
Data encapsulation provides three primary functions:
- **Frame delimiting -** The framing process provides important delimiters that are used to identify a group
of bits that make up a frame. These delimiting bits provide synchronization between the transmitting and receiving
nodes
- **Addressing -** The encapsulation process contains the Layer 3 PDU and also provides for data link layer addressing
- **Error detection -** Each frame contains a trailer used to detect any errors in transmissions

The use of frames aids in the transmission of its as they are placed on the media and in the grouping of bits 
at the receiving node.

#### Media Access Control
The second responsibility of the MAC sublayer is media access control. Media access control is responsible
for the placement of frames on the media and the removal fo frames from the media. As its name implies, it controls
access to the media. This sublayer communicates directly with the physical layer.

Ethernet is a contention-based mtethod of networking. A contention-based method means that any device can try
to transmit data across the shared medium whenever it has data to send. The Carrier Sense Multiple Access/Collision
Detection (CSMA/CD) process is used in half-duplex Ethernet LANs to detect and resolve collisions. Today's
Ethernet LANs use full-duplex switches, which allow multiple devices to send and receive simultaneously with no 
collisions.

### Ethernet Evolution
Since the creation fo Ethernet in 1973, standards have evolved for specifying faster and more flexible versions
of the technology. This ability for Ethernet to improve over time is one of the main reasons it has become
so popular.

At the data link layer, the frame structure is nearly identical for all speeds of Ethernet. The Ethernet frame
structure adds headers and trailers around the Layer 3 PDU to encapsuate the message being sent.

Ethernet II is the Ethernet frame format used in TCP/IP networks.


### Ethernet Frame Fields
The minimum Ethernet frame size is 64 bytes and the maximum is 1518 bytes. This includes all bytes from the 
Destination MAC Address field through the Frame Check Sequence (FCS) field. The Preamble field is not included when
describing the size of a frame.

Any frame less tha n64 bytes in length is considered a "collision fragment" or "runt frame" and is automatically
discarded by receiving stations. Frames with more than 1500 bytes of data are considered "jumbo" or "baby giant
frames".

If the size of a transmitted frame is less tha nthe minimum or grater tha nthe maximum, the receiving device drops
the frame. Dropped frames are likely to be the result of collisions or other unwatned signals and are therefore
considered invalid.

#### Ethernet II Frame Structure and Field Size
8 bytes | 6 bytes | 6 bytes | 2 bytes | 46 to 1500 bytes | 4 bytes
--- | --- | --- | --- | --- | ---
Preamble | Destination MAC Address | Source MAC Address | EtherType | Data | FCS

- **Preamble (7 bytes) and Start Frame Delimiter Fields (SFD - 1 byte) -** Used for synchronization between the
sending and receiving devices. These first eight bytes of the frame are used to get the attention of the receiving
nodes. Esentially, the first few bytes tell the receivers to get ready to receive a new frame
- **Destination MAC Address Field (6 bytes) -** Identifies the intended recipient. This address is used by Layer 2
to assits devices in determining if a frame is addressed to them. The address in the frame is compared to the MAC
address in the device. If there is a match, the device accepts the frame. Can be unicast, multicast or broadcast
address
- **Source MAC Address Field (6 bytes) -** Identifies the frame's originating NIC or interface. Must be a unicast
address
- **EtherType Field (2 bytes) -** Identifies the upper layer protocol encapsulated in the Ethernet Frame. Common
values are, in hexadecimal, 0x800 for IPv4, 0x86DD for IPv6 and 0x806 for ARP
- **Data (46 - 1500 bytes) -** Contains the encapsulated data from a higher layer, which is a generic Layer 3 PDU,
or more commonly, an IPv4 packet. All frames must be at least 64 bytes long. If a small packet is encapsulated,
additional bits called a pad are used to increase the size of the frame to this minimum size
- **Frame Check Sequence Field (4 bytes) -** Used to detect errors in a frame. It uses a cyclic redundancy check
(CRC). The sending device includes the results of a CRC in the FCS field of the frame. The receiving device receives
the frame and generates a CRC to look errors. If the calculations match, no error occurred. Calculations that do
not match are an indication that the data has changed; therefore, the frame is dropped. A change in the data be
the result of a disruption of the electrical signals that represent the bits

### MAC Address and Hexadecimal
An Ethernet MAC address is a 48-bit binary value expressed as 12 hexadecimal digits (4 bits per hexadecimal digit).

Hexadecimal is used to represent Ethernet MAC addresses and IP version 6 addresses.

### MAC Address: Ethernet Identity
In Ethernet, every network device is connected to the same shared media. Ethernet was once predominantly a half-duplex
topology using a multi-access bus or later Ethernet hubs. This meant that all nodes would receive every frame
transmitted. To prevent the excessive overhead involved in the processing of every frame, MAC addresses were
created to identify the actual source and destination. MAC addressing provides a method for device identification
at the lower level of the OSI model. Although Ethernet has now transitioned to full-duplex NICs and switches,
it is still possible that a device that is not the intended destination will receive an Ethernet frame.

#### MAC Address Structure
The MAC address value is a direct result of IEEE-enforced rules for vendors to ensure globally unique addresses
for each Ethernet device. The rules established by IEEE require any vendor that sells Ethernet devices to
register with IEEE. The IEEE assigns the vendor a 3-byte (24-bit) code called the Organizationally Unique 
Identifier (OUI).

IEEE requires a vendor to follow to simple rules, as shown in the figure:
- All MAC addresses assigned to a NIC or other Ethernet device must use that vendor's assigned OUI as the first
3 bytes
- All MAC addresses with the same OUI must be assigned a unique value in the last 3 bytes

**Note:** It is possible for duplicate MAC addresses to exist due to mistakes during manufacturing or in some 
virtual machine implementation methods. In either case, it will be necessary to modify the MAC address with a 
new NIC or in software.

### Frame Processing
The MAC address is often referred to as a burned-in address (BIA) because, historically, this address is burned 
into ROM (Read-Only Memory) on the NIC. This means that the address is encoded into the ROM chip permanently.

**Note:** On modern PC operating systems and NICs, it is possible to change the MAC address in software. This is
useful whe nattempting to gain access to a network that filters based on BIA. Consequently, filtering or controlling
traffic based on the MAC address is no longer as secure.

When teh computer starts up, the first thing the NIC does is copy the MAC address from ROM into RAM. When a device
is forwarding a message to an Ethernet network, it attaches header information to the frame. The header
information contains the source and destination MAC address.

When a NIC receives an Ethernet frame, it examines the destination MAC address to see if it matches the device's
physical MAC address stored in RAM. If there is no match, the device discards the frame. If there is a match,
it passes the frame up the OSI layers, where the de-encapsulation process takes place.

**Note:** Ethernet NICs will also accept frames if the destination MAC address is a broadcast or a multicast
group of which the host is a member.

Any device that can be the source or destination of an Ethernet frame must be assigned a MAC address. This
includes workstations, servers, printers, mobile devices, and routers.

### Mac Address Representations
Dependeing on the device and the operating system, you will see various representations of MAC addresses. Cisco
routers and switches use the form XXXX.XXXX.XXXX where X is a hexadecimal character.

### Unicast MAC Address
In Ethernet, different MAC addresses are used for Layer 2 unicast, broadcast, and multicast communications.

An unicast MAC address is the unique address used when a frame is sent from a single transmitting device
to a single destination device.

For a unicast packet to be sent and received, a destination IP address must be in the IP packet header. A 
corresponding destination MAC address must also be present in the Ethernet frame header. The IP address and MAC
address combine to deliver data to one specific destination host.

The process that a source host uses to determine the destination MAC address is known as Address Resolution Protocol (ARP).

Although the destination MAC address can be a unicast, broadcast, or multicast address, the source MAC address 
must always be a unicast.

### Broadcast MAC Address
A broadcast packet contains a destination IPv4 address that has all ones (1s) in the host portion. This numbering
in the address means that all hosts on that local network (broadcast domain) will receive and process the packet.
Many network protocols, such as DHCP and ARP, use broadcasts.

The source host sends an IPv4 broadcast packet to all devices on its network. The IPv4 destination address is a
broadcast address. When the IPv4 broadcast packet is encapsulated in the Ethernet frame ,the destination MAC
address is the broadcast MAC address of FF-FF-FF-FF-FF-FF in hexadecimal (48 ones in binary).

### Multicast MAC Address
Multicast addresses allow a source device to send a packet to a group of devices. Devices that belong to a 
multicast group are assigned a multicast group IP address. The range of IPv4 multicast addresses is 224.0.0.0 to
239.255.255.255. The range of IPv6 multicast addresses begin with FF00::/8. Because multicast addresses represent
a group of addresses (sometimes called a host group), they can on ly be used as the destination of a packet.
The source will always be a unicast address.

Multicast addresses would be used in remote gaming, where many players are connected remotely ut playing the same
game. Another use of multicast addresses is in distance learning through video conferencing, where many students
are connected to the same class.

The multicast MAC address associated with an IPv4 multicast address is a special value that begins with 01-00-5E in
hexadecimal. The reamining portion of the multicast MAC address is created by converting the lower 23 bits of
the IP multicast group address into 6 hexadecimal characters. For an IPv6 address, the multicast MAC address begins
with 33-33.

### Switch Fundamentals
A Layer 2 Ethernet switch uses MAC addresses to make forwarding decisions. It is completely unaware of the protocol
being carried in the data portion of the frame, such as an IPv4 packet. The switch makes its forwarding decisions
based only on the Layer 2 Ethernet MAC addresses.

An Ethernet switch consults a MAC address table to make a forwarding decision for each frame.

**Note:** The MAC address table is sometimes referred to as a content addressable memory (CAM) table. While the
term CAM table is fairly common, for the purposes of this course, we will refer to it as a MAC address table.

### Learning MAC Addresses
The switch dynamically builds the MAC address table by examining the soure MAC address of the frames received
on a port. The switch forwards frames by searching for a match between the destination MAC address in the frame
and an entry in the MAC address table.

- If the source MAC address does not exist, it is added to the table along with the incoming port number
- If the source MAC address does exist, the switch updates the refresh timer for that entry. By default, most
Ethernet switches keep an entry in the table for 5 minutes

  **Note:** If the source MAC address does exist in the table but on a different port, the switch treats this as
  a new entry. The entry is replaced using the same MAC address but with the more current port number.

If the destination MAC address is a unicast address, the switch will look for a match between the destination
MAC address of the frame and an entry in its MAC address table.

- If the destination MAC address is in the table, it will forward the frame out the specified port
- If the destination MAC address is not in the table, the switch will forward the frame out all ports except the
incoming port. This is known as a unknown unicast

  **Note:** If the destination MAC address is a broadcast or a multicast, the frame is also flooded out all ports
  except the incoming port.

### Filtering Frames
As a switch receives frames from different devices, it is able to populate its MAC address table by examining the
source MAC address of every frame. When the switch's MAC address table contains the destination MAC address,
it is able to filter the frame and forward out a single port.

#### MAC Address Tables on Connected Switches
A switch can have multiple MAC addresses associated with a single port. This is common when the switch is connected
to another switch. The switch will have a separate MAC address table entry for each frame received with a different
source MAC address.

#### Sending a Frame to the Default Gateway
When a device has an IP address that is on a remote network, the Ethernet frame cannot be sent directly to the destination
device. Instead, the Ethernet frame is sent to the MAC address of the default gateway, the router.

### Frame Forwarding Methods on Cisco Switches
Switches use one of the following forwarding methods for switching data between network ports:
- **Store-and-forward switching:** A store-and-forward switch receives the entire frame and computes the CRC.
If the CRC is valid, the switch looks up the destination address, which determines the outgoing interface. The
frame is then forwarded out the correct port
- **Cut-through switching:** A cut-through switch forwards the frame before it is enterely received. At a minimum,
the destination address of the frame must be read before the frame can be forwarded

CRC uses a mathematical formula, based on the number of bits (1s) in the frame, to determine whether the received
frame has an error. After confirming the integrity of the frame, the frame is forwarded out the appropiriate port,
toward its destination. When an error is detected in a frame, the switch discards the frame. Discarding frames
with errors reduces the amount of bandwidth consumed by corrupt data. Store-and-forward switching is required for
Quaility of Service (QoS) analysis on converged networks where frame classification for traffic priorization is
necessary. For example, voice over IP data streams need to have priority over web-browsing traffic.

### Cut-Through Switching
In cut-through switching, the switch acts upon the data as soon as it is received, even if the transmission is
not complete. The switch buffers just enough of the frame to read the destination MAC address so that it can 
determine to which port to forward the data. The switch does not perform any error checking on the frame.

There are two variants of cut-through switching:
- **Fast-forward switching:** Offers the lowest level of latency. It immediately forwards a packet after reading
the destination address. Latency is measured from the first bit received to the first bit transmitted. It's the
typical cut-through method of switching
- **Fragment-free switching:** The switch stores the first 64 bytes of the frame before forwarding. The reason 
of it is that most network errors and collisions occur during the first 64 bytes. This variant tries to enhance
fast-forward switching by performing a small error check on the first 64 bytes of the frame to ensure
that a collision has not occurred before forwarding the frame

Some switches are configured to perform cut-through switching on a per-port basis until a user-defined error
threshold is reached, and then they automatically change to store-and-forward. When the error rate fails below
the threshold, the port automatically changes back to cut-through switching.

### Memory Buffering on Switches
An Ethernet switch may use a buffering technique to store frames before forwarding them. Buffering may also be 
used when the destination port is busy due to congestion and the switch stores the frame until it can be transmitted.

#### Port-based Memory Buffering
Frames are stored in queues that are linked to specific incoming and outgoing ports. A frame is transmitted to the
outgoing port only when all the frames ahead of it in the queue have been successfully trnasmitted. It is 
possible for a single frame to delay the transmission of all the frames in memory because of a busy destination
port. This delay occurs even if the other frames could be transmitted to open destination ports.

#### Shared Memory Buffering
Deposits all frames into a common memory buffer that all the ports on the switch share. The amount of buffer 
memory required by a port is dynamically allocated. The frames in the buffer are linked dynamically to the 
destination port. This allows the packet to be received on one port and then transmitted on another port,
without moving it to a differnet queue.

The switch keeps a map of frame to port links showing where a packet needs to be transmitted. The map link is
cleared after the frame has been succesfully transmitted. The number of frames stored in the buffer is restricted 
by the size of the entire memory buffer and not limited to a single port buffer. This permits larger frames
to be transmitted with fewer dropped frames. This is especially important to asymmetric switching. Asymmetric
switching allows for different data rates on different ports. This allows more bandwidth to be dedicated to 
certain ports, such as a port connected to a server.

### Duplex and Speed Settings
Therea re two types of duplex settings used for communications on an Ethernet network:
- **Full-duplex:** Both ends on the connection can send and receive simultaneously
- **Half-duplex:** Only one end of the connection can send at a time

Autonegotiation is an optional function found on most Ethernet switches and NICs. Autonegotiation enables two 
devices to automatically exchange information about speed and duplex capabilities. The switch and the connected
device will choose the highest performance mode. Full-duplex is chosen if both devices have the capability
along with their highest common bandwidth.

**Note:** Most Cisco switches and Ethernet NICs default to autonegotiation for speed and duplex. Gigabit Ethernet
ports only operate in full-duplex.

#### Duplex Mismatch
One of the most comon causes of performance issues on 10/100 Mb/s Ethernet links occurs when one port on the
link operates at half-duplex while th eother port operates at full-duplex. This occurs when one or both ports
on a link are reset, and the autonegotiation process does not result in both link partners having the same 
configuration. It also can occur when users reconfigure one side of a link and forget to reconfigure the other.
Both sides of a link should have autonegotiation on, or both sides should have it off.

### Auto-MDIX
In addition to having the correct duplex setting, it is also necessary to have the correct cable type defined 
for each port. Connections between specific devices, such as switch-to-switch, switch-to-router, switch-to-host,
and router-to-host devices, once required the use fo specific cable types (crossover or straight-through).
Most switch devices now support the mdix auto interface configuration command in the CLI to enable the automatic
medium-dependent interface crossover (auto-MDIX) feature.

When the auto-MDIX feature is enabled, the switch detects the type of cable attached to the port, and configures
the interfaces accordingly. Therefore, you can use either a crossover or a straight-throught cable for connections
to a copper 10/100/1000 port on the switch, regardless of the type of device on the other end of the connection.

**Note:** The auto-MDIX feature is enabled by default on switches running Cisco IOS Release 12.2(18)SE or later.

### Destination on Same Network
There are two primary addresses assigned to a device on an Ethernet LAN:
- **Physical address (the MAC address) -** Used for Ethernet NIC to Ethernet NIC communications on the same network
- **Logical address (the IP address) -** Used to send the packet from the original source to the final destination

IP addresses are used to identify the address of the original source and the final destination. The destination
IP address may be on the same IP network as the source or may be on a remote network.

**Note:** Most applications use DNS (Domain Name System) to determine the IP address when given a domain name
such as www.cisco.com. DNS is discussed in a later chapter.

Layer 2 or physical addresses, like Ethernet MAC addresses, have a different purpose. These addresses are used
to deliver the data link frame with the encapsulated IP packet from one NIC to another NIC on the same network.
If the destination IP address is on the same network, the destination MAC address will be that of the destination 
device.

### Destination Remote Network
When the destination IP address is on a remote network, the destination MAC address will be the address
of the host's default gateway, the router's NIC.

Routers examine the destination IPv4 address to determine the best path to forward the IPv4 packet. This is
similar to how the postal service forwards mail based on the address of the recipient.

When the router receives the Ethernet frame, it de-encapsulates the Layer 2 information. Using the destination
IP address, it determines the next-hop device, and then encapsulates the IP packet in a new data link frame
for the outgoing interface. Along each link in a path, an IP packet is encapsulated in a frame specific
to the particular data link technology associated with that link, such as Ethernet. If the next-hop device is 
the final destination, the destination MAC address will be that of the device's Ethernet NIC.

### Introduction to ARP
To determine the destination MAC address, the device uses ARP. ARP provides two basic functions:
- Resolving IPv4 addresses to MAC addresses
- Maintaining a table of mappings

### ARP Functions
#### Resolving IPv4 Addresses to MAC Addresses
When a packet is sent to the data link layer to be encapsulated into an Ethernet frame, the device refers
to a table in its memory to find the MAC address that is mapped to the IPv4 address. This talbe is called the 
ARP table or the ARP cache. The ARP table is stored in the RAM of the device.

The sending device will search its ARP table for a destination IPv4 address and a corresponding MAC address.
- If the packet's destination IPv4 address is on the same network as the source IPv4 address, the device will
search the ARP table for the destination IPv4 address
- If the destination IPv4 address is on a different network than the source IPv4 address, the device will search
the ARP table for the IPv4 address of the default gateway

In both cases, the serach is for an IPv4 address and a corresponding MAC address for the device.

Each entry, or row, of the ARP table binds an IPv4 address with a MAC address. We call the relationship between
the two values a map - it simply means that you can locate an IPv4 address in the table and discover the 
corresponding MAC address. The ARP table temporarily saves (caches) the mapping for the devices on the LAN.

If the device locates the IPv4 address, its coresponding MAC address is used as the destination MAC address 
in the frame. If there is no entry is found, then the device sends an ARP request.

### ARP Request

ARP messages are encapsulated directly within an Ethernet frame. There is no IPv4 header. The ARP request
message includes:
- **Target IPv4 address -** This is the IPv4 address that required a corresponding MAC address
- **Target MAC address -** This is the unknown MAC address and will be empty in the ARP request message

The ARP request is encapsulated in an Ethernet frame using the following header information:
- **Destination MAC address -** This is a broadcast address requiring all Ethernet NICs on the LAN to accept
and process the ARP request
- **Source MAC address -** This is the sender of the ARP request's MAC address
- **Type -** ARP messages have a type field of 0x806. This informs the receiving NIC that the data portion of
the frame needs to be passed to the ARP process

Because ARP requests are broadcasts, they are flooded out all ports by the switch except the receiving port. All
Ethernet NICs on the LAN process broadacsts. Every device must process the ARP request to see if the target IPv4
address matches its own. A router will not forward broadcasts out other interfaces.

Only one device on the LAN will have an IPv4 address that matche sthe target IPv4 address in the ARP request.
All other devices will not reply.

### ARP Reply
The ARP reply message includes:
- **Sender's IPv4 address -** This is the IPv4 address of the sender, the device whose MAC address was requested
- **Sender's MAC address -** This is the MAC address of the sender, the MAC address needed by the sender of the
ARP request

The ARP reply is encapsulated in an Ethernet frame using th efollowing header information:
- **Destination MAC address -** This is the MAC address of the sender of the ARP request
- **Source MAC address -** This is the sender of the ARP reply's MAC address
- **Type -** ARP messages have a type field of 0x806. This informs the receiving NIC that the data portion
of the frame needs to be passed to the ARP process

Only the device that originally sent the ARP request will receive the unicast ARP reply. Once the ARP reply is
received, the device will add the IPv4 address and the corresponding MAC address to its ARP table. Packets
destined for that IPv4 address can now be encapsulated in frames using its corresponding MAC address.

If no device responds to the ARP request, the packet is dropped because a frame cannot be created.

Entries in the ARP table are time stamped. If a device does not receive a frame from a particular device by
the time the timestamp expires, the entry for this device is removed from the ARP table.

Additionally, static map entries can be entered in an ARP table, but this is rarely done. Static ARP table
entries do no expire over time and must be manually removed.

**Note:** IPv6 uses a similar process to ARP for IPv4, known as ICMPv6 neighbor discovery. IPv6 uses neighbor
solicitation and neighbor advertisement messages, similar to IPv4 ARP requests and ARP replies.

### ARP Role in Remote Communication
When the desitnation IPv4 address is not on the same network as the source IPv4 address, the source device
needs to send the frame to its default gateway. This is the interface of the local router. Whenever a source
device has a packet with an IPv4 address on another network, it will encapsulate that packet in a frame using
the destination MAC address of the router.

The IPv4 address of the default gateway address is stored in the IPv4 configuration of the hosts. When a host
creates a packet for a destination, it compares the destination IPv4 address and its own IPv4 address to 
determine if the two IPv4 addresses are located on the same Layer 3 network. If th edestination host is not on its same
network, the source checks its ARP table for an entry with the IPv4 address of the default gateway. If there
is not an entry, it uses the ARP process to determine a MAC address of the default gateway.

## Chapter 6: Network Layer
### The Network Layer
The network layer, or OSI Layer 3, provides services to allow end devices to exchange data across the network.
To accomplish this end-to-end transport, the network layer uses four basic processes:
- **Addressing end devices -** End devices must be configured with a unique IP address for identification on
the network
- **Encapsulation -** The encapsulation process adds IP header information, such as the IP address of
the source (sending) and destination (receiving) hosts
- **Routing -** To travel to other networks, the packet must be processed by a router. The role of the router is
to select the best path and direct packets toward the destination host in a process known as routing. A packet
may cross many intermediary devices before reaching the destination host. Each router a packet crosses to reach 
the destination host is called a hop
- **De-encapsulation -** If the destnation IP address within the header matches its  own IP address, the IP header
is removed from t epacket. After the packet is de-encapsulated by the network layer, the resulting Layer 4 PDU 
is passed up to the appropiate service at the transport layer

Network layer protocols specify the packet structure and processing used to carry the data from one host to another
host. Operating without regard to the data carried in each packet allows the network layer to carry packets for
multiple types of communications between multiple hosts.

### Encapsulating IP
IP Encapsulates the transport layer segment or other data by adding an IP header. This header is used to deliver
the packet to the destination host. The IP header remains the same from the time the packet leaves the source host
until it arrives at the destination host.

The process of encapsulating data layer by layer enables the services at the different layers to develop and
scale without affecting the other layers. This means the transport layer segments can be readily packaged by
IPv4 or IPv6 or by any new protocol that might be developed in the future.

Routers can implement these different network layer protocols to operate concurrently over a network. The routing
performed by these intermediate devices only considers the contents of the network layer packet header. In all
cases, the data portion of the packet, that is, the encapsulated transport layer PDU, remains unchanged
during the network layer processes.

### Characteristics of IP
IP was designed as a protocol with low overhead. It provides only the functions htat are necessary to deliver
a packet from a source to a destination over an interconnected system of networks. The protocol was not designed
to track and manage the flow of packets. These functions, if required, are performed by other protocols at
other layers, primarily TCP at Layer 4.

Best characteristics of IP:
- **Connectionless -** No connection with the destination is established before sending data packets
- **Best Effort -** IP is inherently unreliable because packet delivery is not guaranteed
- **Media Independent -** Operation is independent of the medium (i.e., cooper, fiber optic, or wireless)
carrying the data

### IP - Connectionless
IP is connectionless, meaning that no dedicated end-to-end connection is created before data is sent. It's
conceptually similar to sending a letter to someone without notifying the recipient in advance.

This process greatly reduces the overhead of IP. However, with no pre-established end-to-end connection, senders
are unaware whether destination devices are present and functional when sending packets, nor are they aware
if the destination receives the packet, or if they are able to access and read the packet.

### IP - Best Effort Delivery
The IP protocol does not guarantee that all packets that are delivered are, in fact, received.

Unreliable means that IP does not have the capability to manage and recover from undelivered or corrupt packets.
This is becaues while IP packets are sent with information about the location of delivery, they contain no information
that can be processed to inform the sender whether the delivery was successful. Packets may arrive at the
destination corrupted, out of sequence, or not at all. IP provides no capability for packet retransmissions if
errors occur.

If out-of-order packets are delivered, or packets are missing, then applications using the data, or upper layer
services, must resolve these issues. This allows IP to function very efficiently. In the TCP/IP protocol suite,
reliability is the role of the transport layer.

### IP - Media Independent
IP operates independently of th emedia that carry the data at lower layers of the protocol stack.

It is the responsibility of the OSI data link layer to taken an IP packet and preapre it for transmission over 
the communications medium. This means that the transport of IP packets is not limited to any particular medium.

There is, however, one major characteristic of the media that the network layer considers: the maximum size
of the PDU that each medium can transport. This characteristic is referred to as the maximum transmission unit
(MTU). Part of the control communication between the data link layer and the network layer is the establishment 
of a maximum size for the packet. The data link layer passes the MTU value up to the network layer. The network
layer then determines how large packets can be.

In some cases, an intermedate device, usually a router, must split up a packet when forwarding it from one medium
to another medium with a smaller MTU. This process is called fragmenting the packet or fragmentation.

### IPv4 Packet Header
An IPv4 packet header consists of fields containing important information about the packet. These fields contain 
binary numbers which are examined by the Layer 3 process. The binary values of each field identify various
settings of the IP packet.

Significant fields in the IPv4 header include:
- **Version -** Contains a 4-bit binary value set to 0100 that identifies this as an IP version 4 packet
- **Differentiated Services or DiffServ (DS) -** Formerly called the Type of Service (ToS) field, the DS field is
an 8-bit field uses to determine the priority of each packet. The six most significant bits of the DiffServ
field is the Differentiated Services Code Point (DSCP) and the last two bits are the Explicit Congestion Notification
(ECN) bits
- **Time-to-Live (TTL) -** Contains an 8-bit binary value that is used to limit the lifetime of a packet. The
packet sender sets the initial TTL value, and it is decreased by one each time the packet is processed by a 
router. If the TTl field decrements to zero, the router discards the packet and sends an Internet Control Message
Protocol (CMP) Time Exceeded message tothe source IP address
- **Protocol -** Field is used to identify the next level protocol. This 8-bit binary value indicates the data 
payload type that the packet is carrying, which enables the network layer to pass the data to the appropriate 
upper-layer protocol. Common values include ICMP (1), TCP (6) and UDP (17)
- **Source IPv4 Address -** Contains a 32-bit binary value that represents the source IPv4 address of the packet.
The source IPv4 address is always a unicast address
- **Destination IPv4 Address -** Contains a 32-bit binary value that represents the destination IPv4 address of
the packet. The destination IPv4 address is a unicast, multicast, or broadcast address

The twomost commonly referenced fields are the source and destination IP addresses. These fields identify where
the packet is coming from and where it is going. Typically these addresses do not change while travelling from
the source to the destination.

### Limitations of IPv4
Throught the years, IPv4 has been updated to address new challenges. However, even with changes, IPv4 still has
three major issues:
- **IP address depletion -** IPv4 has a limited number of unique public IPv4 addresses available.  Although there
are approximately 4 billion IPv4 addresses, the increasing number of new IP-enabled devices, always-on connections,
and the potential growth of less-developed regions have increased the need for more addresses
- **Internet routing table expansion -** A routing table is used by routers to make best path determinations. As
the number of servers connected to the Internet increases, so too does the number of network routes. These IPv4
routes consume a great deal of memory and processor resources on Internet routers
- **Lack of end-to-end connectivity -** Network Address Translation (NAT) is a technology commonly implemented 
within IPv4 networks. NAT provides a way for multiple devices to share a single public IPv4 address. However,
because the public IPv4 address is shared, the IPv4 address of an internal network host is hidden. This can
be problematic for technologies that require end-to-end connectivity

### Introducing IPv6
IPv6 overcomes the limiations of IPv4 and is a powerful enhancement with features that better suit current and
foreseeable network demands.

Improvements that IPv6 provides include:
- **Increased address space -** IPv6 addresses are based on 128-bit hierarchical addressing as opposed to IPv4 
with 32 bits
- **Improved packet handling -** The IPv6 header has been simplified with fewer fields
- **Eliminates the need for NAT -** With such a large number of public IPv6 addresses, NAT between a private IPv4
address and a public IPv4 is not needed. This avoids some of the NAT-induced application problems experienced 
by applications requiring end-to-end connectivity

The 32-bit IPv4 address space provides approximately 4,294,967296 unique addresses. IPv6 address space provides
340,282,366,920,938,463,463,374,607,431,768,211,456 or 340 undecillion addresses, which is roughly equivalent to
every grain of sand on Earth

### Encapsulating IPv6
One of the major design improvements of IPv6 over IPv4 is the simplified IPv6 header.

For instance, the IPv4 header consists of 20 octets (up to 60 bytes if the Options field is used) and 12 basic
header fields, not including the Options field and Padding field. As highlighted in the figure, for IPv6, some
fields have remained the same, some fields have changed names and positions, and some IPv4 fields are no longer
required.

In contrast, the simplified IPv6 header consists of 40 octets (largely due to the length of the source and
destination IPv6 addresses) and 8 header fields (3 IPv4 basic header fields and 5 additional header fields).
Some fields have kept the same names as IPv4, some fields have changed names or positions, and a new field
has been added.

The IPv6 simplified header offers several advantages over IPv4:
- Simplified header format for efficient packet handling
- Larger payload for increased throughput and transport efficiency
- Hierarchical network architecture for routing efficency
- Autoconfiguration for addresses
- Elimination of need for network address translation (NAT) between private and public addresses

### IPv6 Packet Header
The fields in the IPv6 packet header include:
- **Version -** This field contains a 4-bit binary value set to 0110 that identifies this as an IP version 6
packet
- **Traffic Class -** This 8-bit field is equivalent to the IPv4 Differentiated Services (DS) field
- **Flow Label -** This 20-bit field suggests that all packets with the same flow label receive the same type
of handling by routers
- **Payload Length -** This 16-bit field indicates the length of the data portion or payload of the IPv6 packet
- **Next Header -** This 8-bit field is equivalent to the IPv4 Protocol field. It indicates the data payload 
type that the packet is carrying, enabling the network layer to pass the data to the appropriate upper-layer 
protocol
- **Hop Limit -** This 8-bit field replaces teh IPv4 TTL field. This value is decremented by a value of 1 by
each router that forwards the packet. When the counter reaches 0, the packet is discarded, and an ICMPv6 Time 
Exceeded message is forwarded to the sending host, indicating that the packet did not reach its destination 
because the hop limit was exceeded
- **Source IPv6 Address -** This 128-bit field identifies the IPv6 address of the sending host
- **Destination IPv6 Address -** This 128-bit field identifies the IPv6 address of the receiving host

An IPv6 packet may also contain extension headers (EH), which provide optional network layer information. 
Extension headers are optional and are placed between the IPv6 header and the payload. EHs are used for fragmentation, 
security, to support mobility and more.

Unlike IPv4, routers do not fragment routed IPv6 packets.

### Host Forwarding Decision
Another role of the network layer is to direct packets between hosts. A host can send a packet to:
- **Itself -** A host can ping itself by sending a packet to a special IPv4 address of 127.0.0.1, which is
referred to as the loopback interface. Pinging the loopback interface tests the TCP/IP protocol stack on the 
host
- **Local host -** This is a host on the same local network as the sending host. The hosts share the same
network address
- **Remote host -** This is a host on a remote network. The hosts do not share the same network address

Whether a packet is deestined for a local host or a remote host is determined by the IPv4 address and subnet mask
combination of the source (or sending) device compared to the IPv4 address and subnet mask of the destination
device.

In a home or business network, you may have several wired an dwireless devices interconnected together using an
intermediate device, such as a LAN switch and/or a wireless access point (WAP). This intermediate device
provides interconnections between local hosts on the local network. Local hosts can reach each other and share
information without the need for any additional devices. If a host is sending a packet to a device that is 
configured with the same IP network as the host device, the packet is simply forwarded out of the host interface,
through the intermediate device, and to the destination device directly.

When a source device sends a packet to a remote destination device, then the help of routers and routing is 
needed. Routing is the process of identifying the best path to a destination. The outer connected to the local
network segment is referred to as the default gateway.

### Default Gateway
The default gateway is the network device that can route traffic to other networks. It is the router that can 
route traffic out of the local network.

- Routes traffic to other networks
- Has a loca lIP address in the same address range as other hosts on the network
- Can take data in and forward data out

### Using the Default Gateway
A host's routing table will typically include a default gateway. The host receives the IPv4 address of the
default gateway either dynamically from Dynamic Host Configuration Protocol (DHCP) or configured
manually. Having a default gateway configured creates a default route in the routing table of the PC. A
default route is the route or pathway your computer will take when it tries to contact a remote network.

The default route is derived from the default gateway configuration and is placed in the host computer's routing
table.

### Host Routing Tables
The `route print` or `netstat -r` command can be used to display the host routing table. Both commands generate
the same output. The output may seem overhwelming at first, but is fairly simple to understand.

Displays three sections related to the current TCP/IP network connections:
- **Interface List -** Lists the Media Access Control (MAC) address and assigned interface number of every 
network-capable interface on the host, inclduing Ethernet, Wi-Fi, and Bluetooth adapters
- **IPv4 Route Table -** Lists all known IPv4 routes, including direct connections, local network, and local
default routes
- **IPv6 Route Table -** Lists all known IPv6 routes, including direct connections, local network, and local 
default routes

### Router Packet Forwarding Decision
When a host sends a packet to another host, it will use its routing table to determine where to send the packet.
If the destination host is on a remote network, the packet is forwarded to the default gateway.

The routing table of a router can store information about:
- **Directly-connected routes -** These routes come from the active router interfaces. Routers add a directly
connected route when an interface is configured with an IP address and is activated. Each of the router'
interfaces is connected to a different network segment
- **Remote routes -** These routes come from remote networks connected to ther routers. Route to these networks
can be manually configured on the local router by the network administrator or dynamically configured by
enabling the local router to exchange routing information with other routers using a dynamic routing protocol
- **Default route -** Like a host, routers also use a default route as a last resort if there is no other route
to the desired network in the routing table

### IPv4 Router Routing Table
On a Cisco IOS router, the `show ip route` command can be used to display the router's IPv4 routing table.

The routint table  also has information on how the route was learned, the trustworthiness and rating of the route,
when the route was updated, and which interface to use to reach the requested destination.

When a packet arrives at the router interface, the router examines the packet header to determine the destination
network. If the destination network matches a route in the routing table, the router forwards the packet using
the information specified in the routing table. If there are two or more possible routes to the same destination,
the metric is used to decide which route appears in the routing table.

### Directly Connected Routing Table Entries
When a router interface is configured with an IPv4 address, a subnet mask, and is activated, the following two 
routing table entires are automatically created:
- **C -** Identifies a directly-connected network. Directly-connected networks are automatically created when
an interface is configured with an IP address and activated
- **L -** Identifies that this is a local interface. This is the IPv4 address of the interface on the router

Entries:
- **Route Source -** Identifies how the network was learned by the router
- **Destination Network -** Identifies the destination network an dhow it was learned
- **Outgoing Interface -** Indentifies the exit interface to use to forward a packet toward the final destination

**Note:** Local interface entries did not apear in routing tables prior to IOS Release 15

### Remote Network Routing Table Entries
A router typically has multiple interfaces configured. The routing table stores information about both 
directly-connected networks and remote networks.

Entries:
- **Route Source -** Identifies how the network was learned by the router. Common router sources include 
**S** (static route), **D** (Enhanced Inferior Gateway Routing Protocol or EIGRP), and **O** (Open Shortest Path
First or OSPF)
- **Destination Network -** Identifies the destination network
- **Administrative Distance -** Identifies the administrative distance (i.e., trustworthiness) of the route source.
Lower values indicate increased trushworthiness of the route source
- **Metric -** Identifies the value assigned to reach the remote network. Lower values indicate preferred routes
- **Next-hop -** Identifies the IP address of the next router to forward the packet
- **Route Timestamp -** Identifies when the router was last heard from
- **Outgoing Interface -** Identifies the exit interface to use to forward a packet toward the final destination

### Next-Hop Address
When a packet destined for a remote network arrives at the router, the router matches the destination network
to a route in the routing table. If a match is found, the router forwards the packet to the next hop address out
of the identified interface.

Connected networks with a route source of C and L have no next-hop address. This is because a router can forward
packets directly to hosts on these networks using the designated interface.

It is also important to understand that packets cannot be forwarded by the router without a route for the 
destination network in the routing table. If a route representing the destination network is not in the routing
table, the packet is dropped (that is, not forwarded). However, just as a host can use a default gateway to
forward a packet to an unknown destination, a router can also include a default route to create a Gateway of
Last Resort. The deafult route could be manually configured or dynamically obtained.

### A Router is a Computer
There are many types of infrastructure routers available. In fact, Cisco routers are desgined to address the
needs of many different types of Business and networks:
- **Branch -** Teleworkers, small businesses, and medium-size branch sites. Includes Cisco Integrated Services 
Routers (ISR) G2 (2nd generation)
- **WAN -** Large businesses, organizations, and enterprises. Includes the Cisco Catalyst Series Switches and
the Cisco Aggregation Services Routers (ASR)
- **Service Provider -** Large service providers. Includes Cisco ASR, Cisco CRS-3 CArrier Routing System, and
7600 Series routers

Regardless of their function, size or complexity, all router models are essentially computers. Just like computers,
tablets, and smart devices, routers also require:
- Central processing units (CPU)
- Operating systems (OS)
- Memory consisting of random-access memory (RAM), read-only memory (ROM), nonvolatile random-access memory (NVRAM),
and flash

### Router CPU and OS
Like all computers, tablets, gaming consoles, and smart devices, Cisco devices rquire a CPU to execute OS
instructions, such as system initialization, routing functions, and switching functions.

The CPU requires an OS to provide routing and switching functions. The Cisco Internetwork Operating System (IOS)
is the system software used for most Cisco devices regardless of the size and type of the device. It is used for
routers, LAN, switches, small wireless access points, large routers with dozes of interfaces, and many other devices.

### Router Memory
A router has access to volatile or non-volatile memory storage. Volatile memory requires continual power to maintain
its information. When the router is powred down or restarted, the content is erased and lost. Non-volatile memory
retains its information even when a device is rebooted.

Specifically, a Cisco router uses four types of memory:
- **RAM -** This is volatile memory used in Cisco routers to store applications, processes, and data needed to
be executed by the CPU. Cisco routers use a fast type of RAM called synchronous dynamic random access memory
(SDRAM)
  - The IOS image and running configuration file uses RAM
  - The routing table used to detemrine the best path to use to forward packets
  - The ARP cache used to map IPv4 addresses to MAC addresses
  - The Packet buffer used to temporarily store packets before forwarding to the destination
- **ROM -** This non-volatile memory is used to store crucial operational instructions and limited IOS. Specifically,
it is firmware embedded on an integrated circuit inside the router which can only be altered by Cisco
  - Bootup information that provides the startup instructions
  - Power-on selft-test (POST) that tests all the hardware components
  - Limited IOS to provide a backup versoin of the IOS. It is used for loading a full feature IOS when it
  has been deleted or corrupted
- **NVRAM -** This non-volatile memory is used as the permanent storage for the startup configuration file (startup-config)
- **Flash -** This non-volatile computer memory used as permanent storage for the IOS and other system related
files such as log files, voice configuration files, HTML files, backup configurations, and more. When a router
is rebooted, the IOS is copied from flash into RAM.

### Inside a Router
Althought there are several differnet types and models of routers, every router has the same general hardware
components.
- Power Supply
- Shield for WAN interface card WIC or high-speed WIC (HWIC) x2
- Fan 
- Synchronous dynamic RAM (SDRAM) used for holding the running configuration and routing tables, and for suporting
package buffering
- Nonvolatile RAM (NVRAM) and boot flash memory used for storing the ROMMON boot code as well as NVRAM data
- CPU
- Advanced Integration Module (AIM) option that offloads processor-intensive functions such as encryption from
- the main CPU

### Connect to a Router
Cisco devices, routers, and switches typically interconnect many devices. For this reason, these devices have
several types of ports and interfaces that are used to connect to the device.

Like many networking devices, Cisco devices use light emitting diode (LED) indicators to provide status information.
An Interface LED indicates the activity of the corresponding interface. If an LED is off when the interface is
active, and the interface is correctly connected, this may be an indication of a problem with that interface.
If an interface is extremely busy, its LED is always on.

### LAN and WAN interfaces
The conections on a Cisco router can be grouped into two categories: In-band router interfaces and management
ports.

- **In-band Router Interfaces -** Are the LAN and WAN interfaces configured with IP addressing to carry user
traffic. Ethernet interfaces are most common LAN connections, while common WAN connections include serial and
DSL interfaces
- **Management Ports -** Include the console and AUX ports which are used to configure, manage, and troubleshoot
the router. Unlike LAN and WAN interfaces, management ports are not used for packet forwarding user traffic

Similar to a Cisco switch, there are several ways to access user EXEC mode in the CLI environment on a Cisco router.
These are the most common:
- **Console -** This is a physical management port that provides out-of-band access to a Cisco device.
Out-of-band access refers to access via a dedicated management channel that is used for device maintenance
purposes only
- **Secure Shell (SSH) -** SSH is a method for remotely establishing a secure CLI connection through a virtual
interface, over a network. Unlike a console connection, SSH connections require active networking services on the
device including an active interface configured with an address
- **Telnet -** Telnet is an insecure method of remotely establishing a CLI session through a virtual interface
over a network. Unlike SSH, Telnet does not provide a securely encrypted connection. User authentication,
passwords, and commands are sent over the network in plaintext

**Note:** Some devices, such as routers, may also support a legacy auxiliary port that was used to establish a CLI
session remotely using a modem. Similar to a console connection, the AUX port is out-of-band and does not require
networking services to be configured or available.

Telnet and SSH require an inband network connection which means that an administrator must access the router 
through one of the WAN or LAN interfaces.
- **Serial WAN Interfaces -** Added to EHWIC0 and labeled Serial 0 and Serial 1. Serial Interfaces are used for
connecting routers to external WAN networks. Each serial WAn interface has its own IP address and subnet mask,
which identifies it as a member of a specific network
- **Ethernet LAN Interfaces -** Labeled GE 0/0 and GE0/1. Ethernet interfaces are used for connecting to other
Ethernet-enable ddevices including switches, routers, firewalls, etcs. Each LAN interface has its own IPv4
address and subnet mask and/or IPv6 address and prefix, which identifies it as a member of a specific network

Inband interfaces receive and forward IP packets. Every configured and active interface on the router is a member
or host on a differnet IP network. Each interface must be configured with an IPv4 address and subnet mask of
a different network. The Cisco IOS does not allow two active interfaces on the same router to belong to the same
network.

### Bootset Files
Both Cisco routers and switches load the IOS image and startup configuration file into RAM when they are booted.

The running configuration is modified when the network administrator performs device configurations. Changes 
made to the running-config file should be saved to the startup-configuration file in NVRAM, in case the router 
is restarted or loses power.

### Router Bootup Process
There are three major phases to the bootup process:
1. Perform the POST and load the bootstrap program
2. Locate and load the Cisco IOS software
3. Locate and load the startup configuration file or enter setup mode

#### Performing POST and Load Bootstrap Program
During the Power-On Self-Test (POST), the router executes diagnostics from ROM on several hardware components,
including the CPU, RAM, and NVRAM. After the POST, the bootstrap program is copied from ROM into RAM. The main
task of the bootstrap program is to locate the Cisco IOS and load it into RAM.

**Note:** At this point, if you have a console conection to the router, you begin to see the output on the 
screen.

#### Locating and Loading Cisco IOS
The IOS is typically stored in flash memory and is copied into RAM for execution by the CPU. If the IOS image
is not alocated in flash, then the router may look for it using a Trivial File Transfer Protocol (TFTP) server.
If a full IOS image cannot be located, a limited IOS is copied into RAM, which can be used to diagnose problems
and transfer a full IOS into Flash Memory.

#### Locating and Loading the Configuration File
The bootstrap program then copie sthe startup configuration file from NVRAM into RAM. This becomes the running
configuration. If the stratup configuration file does not exist in NVRAM, the router may be configured to search
for a TFTP server. If a TFTP server is not found, then the router displays the setup mode prompt.

### Basic Router and Switch Configuration Steps
Cisco routers and Cisco switches have may similarities, support similar command structures and support many of
the same commands. In addition, both devices have identical initial configuration steps when implemented in a
network.

Name | Command
--- | ---
Configure the device name | hostname *name*
Secure user EXEC mode | line console 0 &rarr; password *password* &rarr; login
Secure remote Telnet / SSH access | line vty 0 15 &rarr; password *password* &rarr; login
Secure privileged EXEC mode | enable secret *password*
Secure all passwords in the config file | service password-encryption
Provide legal notification | banner motd *delimiter message delimiter*
Configure the management SVI | interface vlan 1 &rarr; ip address *ip-address subnet-mask* &rarr; no shutdown
Save the configuration | copy running-config startup-config

## Chapter 7: IP Addressing
### IPv4 Addresses
Each address consists of a string of 32 bits, divided into four sections called octets. Each octet contains
8 bits (or 1 byte) separated with a dot.

Working with binary numbers can be challenging. For ease of use by people, IPv4 adresses are commonly expressed
in dotted decimal notation.

For a solid understanding of network addressing, it is necessary to know binary addressing and gain practical
skills converting between binary and dotted decimal IPv4 addresses.

### Positional Notation
Positional notation means that a digit represents different values depending on the "position" the digit occupies
in the sequence of numbers. You already know the most common numbering system, the decimal (base 10) notation system.

### Binary to Decimal Conversion
To covnert a binary IPv4 address to its dotted decimal equivalent, divide the IPv4 address into four 8-bit 
octets. Next apply the binary positional value to the first octet binary number and calculate accordingly.

### Decimal to Binary Conversion
It is also necessary to understand how to convert a dotted decimal IPv4 address to binary. A useful tool is
the binary positional value table.

### Network and host Portions
Understanding binary notation is important when determining if two hosts are in the same network. Recall than
an IPv4 address is a hierarchical address that is made up of a network portion and a host portion. When determining
the network portion versus the host portion, it is neessary to look at the 32-bit stream. Within the 32-bit 
stream, a portion of the bits identify the network, and a portion of the bits identify the host.

Network Portion | Host Portion
--- | ---
192.168.10. | 10
11000000.10101000.00001010. | 00001010

The bits within the network portion of the address must be idnetical for all devices that reside in the same
network. The bits within the host portion of the address must be unique to identify a specific host within a
network.

But how do hosts know which portion of the 32-bits identifies the network and which identifies the host? That
is the job of the *subnet mask.*

### The Subnet Mask
Three dotted decimal IPv4 addresses must be configured when assigning an IPv4 configuration to host:
- **IPv4 address -** Unique IPv4 address of the host
- **Subnet mask -** Used to identify the network/host portion of the IPv4 address
- **Default gateway -** Identifies the local gateway (i.e. local router interface IPv4 address) to reach remote
networks

When an IPv4 address is assigned to a device, the subnet mask is used to determine th enetwork address where
the device belongs. The network address represents all the devices on the same network.

To idenfity the network and host portions of an IPv4 address, the subnet mask is compared to the IPv4 address
bit for bit, from left to right. The 1s in the subnet mask identiy the network portion while the 0s identify
the host portion. Not ethat the subnet mask does not actually contain the network or host portion of an IPv4
address, it just tells the computer where to look for these portions in a given IPv4 address.

The actual process used to identify the network portion and host portion is called ANDing.

### Logical AND
A logical AND is one of three basic binary operations used in digital logic. The other two are OR and NOT.While 
all three are used in data networks, only AND is used in determining the network address.

To identify the network address of an IPv4 host, the IPv4 address is logically ANDed, bit by bit, with the 
subnet mask. ANDing between the address and the subnet mask yields the network address.

### The Prefix Length
Expressing network addresses and host addresses with the dotted decimal subnet mask address can become cumbersome.
Fortunately, there is an alternate shorthand method of identifying a subnet mask called the prefix length.

Specifically, the prefix length is the number of bits set to 1 in the subnet mask. It is written in "slash
notation", which is a "/" followed by the number of bits set to 1. Therefore, count the number of bits in the
subnet mask and prepend it with a slash.

### Network, Host, and Broadcast Addresses
Each network address contains (or identifies) host addresses and a broadcast address.
- **Network Address -** Address and subnet mask refer to a network. All hosts within the network share the
same network address. The host portion is all 0s
- **Host Addresses -** Unique IP addresses assigned to hosts and devices. The host portion always contains
assorted 0s and 1s but never all 0s or all 1s
  - **First Host Address -** First available host IP address in that network. The host portion always has all
  0s and ends with a 1
  - **Last Host Address -** Last available host IP address in that network. The host portion always has all
  1s and ends with a 0
- **Broadcast Address -** A special address that communicates with all hosts in a network. For instance, when
a host sends a packet to the network broadcast IPv4 address, all other hosts in the network receive the packet.
The broadcast address uses the highest address in the network range. The host portion is all 1s

### Static IPv4 Address Assignment to a Host
Devices can be assigned an IP address either statically or dynamically.

In networks, some devices require a fixed IP address. For instance, printers, servers, and networking devices
need an IP address that does not change. For this reason, these devices are typically assigned static IP
addresses.

A host can also be configured with a static IPv4 address. Assigning host static IP addresses is acceptable in
small networks. however, it would be time-consuming to enter static addresses on each host in a large network.
It is important to maintain an accurate list of static IP addresses assigned to each device.

### Dynamic IPv4 Address Asisgnment to a Host
In most data networks, the largest population of hosts includes PCs, tablets, smartphones, printers, and IP
phones. It is also often the case that the user population and their devices change frequently. It would be
impractical to statically assign IPv4 addresses for each device. Therefore, these devices are assigned IPv4
addresses dynamically using the Dynamic Host Configuration Protocol (DHCP).

A host can obtain IPv4 addressing information automatically. The host is a DHCP client and requests IPv4 address
information from a DHCP server. The DHCP server provides an IPv4 address, subnet mask, default gateway, and 
other configuration information.

DHCP is generally the preferred method of assigning IPv4 addresses to hosts on large networks. An additional
benefit of DHCP is the address is not permanently assigned to a host but is only "leased" for a period of time.
If the host is powered down or taken off the network, the address is returned to the pool for reuse. This
feature is especially helpful for mobile users that come and go on a network.

### IPv4 Communication
A host successfully connected to a network can communicate with other devices in one of three ways:
- **Unicast -** The process of sending a packet from one host to an individual host
- **Broadcast -** The process of sending a packet from one host to all hosts in the network
- **Multicast -** The proces sof sending a packet from one host to a selected group of hosts, possibly in 
different networks

These three types of communication are used for different purposes in data networks. In all three cases, the
IPv4 address of the originating host is placed in the packet header as the source address.

### Unicast Transmission
Unicast communication is used for normal host-to-host communication in both a client/server and peer-to-peer
network. Unicast packets use the address of the destination device as the destination address and can be 
routed through an internetwork.

In an IPv4 network, the unicast address applied to an end device is referred to as the host address. For unicast
communication, the addresses assigned to the two end devices are used as the source and destination IPv4 
addresses. During th eencapsulation process, the source host uses its IPv4 address as the source address and
the IPv4 address of the destination host as the destination address.  Regardless of whether the destination
specified a packet as a unicast, broadcast or multicast; the source address of any packet is always the unicast 
address of the originating host.

**Note:** In this course, all communication between devices is unicast unless otherwise noted.

IPv4 unicast host addresses are in the address range of 0.0.0.0 to 223.255.255.255. However, within this range
are many addresses that are reserved for special purposes.

### Broadcast Transmission
Broadcast traffic is used to send packets to all hosts in the network using the broadcast address for the 
network. With a broadacst, the packet contains a destination IPv4 address with all ones (1s) in the host
portion. This means that all hosts on that local network (broadcast domain) will receive and look at the packet.
Many network protocols, such as DHCP, use broadcasts. When a host receives a packet sent to the network
broadcast address, the host processes the packet as it would a packet addressed to its unicast address.

Broadcast may be directed or limited. A directed broadcast is sent to all hosts on a specific network. By
default, routers do not forward broadcasts.

When a packet is broadcast, it uses resources on the network and causes every receiving host on the network to
process the packet. Therefore, broadacst traffic should be limited so that it does not adeversely affect the
performance of the network or devices. Because routers separate broadcast domains, subdividing networks can
improve network performance by elminating excessive broadcast traffic. 

### Multicast Transmission
Multicast tranmission reduces traffic by allowing a host to send a single packet to a selected set of hosts that
subscribe to a multicast group.

IPv4 has reserved the 224.0.0.0 to 239.255.255.255 addresses as a multicast range. The IPv4 multicast addresses
224.0.0.0 to 224.0.0.255 are reserved for multicasting on the local network only. These addresses are to be used
for multicast groups on a local network. A router connected to the local network recognizes that these packets
are addressed to a local network multicast group and never forwards them further. A typical use of reserved
local network multicast address is in routing protocols using multicast transmission to exchange routing
information. For instance, 224.0.0.9 is the multicast address used by Routing Information Protocol (RIP)
version 2 to communicate with other RIPv2 routers.

Hosts taht receive particular multicast data are called multicast clients.

Each multicast group is represented by a single IPv4 multicast destination address. When an IPv4 host subscribes
to a multicast group, the host processes packets addressed to this multicast address, and packets addressed to
its uniquely allocated unicast address.

### Public and Private IPv4 Addresses
Public IPv4 addresses are addresses which are globally routed between ISP (Internet Service Provider) routers.
However, not all available IPv4 addresses can be used on the Internet. There are blocks of addresses called
private addresses that are used by most organizations to assign IPv4 addresses to internal hosts.

In the mid-1990s private IPv4 addresses were introduced because of the depletion of IPv4 address space. Private
IPv4 addresses are not unique and can be used by an internal network.

Specifically, the private address blocks are:
- **10.0.0.0/8** or **10.0.0.0** to **10.255.255.255**
- **172.16.0.0/12** or **172.16.0.0** to **172.31.255.255**
- **192.168.0.0/16** or **192.168.0.0** to **192.168.255.255**

It is important to know that addresses within these address blocks are not allowed on the Internet and must be
filtered (discarded) by Internet routers. The Internet Service Provider (ISP) routers would see that the source
IPv4 addresses in the packets are from private addresses and would, therefore, discard the packets.

**Note:** Private addresses are defined in RFC 1918.

Most organizations use private IPv4 addresses for their internal hosts. However, these RFC 1918 address are not
routable in the Internet and must be translated to a public IPv4 address. Network Address Translation (NAT) is
used to translate between private IPv4 and public IPv4 addresses. This is usually done on the router that
connects the internal network of the ISP's network.

Home routers provide the same capability. For instance, most home routers assign IPv4 addresses to their wired
and wireless hosts from the private address of 192.168.1.0/24. The home router interface that connects to the
Internet Service Provider (ISP) network is assigned a public IPv4 address to use on the Internet.

### Special User IPv4 Addresses
There are certain addresses such as the network address and broadcast address that cannot be assigned to hosts.
There are also special addresses that can be assigned to hosts, but with restrictions on how those hosts can
interact within the network.

- **Loopback addresses (127.0.0.0/8 or 127.0.0.1 or 127.255.255.254) -** More commonly identified as only
127.0.0.1, these are special addresses used by a host to direct traffic to itself
- **Link-Local addresses (169.254.0.0/16 or 169.254.0.1 to 169.254.25.254) -** More commonly known as the
automatic Private IP Addressing (APIPA) addresses, they are used by a Windows DHCP client to self-configure
in the event that there are no DHCP severs available. Useful in a peer-to-peer connection
- **TEST-NET addresses (192.0.2.0/24 or 192.0.2.0 to 192.0.2.255) -** These addresses are set aside for
teaching and learning purposes and can be used in dcumentation and network examples

**Note:** There are also Experimental Addresses in the block 240.0.0.0 to 255.255.255.254 that are reserved
for future use (RFC 3330).

### Legacy Classful Addressing
In 1981, Internet IPv4 addresses were assigned using classful addressing as defined in RFC 790, Assigned Numbers.
Customers were allocated a network address based on one of three classes A, B, or C. The RFC divided the unicast
ranges into specific classes called:
- **Class A (0.0.0.0/8 to 127.0.0.0/8) -** Designed to support extremely large networks with more than 16 million
host addresses. It used a fixed /8 prefix with the first octet to indicate the network address and the remaining
three octets for host addresses. All class A addresses required that the most significant bit of the
high-order octet be a zero creating a total of 128 possible class A networks
- **Class B (128.0.0.0/16 - 191.255.0.0/16) -** Designed to suport the needs of moderate to large size of netowrks
with up to approximately 65,000 host addresses. It used a fixed /16 prefix with the two high-order octets to 
indicate the network and the remaining octet for the host addresses. The most significant three bits of the
high-order octet must be 110 creating over 2 million possible networks
- **Class C (192.0.0.0/24 - 223.255.255.0/24) -** Designed to support small networks with a maximum of 254 hosts.
It used a fixed /24 prefix with the first three octets to indicate the network and the remainin goctet for the
host addresses. The most significant three bits of the high-order octet must be 110 creating over 2 million 
possible networks

**Note:** There is alos a Class D multicast block consisting of 224.0.0.0 to 239.0.0.0 and a Class E experimental
address block consisting of 240.0.0.0 - 255.0.0.0

### Classless Addressing
The system in use today is referred to as *classless addressing*. The formal name is Classless Inter-Domain 
Routing (CIDR, pronounced "cider"). In 1993, the IETF created a new set of standards that allowed service
providers to allocate IPv4 addresses on any address bit boundary (prefix length) instead of only by a class A,
B, or C address. This was to help delay the depletion and eventual exhaustion of IPv4 addresses.

The IETF knew that CIDR was only a temporary solution and that a new IP protocol would have to be devleoped to
accomodate the rapid growth in the number of Internet users. In 1994, the IETF began its work to find a successor
to IPv4, which eventually became IPv6.

### Assignment of IP Addresses
For a company or organization to support network hosts, such as web servers accessible from the Internet, that
organization must have a block of public addresses assigned. Remember that public addresses must be unique, and
use of these public addresses is regulated and allocated to each organization separately. This is true for IPv4
and IPv6 addresses.

Both IPv4 and IPv6 addresses are managed by the Internet Assigned Numbers Authority (IANA) (http://www.iana.org).
The IANA manages and allocated blocks of IP addresses to the Regional Internet Registries (RIRs).
- **ARIN -** American Registry for Internet Numbers (ARIN) manages and maintains IPv4 and IPv6 addresses for
North America
- **LACNIC -** Regional Latin-American and Caribbean IP Address Registry (LACNIC) manages and maintains IPv4 
and IPv6 addresses for Latin America and some Caribbean islands
- **RIPE NCC -** Réseaux IP Europeans (RIPE) manages and maintains IPv4 and IPv6 addresses for Europe, the
Middle East, and Central Asia
- **APNIC -** Asia Pacific Network Information Centre (APNIC) manages and maintains IPv4 and IPv6 addresses
for the Asia and Pacific regions including Australia
- **AfriNIC -** African Network Information Centre (AfriNIC) manages and maintains IPv4 and IPv6 addresses for
Africa

RIRs are responsible for allocating IP addresses to ISPs who in turn provide IPv4 address blocks to orgainzations
and smaller ISPs. Organizations can get their addresses directly from an RIR subject to the policies of that RIR

### IPv6 and IPv6 Coexistence
The IETF has created various protocols and tools to help network administrators migrate their networks to IPv6.
The migration techniques can be divided into three categories:

- **Dual Stack -** Allows IPv4 and IPv6 to coexist on the same network segment. Dual stack devices run both
IPv6 and IPv6 protocol stacks simultaneously
- **Tunneling -** Is a method of transporting an IPv6 packet over an IPv4 network. The IPv6 packet is encapsulated
inside an IPv4 packet, similar to other types of data
- **Translation -** NAT64 allows IPv6-enabled devices to communicate with IPv4-enabled devices using a translation
technique similar to NAT for IPv4. An IPv6 packet is translated to an IPv4 packet and vice versa

**Note:** Tunneling and translation are only used where needed. The goal should be native IPv6 communications
from source to destination.

### IPv6 Address Representation
IPv6 addresses are 128 bits in length and written as a string of hexadecimal values. Every 4 bits is represented
by a single hexadecimal digit; for a total of 32 hexadecimal values. IPv6 addresses are not case-sensitive and
can be written in either lowercase or uppercase.

#### Preferred Format
The preferred format for writting an IPv6 address is X:X:X:X:X:X:X:X with each "X" consisting of four hexadecimal
values. When referring to 8 its of a nIPv4 address we use the term octet. In IPv6, a hextet is the unofficial
term used to refer to a segment of 16 bits of four hexadecimal values. Each "X" is a single hextet, 16 bits or
four hexadecimal digits.

Preferred format means the IPv6 address is written using all 32 hexadecimal digits. It does not necessarily mean
it is the ideal method for representing the IPv6 address.

#### Rule 1 - Omit Leading 0s
the first rule to help reduce the notation of IPv65 addresses is to omit any leading 0s (zeros) in any 16-bit
section or hextet. For example:
- 01AB can be represented as 1AB
- 09F0 can be represented as 9F0
- 0A00 can be represented as A00
- 00AB can be represented as AB

This rule only applies to leading 0s, NOT to trailing 0s, otherwise the address would be ambiguous.

#### Rule 2 - Omit All 0 Segments
The second rule to help reduce the notation of IPv6 addresses is that a double colon ( :: ) can replace any 
single, contiguous string of one or more 16-bit segments (hextets) consisting of all 0s.

The double colon ( :: ) can only e used once within an address, otherwise there would be more than one possible
resulting address. When used with the omitting leading 0s technique, the notation of IPv6 address can often be
greatly reduced. This is commonly known as the compressed format.

#### IPv6 Address Types
- **Unicast -** An IPv6 unicast address uniquely identifies an interface on an IPv6-enabled device
- **Multicast -** An IPv6 multicast address is used to send a single IPv6 packet to multiple destinations
- **Anycast -** An IPv6 anycast address is any IPv6 unicast address that can be assigned to multiple devices.
A packet sent to an anycast address is routed to the nearest device having that address

Unlike IPv6, IPv6 doest not have a broadacst address. However, there is an IPv6 all-nodes multicast address
that essentially gives the same result.

#### IPv6 Prefix Length
IPv6 uses the prefix length to represent the prefix portion of the address. IPv6 does not use the dotted-decimal
subnet mask notation. The prefix length is used to indicate the network portion of an IPv6 address using the
IPv6 address/prefix length.

The prefix length can range from 0 to 128. A typical IPv6 prefix length for LANs and most other types of
networks is /64. This means the prefix or network portion of the address is 64 bits in length, leaving another
64 bits for the interface ID (host portion) of the address.

#### IPv6 Unicast Addresses
An IPv6 unicast address uniquely identifies an interface on an IPv6-enabled device. A packet sent to a unicast
address is received by the interface that is assigned that address. Similar to IPv4, a source IPv6 address must
be a unicast address. The destination IPv6 address can be either a unicast or a multicast address.

The most common types of IPv6 unicast addresses are global unicast addresses (GUA) and link-local unicast 
addresses.

##### Global unicast
A global unicast address is similar to a public IPv4 address. These are globally unique, internet routable
addresses. Global unicast addresses can be configured statically or assigned dynamically.

##### Link-local
Link-local addresses are used to communicate with other devices on the same local link. With IPv6, the term link
refers to a subnet. Link-local addresses are confined to a single link. Their uniqueness must only be confirmed
on that link because they are not routable beyond the link. In other words, routers will not forward packets
with a link-local source or destination address.

##### Unique local
IPv6 unique local addresses have some similarity to RFC 1918 private addresses for IPv4, but there are significant
differences. Unique local addresses are used for local addressing within a site or between a limited number of
sites. These addresses should not be routable in the global IPv6 and should not be translated to a global IPv6
address. Unique local addresses are in the range of FC00::/7 to FDFF::/7.

Unique local addresses can be used for devices that will never need or have access from another network.

#### IPv6 Link-local Unicast Addresses
The global unicast address is not a requirement. however, every IPv6-enabled network interface is required to
have a link-local address.

If a link-local address is not configured manually on an interface, the device will automatically create its own
without communicating with a DHCP server. IPv6-enabled hosts create an IPv6 link-local address even if the
device has not been assigned a global unicast IPv6 address. This allows IPv6-enabled devices to communicate 
with other IPv6-enabled devices on the same subnet. This includes communication with the default gateway.

IPv6 link-local addresses are in the FE80::/10 range. The /10 indicates that the first 10 bits are\
`1111 1110 10xx xxxx`. The first hextet has a range of `1111 1110 1000 0000` (FE80) to `1111 1110 1011 1111` 
(FEBF).

**Note:** Typically, it is the link-local address of the router, and not the global unicast address, that is 
used as the default gateway for other devices on the link.

### Structure of an IPv6 Global Unicast Address
IPv6 global unicast addresses (GUA) are globally unique and routable on the IPv6 Internet. These addresses are
equivalent to public IPv4 addreses. The Internet Commitee for Assigned Names and Numbers (ICANN), the operator 
for IANA, allocates IPv6 address blocks to the five RIRs. Currently, only global unicast addresses with the 
first three bits of 001 or 2000::/3 are being assigned. The first hexadecimal digit of GUA address will begin
with a 2 or a 3. This is only 1/8th of the total available IPv6 address space, excluding only a very small
portion for other types of unicast and multicast addresses.

**Note: The 2001:0DB8::/32 address has been reserved for documentation purposes, including use in examples.

A global unicast address has three parts:
- Global routing prefix
- Subnet ID
- Interface ID

##### Global Routing Prefix
The global routing prefix is the prefix or network portion of the address that is assigned by the provider,
such as an ISP, to a customer or site. Typically, RIRs assign a /48 global routing prefix to customers. This
can include everyone from enterprise business networks to individual households.

For example, the IPv6 address 2001:0DB8:ACAD::/48 has a prefix that indicates that the first 48 bits (3 hextets)
is the prefix or network portion of the address. The double colon ( :: ) prior to the /48 prefix length means
the rest of the address contains all 0s.

The size of the global routing prefix determines the size of the subnet ID.

##### Subnet ID
The Subnet ID is used by an organization to identify subnets within its site. The larger the subnet ID, the
more subnets available.

##### Interface ID
The IPv6 Interface ID is equivalent to the host portion of an IPv4 address. The term Interface ID is used
because a single host may have multiple interfaces, each having one or more IPv6 addresses. It is highly
recommended that in most cases /64 subnets should be used. In other words a 64-bit interface ID.

**Note:** Unlike IPv4, in IPv6, the all-0s and all-1s host addresses can be assigned to a device. The all-1s
address can be used due to the fact that broadcast addresses are not used within IPv6. The all-0s address can
also be used, but is reserved as a Subnet-Router anycast address, and should be assiged only to routers.

An easy way to read most IPv6 addresses is to count the number of hextets.

### Static Configuration of a Global Unicast Address
#### Router Configuration
Most IPv6 configuration and verification commands in the Cisco IOS are similar to their IPv4 counterparts. In
many cases, the only difference is the use of `ipv6` in place of `ip` within the commands.

#### Host Configuration
Manually configuring the IPv6 address on a host is similar to configuring an IPv4 address.

Just as with IPv4, configuring static addresses on clients does not scale to larger environments. For this
reason, most network administrators in an IPv6 network will enable dynamic assignment of IPv6 addresses.

There are two ways i nhwich a device can obtain an IPv6 global unicast address automatically:
- Stateless Address Autoconfiguration (SLAAC)
- Stateful DHCPv6

**Note:** When DHCPv6 or SLAAC is used, the local router's link-local address will automatically be specified
as the default gateway address.

### Dynamic Configuration - SLAAC
Stateless Address Autoconfiguration (SLAAC) is a method that allows a device to obtain its prefix, prefix length,
default gateway address, and other information from an IPv6 router without the use of a DHCPv6 server. Using
SLAAC, devices rely on the local router's ICMPv6 Router Advertisement (RA) messages to obtain the necessary
information.

IPv6 routers periodically send out ICMPv6 RA messages, every 200 seconds, to all IPv6-enabled devices on the
network. An RA message will also be sent in response to a host sending an ICMPv6 Router Solicitation (RS)
message.

IPv6 routing is not enabled by default. To enable a router as an IPv6 router, the `ipv6 unicast-routing` global
configuration command must be used.

**Note:** IPv6 addresses can be configured on a router without it being an IPv6 router.

The ICMPv6 RA message is a suggestion to a device on how to obtain an IPv6 global unicast address. The ultimate
decision is up to the device's operating system. The ICMPv6 RA message includes:
- **Network prefix and prefix length -** Tells the device which network it belongs to
- **Default gateway address -** This is an IPv6 link-local address, the source IPv6 address of the RA message
- **DNS addresses and domain name -** Addresses of DNS servers and domain name

There are three options for RA messages:
- Option 1: SLAAC
- Option 2: SLAAC with a stateless DHCPv6 server
- Option 3: Stateful DHCPv6 (no SLAAC)

#### RA Option 1: SLAAC
By default, the RA message suggests that the receiving device use the information in the RA mesage to create
its own IPv6 global unicast address and for all other information. The services of a DHCPv6 server are not
required.

SLAAC is stateless, which means there is no central server (for example, a stateful DHCPv6 server) allocating
global unicast addresses and keeping a list of devices and their addresses. With SLAAC, the client device uses
the information in the RA message to create its own global unicast address. The two parts of the address are 
created as follows:
- **Prefix -** Received in the RA message
- **Interface ID -** Uses the EUI-64 process or by generating a random 64 bit number

#### Dynamic configuration - DHCPv6
By default, the RA message is option 1, SLAAC only. The router's interface can be configured to send a router
advertisement using SLAAC and stateless DHCPv6, or stateful DHCPv6 only.

##### RA Option 2: SLAAC and Stateless DHCPv6
With this option, the RA message suggests devices use:
- SLAAC to create its own IPv6 global unicast address
- The router's link-local address, the RA's source IPv6 address for the default gateway address
- A stateless DHCPv6 server to obtain other information such as DNS sever address and domain name

A stateless DHCPv6 server distributes DNS server addresses and domain names. It does not allocate global unicast
addresses.

##### RA Option 3: Stateful DHCPv6
Stateful DHCPv6 is simlar to DHCP for IPv4. A device can automatically receive its addressing information
including a global unicast address, prefix length, and the addresses of DNS servers using the services of a
stateful DHCPv6 server.

With this option the RA message suggets devices use:
- The router's link-local address, the RA's source IPv6 address for the default gateway address
- A stateful DHCPv6 server to obtain a global unicast address, DNS server address, domain name and all other
information

A stateful DHCPv6 server allocates and maintains a list of which device recives which IPv6 address. DHCP for
IPv4 is stateful.

**Note:** The default gateway address can only be obtained dynamically from the RA message. The stateless or
stateful DHCPv6 server does not provide the default gateway address.

### EUI-64 Process and Randomly Generated
When the RA message is either SLAAC or SLAAC with stateless DHCPv6, the client must generate its own Interface
ID. The client knows the prefix portion of the address from the RA message but must create its own Interface ID.
The Interface ID can be created using the EUI-64 process or a randomly generated 64-bit number.

#### EUI-64 Process
IEEE defined the Extended Unique Identifier (EUI) or modified EUI-64 process. This process uses a client's 
48-bit Ethernet MAC address, and inserts another 16 its in the middle of the 48-bit MAC address to create a 
64-bit interface ID.

Ethernet MAC addresses are usually represented in hexadecimal and are made up of two parts:
- **Organizationally Unique Identifier (OUI) -** The OUI is a 24-bit (6 hexadecimal digits) vendor code
assigned by IEEE
- **Device Identifier -** The device idnetifier is a unique 24-bit (6 hexadecimal digits) value within a common
OUI

An EUI-64 Interface ID is represented in binary and is made up of three parts:
- 24-bit OUI from the client MAC address, but the 7th bit (the Universally/Locally (U/L) bit) is reversed. This
means that if the 7th bit is a 0, it becomes a 1, and vice versa.
- The inserted 16-bit value FFFE
- 24-bit Device Identifier from the client MAC address

1. Divide the MAC address between the OUI and device identifier
2. Insert the hexadecimal value FFFE, which in binary is: 1111 1111 1111 1110
3. Convert ht efirst 2 hexadecimal values of the OUI to binary and flip the U/L bit (bit 7)

The result is an EUI-64 generated interface ID. i.e. FE99:47FF.FE75.CEE0.

**Note:** The use of the U/L bit, and the reasons for reversing its value, are discussed in RFC 5342.

The advantage of EUI-64 is the Ethernet MAC address can be used to determine the interface ID. It also allows
network administrators to easily track an IPv6 address to an end-device using the unique MAC address. However,
this has caused privacy concerns among many users. They are concerned that their packets can be traced to the
actual physical computer. Due to these concerns, a randomly generated interface ID may be used instead.

#### Randomly Generated Interface IDs
Depending upon the operating system, a device may use a randomly generated Interface ID instead of using the
MAC address and the EUI-64 process. 

After the Interface ID is establshed, either through the EUI-64 process or through random generation, it can be
combined with an IPv6 prefix in the RA mesage to create a global unicast address.

**Note:** To ensure the uniqueness of any IPv6 unicast address, the client may use a process known as Duplicate
Address Detection (DAD). This is similar to an ARP request for its own address. If there isn't a reply, then
the address is unique.

#### Dynamic Link-Local Addresses
All IPv6 devices must have an IPv6 link-local address. A link-local address can be established dynamically or
configured manually as a static link-local address.

Operating systems will typically use the same method for both a SLAAC created global unicast address and a 
dynamically assigned link-local address.

Cisco routers automatically create an IPv6 link-local address whenever a global unicast address is assigned to
the interface. By default, Cisco IOS routers use EUI-64 to generate the Interface ID for all link-local address
on IPv6 interfaces. For serial interfaces, the router will use the MAC address of an Ethernet Interface. Recall
that a link-local address must be unique only on that link or network. However, a drawback to using the dynamically 
assigned link-local address is its long interface ID, which make it challenging to identify and remember
assigned addresses.

To make it easier to recognize and remember these addresses on routers, it is common to statically configure
IPv6 link-local addresses on routers.

### Static Link-Local Addresses
Configuring the link-local address manually proivdes the ability to create an address that is recognizable
and easier to remember.

Link-local addresses can be configured manually using the same interface command used to create IPv6 global
unicast addresses but with the additional `link-local` parameter. When an address begins with his hextet within
the range of FE80 to FEBF, the link-local parameter must follow the address.

### Verifying IPv6 Address Configuration
The `show ipv6 interface brief` command displays abbreviated output for each of the interfaces.

Each interface has two IPv6 addresses. The second address for each interface is the global unicast address
that was configured. The first address, the one that begins with FE80, is the link-local unicast address for
the interface. Recall that the link-local address is automatically added to the interface when a global unicast
address is assigned.

Serial interfaces do not have Ethernet MAC addresses, so Cisco IOS uses the MAC address of the first available
Ethernet Interface. This is possible because link-lokal interfaces only have to be unique on that link.

The link-local address of the router interface is typically the default gateway address for devices on that
link or network.

The `show ipv6 route` command can be used to verify that IPv6 networks and specific IPv6 interface addresses
have been installed in the IPv6 routing table. The `show ipv6 route` command will only display IPv6 networks,
not IPv4 networks.

Within the route table, a `C` next to a route indicates that this is a directly connected network.

**Note:** The `L` indicates a Local route, the specific IPv6 address assigned to the interface. This is not a
link-local address. Link-local addresses are not uncluded in the router's routing table because they are not
routable addresses. 

The IPv6 global unicast address configured on the interface is also installed in the routing table as a local
route. The local route has a /128 prefix. Local routes are used by the routing table to efficiently process
packets with a destination address of the router's interface address.

#### Assigned IPv6 Multicast Addresses
IPv6 multicast addresses are similar to IPv4 multicast addresses. Recall that a multicast address is used to
send a single packet to one or more destinations (multicast group). IPv6 multicast addresses have the prefix
FF00::/8.

**Note:** Multicast addresses can only be destination addresses and not source addresses.

There are two types of IPv6 multicast addresses:
- Assigned multicast
- Solicited node multicast

#### Assigned Multicast
Assigned multicast addresses are reserved multicast addresses for predefined groups of devices. An assigned
multicast address is a single address used to reach a group of devices running a common protocol or service.
Assigned multicast addresses are used in context with specific protocols such as DHCPv6.

Two common IPv6 assigned multicast groups inlcude:

- **FE02::1 All-nodes-mulicast group -** This is a multicast group that all Ipv6-enabled devices join. A
packet sent to this group is received and rocessed by all IPv6 interfaces on the link or network. This has 
the smae effect as a broadcast address in IPv4. An IPv6 router sends ICMPv6 RA messages to the all-node multicast
group. The RA message informs all IPv6-enabled devices on the network about addressing information, such as the
prefix, prefix length, and default gateway.

- **FF02::2 All Routers multicast group -** This is a multicast group that all IPv6 routers join. A router
becomes a member of this group when it is enabled as an IPv6 router with the `ipv6 unicast-routing` global
configuration command. A packet sent to this group is received and processed by all IPv6 routers on the link
or network.

IPv6-enabled devices send ICMPv6 Router Solicitation (RS) messages to the all-routers multicast address. The
RS message requests an RA message from the IPv6 router to assist the device in its address configuration.

### Solicited-Node IPv6 Multicast Addresses
A solicited multicast address is similar to the all-nodes multicast address. The advantage of a solicited-node
multicast address is that it is mapped to a special Ethernet multicast address. This allows the Ethernet NIC
to filter the frame by examining the destination MAC address without sending it to the IPv6 process to see if
the device is the intended target of the IPv6 packet.

### ICMPv4 and ICMPv6
The purpose of these messages is to provide feedback about issues related to the processing of IP packets under
certain conditions, not to make IP reliable. ICMP messages are not required and are often not allowed within a
network for security reasons.

ICMPv4 is th emessaging protocol for IPv4. ICMPv6 provides the same services for IPv6 but includes additional
functionality.

ICMP messages common to both ICMPv4 and ICMPv6 include:
- Host confirmation
- Destination or SErvice Unreachable
- Time exceeded
- Route redirection

#### Host Confirmation
An ICMP Echo Message can be used to determine if a host is operational. This use of the ICMP Echo messages is
the basis of the ping utility.

#### Destination or SErvice Unreachable
When a host or gateway receives a packet that it cannot deliver, it can use an ICMP Destination Unreachable
message to notify the source that the destination or service is unreachable.

Some of the Destination Unreachable codes for ICMPv4 are:
- 0 - Net unreachable
- 1 - Host unreachable
- 2 - Protocol unreachable
- 3 - Port unreachable

**Note:** ICMPv6 has similar but sightly different codes for Destination Unreachable messages.

#### Time Exceeded
An ICMPv4 Time Exceeded message is used by a router to indicate that a packet cannot be forwarded because the
Time to Live (TTL) field of the packet was decremented to 0.

ICMPv6 also sends a Time Exceeded message if the router cannot forward an IPv6 packet because the packet has
expried. IPv6 does not have a TTL field; it uses the hop limit field to determine if the packet has expired.

### ICMPv6 Router Solicitation and Router Advertisement Messages 
The information and error messages found in ICMPv6 are very similar to the control and error messages implemented
by ICMPv4.

ICMPv6 includes four new protocols as part of the Neighbor Discovery Protocol (ND or NDP).

Messaging between an IPv6 router and an IPv6 device:
- Router Solicitation (RS) message
- Router Advertisement (RA) message

Messaging between IPv6 devices:
- Neighbor Solicitation (NS) message
- Neighbor Advertisement (NA) message

**Note:** ICMPv6 ND also includes the redirect message, which has a similar function to the redirect message
used in ICMPv4.

Neighbor Solicitation and Neighbor Advertisement messages are used for Address resolution and Duplicate Address
Detection (DAD).

#### Address Resolution
Address resolution is used when a device on on the LAN knows the IPv6 unicast address of a destination but does
not know its Ethernet MAC address. To determine the MAC address for the destination, the device will send an NS
message to the solicited node address. The message will include the known (targeted) IPv6 address. The device
that has the targeted IPv6 address will respond with a NA message containing its Ethernet MAC address.

#### Duplicate Address Detection
When a device is assigned a global unicast or link-local unicast address, it is recommended that DAD is
performed on the address to ensure that it is unique. To check the uniqueness of an address, the device will
send an NS message with its own IPv6 address as the targeted IPv6. If another device on the network has this
address, it will respond with an NA message. This NA message will notify the sending device that the address is
in use. If a corresponding NA message is not returned within a certain period of time, the unicast address is
unique and acceptable for use.

**Note:** DAD is not required, but RFC 4861 recommends that DAD is performed on unicast addresses.

#### Ping -Testing the Local Stack
Ping is a testing utility that uses ICMP echo request and echo reply messages to test connectivity between
hosts. Ping works with oth IPv4 and IPv6 hosts.

To test connectivity to another host on a network, an echo request is sent to the host address using the ping
command. If the host at the specified address receives the echo request, it respnods with an echo reply. As
each echo reply is received, ping provides feedback on the time between when the request was sent and when the
reply was received. This can be a measure of network performance.

##### Pinging the Local Loopback
To perform this test, we ping the local loopback address of 127.0.0.1 for IPv4 (::1 for IPv6).

A response from loopback indicates that IP is properly installed on the host. This response comes from the 
network layer. This response is not, however, an indicatio that the addresses, masks, or gateways are properly
configured. Nor does it indicate anything about the status of the lower layer of the network stack. This simply
tests IP down through the network layer of IP. An error message indicates that TCP/IP is not operational on the
host.

### Traceroute - Testing the Path
Traceroute (tracert) is a utility that generates a list of hops that were succesfully reached along the path.
This list can provide important verification and troubleshooting information. If the data reaches the destination,
then the race lists the interface of every router in the path between the hosts. If the data fails at some hop
along the way, the address of the last router that responded to the trace can provide an indication of where
the problem or security restrictions are found.

#### Round Trip Time (RTT)
The round trip time is the time a packet takes to reach the remote host and for the response from the host to
return. An asterisk (*) is used to indicate a lost or unreplied packet.

This information can be used to locate a problematic router in the path. If the display shows high response 
times or data losses from a particular hop, this is an indication that the resources of the router or its 
connections may be stressed.

#### IPv4 TTL and IPv6 Hop Limit
The first sequence of messages sent from traceroute will have a TTL field value of 1. This causes the TTL to
time out the IPv4 packet at the first router. This router then responds with an ICMPv4 message. Traceroute now
has the address of the first hop.

Traceroute then progressively increments the TTL field (2,3,4...) for each sequence of messages. This provides
the trace with the address of each hop as the packets timeout further down the path. The TTL field continues to
be increased until the destination is reached, or it is incremented to a predefined maximum.

After the final destination is reached, the host responds with either an ICMP port unreachable message or an 
ICMP echo reply message instead of the ICMP time exceeded message.

## Chapter 9: Transport Layer
### Role of the Transport Layer
The transport layer is responsible for establishing a temporary communication session between two applications
and delivering data between them. An application generates data that is sent from an application on a source
host to an application on a destination host. This is without regard to the destination host type, the type
of media over which the data must travel, the path taken by the data, the congestion on a link, or the size of
the network.

### Transport Layer Responsibilities
#### Tracking Individual Conversations
At the transport layer, each set of data flowing between a source application and a destination application is
known as a conversation. A host may have multiple applications that are communicating across the network
simultaneosly. Each of these applications communicates with one or more applications on one or more remote hosts.
It is the responsibility of the transport layer to maintain and track these multiple conversations.

#### Segmenting Data and Reassembling Segments
Data must be prepared to be sent across the media in manageable pieces. Most networks have a limitation on the
amount of data that can be included in a single packet. Transport layer protocols have services that segment
the application data into blocks that are an appropriate size. This service includes the encapsulation required
on each piece of data. A header, used for reassembly, is added to each block of data. This header is used to 
track the data stream.

At the destination, the transport layer must be able to reconstruct the pieces of data into a complete data
stream that is useful to the application layer.

#### Identifying the Applications
To pass data streams to the proper applications, the transport layer must identify the target application. To
accomplish this, the transport layer assigns each application an identifier called a port number. Each software
process that needs to access the network is assigned a port number unique to that host.

### Conversation Multiplexing
Sending some types of data across a network, as one complete communication stream, can consume all o the
available bandwidth. This will then prevent other communications from occurring at the same time. It would also
make error recovery and retransmission of damaged data difficult.

Segmenting the data into smaller chuncks enables many different communications, from many different users, to 
be interleaved (multiplexed) on the same network.

To identify each segment of data, the transport layer adds a header containing binary data organized into
several fields. It is the values in these fields that enable various transport layer protocols to perform
different functions in managing data communication.

### Transport Layer Reliability
The transport layer is also responsible for managing reliability requirements of a conversation. Different
applications have different transport reliability requirements.

IP is concerned only with th estructure, addressing, and routing of packets. IP does not specify how the 
delivery or transportation of the packets take place. Transport protocols specify how to transfer messages
between hosts. TCP/IP provides two transport layer protocols, Transmission Control Protocol (TCP) and User
Datagram Protocol (UDP). IP uses these transport protocols to enable hosts to communicate and transfer data.

TCP is considered a reliable, full-featured transport layer protocol, which ensures that all of the data
arrives at the destination. However, this required additional fields in the TCP header which increases the size
of the packet and also increases delay. In contrast, UDP is a simpler transport layer protocol that does not
provide for reliability. It therefore has fewer fields and is faster than TCP.

### TCP
TCP transport is analogous to sending packages that are tracked from source to destination. If a shipping order
is broken up into several packages, a customer can check online to see the order of the delivery.

With TCP, there are three basic operations of reliability:
- Numbering and tracking data segments transmitted to a specific host from a specific application
- Acknowledging received data
- Retransmitting any unacknowledged data after a certain period of time.

### UDP
While the TCP reliability functions provide more robust communication between applications, they also incur 
additional overhead and possible delays in transmission. There is a trade-off between the value of reliability
and the burde nit places on network resources. Adding overhead to ensure reliability for some applications 
could reduce the usefulness of the application and can even be detrimental. In such cases, UDP is a better
transport protocol.

UDP provides the basic functions for delivering data segments between the appropriate applications, with very
little overhead and data checking. UDP is known as a best-effort delivery protocol. In the context of 
networking, best-effor delivery is referred to as unreliable because there is no acknowledgment that the data
is received at the destination. With UDP, there are no transport layer processes that inform the sender of a
successful delivery.

UDP is similar to placing a regular, non-registered, letter in the mail. The sender of the letter is not aware
of the availability of the receiver to receive the letter. Nor is the post office responsible for tracking the
letter or informing the sender if the letter does not arrive at the final destination.

### The Right Transport Layer Protocol for the Right Application
- **TCP**
  - Databases
  - Web browsers
  - Email clients
- **UDP**
  - Live audio streaming
  - Live video
  - Voice over IP (VoIP)

**Note:** Applications that stream stored audio and video use TCP. For example, if your network suddenly cannot
support the bandwidth needed to watch an on-demand movie, the application pauses the playback. During the pause,
you might see a "buffering..." message while TCP works to re-establish the stream. Once all the segments are
in order and a minimum level of bandwidth is restored, your TCP session resumes and the movie begins playing.

### TCP Features
#### Establishing a Session
TCP is a connection-oriented protocol. A connection-oriented protocol is one that negotiates and establishes
a permanent connection (or session) between source and destination devices prior to forwarding any traffic.
Through session establishment, the devices negotiate the amount of traffic that can be forwarded at a given
time, and the communication data between the two can be closely managed.

#### Reliable Delivery
In networking terms, reliability means ensuring that each segment that the source sends arrives at the destination.
For many reasons, it is possible for a segment to become corrupted or lost completely, as it is transmitted
over the network.

#### Same-Order Delivery
Because networks may provide multiple routes that can have different transmission rates, data can arrive in the
wrong order. By numbering and sequencing the segments, TCP can ensure that these segments are reassembled into
the proper order.

#### Flow control
Network hosts have limited resources, such as memory and processing power. When TCP is aware that these
resources are overtaxed, it can request that the sending application reduce the rate of data flow. This is done
by TCP regulating the amount of data the source transmits. Flow control can prevent the need for retransmission
of the data when the receiving host's resources are overwhelmed.

#### TCP Header
TCP is a stateful protocol. A stateful protocol is a protocol that keeps track of the state of the communication
session. To track the state of a session, TCP records which information it has sent and which information has been
acknowledged. The stateful session begins with the session establishment and ends when closed with the session
termination.

Each TCP segment has 20 bytes of overhead in the header encapsulating the application layer data:
- **Source Port (16 bits) and Destination Port (16 bits) -** Used to identify the application
- **Sequence number (32 bits) -** Used for data reassembly purposes
- **Acknowledgment number (32 bits) -** Indicates data has been received and the next byte expected from the source
- **Header length (4 bits) -** Known as "data offset". Indicates the length of the TCP segment header
- **Reserved (6 bits) -** This field is reserved for the future
- **Control bits (6 bits) -** Includes bit codes, or flags, which indicate the purpose and function of the TCP segment
- **Window size (16 bits) -** Indicates the number of bytes that can be accepted at one time
- **Checksum (16 bits) -** Used for error checking of the segment header and data
- **Urgent (16 bits) -** Indicates if data is urgent

### UDP Features
Uesr Datagram Protocol (UDP) is considered a best-effor ttransport protocol. UDP is a lightweight transport
protocol that offers the same data segmentation and reassembly as TCP, but without TCP reliability and flow
control. UDP is such a simple protocol that it is usually described in terms of what it does not do compared
to TCP.

- Data is reconstructed in the order that it is received
- Any segments lost are not resent
- No session establishment
- Does not inform the sender about resource availability

### UDP Header
UDP is a stateless protocol, meaning neither the client, nor the server, is obligated to keep track of the
state of the communication session. if reliability is required when using UDP as the transport protocol, it
must be handled by the application.

One of the most important requirements for delivering live video and voice over the network is that the data
continues to flow quickly. Live video and voice applications can tolerate some data loss with minimal or no 
noticeable effect, and are perfectly suited to UDP.

The pieces of communication in UDP are called datagrams. These datagrams are sent as best-effor by the transport
layer protocol. UDP has a low overhead of 8 bytes.

### Multiple Separate Conversations
The transport layer must be able to separate and manage multiple communications with different transport requirement
needs. Users expect to be able to simultaneously receive and send email and instant messages, view websites, and
conduct a VoIP phone call. Each of these applications is sending and receiving data over the network at the
same time, despite different reliability requirements. Additionally, data from the phone call is not directed
to the web browser, and text from an instant message does not appear in an email.

TCP and UDP manage these multiple simultaneous conversations by using header fields that can uniquely identify
these applications. These unique identifiers are the port numbers.

### Port Numbers
The source port number is associated with the originating application on the local host. The destination port
number is associated with the destination application on the remote host.

#### Source Port
The source port number is dynamically generated by the sending device to identify a conversation between two
devices. This process allows multiply conversations to occur simultaneously. It is common for a device to send
multiple HTTP service requests to a web server at the same time. Eac separate HTTP conversation is tracked
based on the source ports.

#### Destination Port
The client places a destination port number in the segment to tell the destination server what service is being
requested. For example, when a client specifies port 80 in the destination port, the server that receives the
message knows that web services are being requested. A server can offer more than one service simultaneously
such as web services on port 80 at the same time that it offers File Transfer Protocol (FTP) connection
establishment on port 21.

### Socket Pairs
The source and destination ports are placed within the segment. The segments are then encapsulated with an IP
packet. The IP packet contains the IP address of the source and destination. The combination of the source IP
address and source port number, or the destination IP address and destination port number is known as a socket.
The socket is used to identify the server tand service being requested by the client. A client socket might
look like this, with 1099 representing the source port number: 192.168.1.5:1099

The socket on a web server might be: 192.168.1.7:80

Together, these two sockets combine to form a socket pair: 192.168.1.5:1099, 192.168.1.7:80

Sockets enable multiple processes, running on a client, to distinguish themselves from each other, and
multiple connections to a server process to be distinguished from each other.

The source port number acts as a return address for the requesting application. The transport layer keeps track
of this port and the application that initiated the request so that when a response is returned, it can be
forwarded to the correct application.

### Port Number Groups
The Internet Assigned Numbers Authority (IANA) is the standards body responsible for assigning various addressing
standards, including port numbers. There are different types of port numbers.
- **Well-known Ports (Numbers 0 to 1023) -** Reserved for services and applications
- **Registered Ports (Numbers 1024 to 49151) -** Custom applications
- **Dynamic or Private Ports (Numbers 49152 to 65535) -** Usually assigned dynamically by the client's OS when
a connection to a service is initiated. The dynamic port i sthen used to identify the client application during
communication

**Note:** Some client operating systems may use registered port numbers instead of dynamic port numbers for
assigning source ports.

### The netstat Command
Unexplained TCP connections can pose a major security threat. They can indicate that something or someone is
connected to the local host. Sometimes it is necessary to know which active TCP connections are open and running
on a networked host. Netstat is an important network utility that can be used to verify those connections.

By default, the netstat command will attempt to resolve IP addresses to domain names and port numbers to 
well-known applications. The **-n** option can be used to display IP addresses and port numbers in their 
numerical form.

### TCP Server Processes
Each application process running on the server is configured to use a port number, either by defaul tor manually,
by a system administrator. An individual server cannot have two services assigned to the same port number
within the same transport layer services.

### TCP Conection Establishment
In some cultures, when two persons meet, they often greet each other by shaking hands. The act of shaking hands
is understood by both parties as a signal for a friendly greeting. Connections on the network are similar. In
TCP connections, the host client establishes the connection with the server.

A TCP connection is established in three steps:
- **Step 1 -** The initiating client requests a client-to-server communication session with the server
- **Step 2 -** The server acknowledges the client-to-server communication session and requests a server-to-client
communication session
- **Step 3 -** The initiating client acknowledges the server-to-client communication session

### TCP Session Termination
To close a connection, the Finish (FIN) control flag must be set in the segment header. To end each one-way
TCP session, a two-way handshake, consisting of a FIN segment and an Acknowledgment (ACK) segment, is used.
Therefore, to terminate a single conversation supported by TCP, four exchanges are needed to end both sessions.

**Note:** When the client has no more data to send in the stream, it sends a segment with the FIN flag set.

- **Step 1 -** When the client has no more data to send in the stream, it sends a segment with the FIN flag set
- **Step 2 -** The server sends an ACK to acknowledge the receipt of the FIN to terminate the session from
client to server
- **Step 3 -** The server sends a FIN to the client to terminate the server-to-client session
- **Step 4 -** The client responds with an ACK to acknowledge the FIN from the server

When all segments have been acknowledged, the session is closed
