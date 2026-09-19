CATEGORY = "Computer Networks"

QUESTIONS = [
    # Easy (20)
    {
        "difficulty": "Easy",
        "question": "How many layers are present in the standard OSI Reference Model?",
        "options": ["4", "5", "7", "8"],
        "answer": "7",
        "explanation": "The OSI model consists of 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application."
    },
    {
        "difficulty": "Easy",
        "question": "What does IP stand for in computer networking?",
        "options": ["Internet Protocol", "Internal Program", "Interface Port", "Interconnected Packet"],
        "answer": "Internet Protocol",
        "explanation": "IP stands for Internet Protocol, the principal communications protocol for relaying datagrams across network boundaries."
    },
    {
        "difficulty": "Easy",
        "question": "What is the size of an IPv4 address in bits?",
        "options": ["16 bits", "32 bits", "64 bits", "128 bits"],
        "answer": "32 bits",
        "explanation": "IPv4 addresses are 32-bit binary numbers, typically written as four decimal octets (e.g., 192.168.1.1)."
    },
    {
        "difficulty": "Easy",
        "question": "What is the size of an IPv6 address in bits?",
        "options": ["32 bits", "64 bits", "128 bits", "256 bits"],
        "answer": "128 bits",
        "explanation": "IPv6 addresses are 128 bits in length, written as eight groups of four hexadecimal digits."
    },
    {
        "difficulty": "Easy",
        "question": "Which protocol provides reliable, connection-oriented byte-stream delivery with error checking and flow control?",
        "options": ["UDP", "TCP", "IP", "ICMP"],
        "answer": "TCP",
        "explanation": "TCP (Transmission Control Protocol) establishes a reliable connection with acknowledgments, retransmissions, and flow control."
    },
    {
        "difficulty": "Easy",
        "question": "Which protocol is connectionless and best-effort, prioritizing speed over reliability?",
        "options": ["TCP", "UDP", "FTP", "SSH"],
        "answer": "UDP",
        "explanation": "UDP (User Datagram Protocol) is a lightweight connectionless transport protocol without retransmissions or handshakes."
    },
    {
        "difficulty": "Easy",
        "question": "What is the default port number for HTTP web traffic?",
        "options": ["21", "22", "80", "443"],
        "answer": "80",
        "explanation": "HTTP (HyperText Transfer Protocol) runs on default port 80; HTTPS runs on port 443."
    },
    {
        "difficulty": "Easy",
        "question": "What is the default port number for secure HTTPS traffic?",
        "options": ["80", "443", "8080", "25"],
        "answer": "443",
        "explanation": "HTTPS runs over TLS/SSL on well-known port 443."
    },
    {
        "difficulty": "Easy",
        "question": "What is the primary function of the Domain Name System (DNS)?",
        "options": ["Translating human-friendly domain names (e.g., google.com) into numerical IP addresses", "Assigning MAC addresses to network cards", "Encrypting email traffic", "Routing packets across LANs"],
        "answer": "Translating human-friendly domain names (e.g., google.com) into numerical IP addresses",
        "explanation": "DNS acts as the phonebook of the Internet, resolving hostnames to IP addresses."
    },
    {
        "difficulty": "Easy",
        "question": "Which layer of the OSI model is responsible for routing packets across interconnected networks?",
        "options": ["Data Link Layer", "Network Layer", "Transport Layer", "Physical Layer"],
        "answer": "Network Layer",
        "explanation": "The Network Layer (Layer 3) handles logical addressing and packet routing across networks (e.g. IP routers)."
    },
    {
        "difficulty": "Easy",
        "question": "What is the length of a standard Ethernet MAC (Media Access Control) address?",
        "options": ["32 bits", "48 bits (6 bytes)", "64 bits", "128 bits"],
        "answer": "48 bits (6 bytes)",
        "explanation": "A physical MAC address consists of 48 bits (6 bytes), formatted as six hexadecimal pairs (e.g., 00:1A:2B:3C:4D:5E)."
    },
    {
        "difficulty": "Easy",
        "question": "Which networking device operates at Layer 2 (Data Link Layer) and forwards frames based on MAC addresses?",
        "options": ["Hub", "Switch", "Router", "Repeater"],
        "answer": "Switch",
        "explanation": "A network switch operates at Layer 2, maintaining a MAC address table to forward frames directly to target ports."
    },
    {
        "difficulty": "Easy",
        "question": "Which protocol automatically assigns dynamic IP addresses and configuration parameters to network hosts?",
        "options": ["DNS", "DHCP", "ARP", "BGP"],
        "answer": "DHCP",
        "explanation": "DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses, subnet masks, and gateways to clients."
    },
    {
        "difficulty": "Easy",
        "question": "Which protocol is used to map a known IP address to its corresponding physical MAC address in a local network?",
        "options": ["ARP (Address Resolution Protocol)", "RARP", "DNS", "ICMP"],
        "answer": "ARP (Address Resolution Protocol)",
        "explanation": "ARP broadcasts queries on the local link to find the MAC address matching a specific IPv4 address."
    },
    {
        "difficulty": "Easy",
        "question": "What is the command utility `ping` based on?",
        "options": ["TCP handshake", "ICMP (Internet Control Message Protocol) Echo Request / Reply", "UDP datagrams", "HTTP GET requests"],
        "answer": "ICMP (Internet Control Message Protocol) Echo Request / Reply",
        "explanation": "`ping` sends ICMP Echo Request packets and listens for ICMP Echo Reply packets to test reachability and latency."
    },
    {
        "difficulty": "Easy",
        "question": "Which network topology connects every node to a central hub or switch?",
        "options": ["Bus topology", "Ring topology", "Star topology", "Mesh topology"],
        "answer": "Star topology",
        "explanation": "In a star topology, all network nodes are connected individually to a central distribution node."
    },
    {
        "difficulty": "Easy",
        "question": "What is the loopback IP address in IPv4?",
        "options": ["127.0.0.1", "192.168.0.1", "10.0.0.1", "255.255.255.255"],
        "answer": "127.0.0.1",
        "explanation": "127.0.0.1 is the standard loopback address (localhost) used to test network software on the local machine."
    },
    {
        "difficulty": "Easy",
        "question": "Which protocol is used for securely accessing remote command-line shells over port 22?",
        "options": ["Telnet", "SSH (Secure Shell)", "FTP", "SNMP"],
        "answer": "SSH (Secure Shell)",
        "explanation": "SSH provides encrypted, secure remote command-line access over port 22."
    },
    {
        "difficulty": "Easy",
        "question": "What is the default port used by Simple Mail Transfer Protocol (SMTP)?",
        "options": ["21", "25", "110", "143"],
        "answer": "25",
        "explanation": "SMTP traditionally uses TCP port 25 for sending and relaying emails between mail servers."
    },
    {
        "difficulty": "Easy",
        "question": "What type of transmission sends a message to all devices on a local subnet simultaneously?",
        "options": ["Unicast", "Multicast", "Broadcast", "Anycast"],
        "answer": "Broadcast",
        "explanation": "Broadcast delivers a single network packet to all connected nodes on the local broadcast domain."
    },

    # Medium (20)
    {
        "difficulty": "Medium",
        "question": "How does TCP establish a connection between client and server?",
        "options": ["Three-Way Handshake (SYN, SYN-ACK, ACK)", "Two-Way Ping (REQ, RES)", "Four-Way Finish (FIN, ACK, FIN, ACK)", "UDP broadcast announce"],
        "answer": "Three-Way Handshake (SYN, SYN-ACK, ACK)",
        "explanation": "TCP establishes a reliable connection via the 3-way handshake: Client SYN -> Server SYN-ACK -> Client ACK."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of the Subnet Mask in IPv4?",
        "options": ["Distinguishing the network ID portion of an IP address from the host ID portion", "Encrypting packet payload", "Assigning MAC addresses", "Calculating round-trip time"],
        "answer": "Distinguishing the network ID portion of an IP address from the host ID portion",
        "explanation": "A subnet mask performs bitwise AND with an IP address to separate the network prefix from the local host bits."
    },
    {
        "difficulty": "Medium",
        "question": "How many usable host IP addresses are available in a `/24` subnet (e.g., subnet mask 255.255.255.0)?",
        "options": ["256", "254", "255", "128"],
        "answer": "254",
        "explanation": "A /24 subnet has 8 host bits (2^8 = 256 addresses); subtracting network address (0) and broadcast address (255) gives 254 usable hosts."
    },
    {
        "difficulty": "Medium",
        "question": "What is Network Address Translation (NAT)?",
        "options": ["A method that maps multiple private IP addresses in a local LAN to a single public IP address for Internet access", "A routing protocol for fiber cables", "A protocol for assigning domain names", "An encryption algorithm for Wi-Fi"],
        "answer": "A method that maps multiple private IP addresses in a local LAN to a single public IP address for Internet access",
        "explanation": "NAT (or NAPT) modifies IP headers in transit to enable private networks (RFC 1918) to share public IP addresses."
    },
    {
        "difficulty": "Medium",
        "question": "What are the four phases of the TCP Congestion Control algorithm?",
        "options": ["Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery", "Init, Run, Pause, Stop", "Syn, Ack, Fin, Reset", "Listen, Speak, Wait, Repeat"],
        "answer": "Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery",
        "explanation": "Standard TCP congestion control transitions through Slow Start, Congestion Avoidance (AIMD), Fast Retransmit, and Fast Recovery."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Distance Vector (e.g. RIP) and Link State (e.g. OSPF) routing protocols?",
        "options": ["Distance Vector shares routing tables with direct neighbors periodically (Bellman-Ford); Link State floods complete topology maps and runs Dijkstra", "Link state cannot scale beyond 15 hops", "Distance vector protocols use SPF trees", "They are identical in algorithm"],
        "answer": "Distance Vector shares routing tables with direct neighbors periodically (Bellman-Ford); Link State floods complete topology maps and runs Dijkstra",
        "explanation": "RIP shares vectors of distances with neighbors; OSPF maintains a complete graph of the network and computes shortest paths via Dijkstra."
    },
    {
        "difficulty": "Medium",
        "question": "What is the Count-to-Infinity problem in distance vector routing and how is it mitigated?",
        "options": ["Routing loops causing distance metrics to increment infinitely; mitigated using Split Horizon and Poison Reverse", "A buffer overflow in switches", "Infinite packet retransmission in TCP", "DNS cache poisoning"],
        "answer": "Routing loops causing distance metrics to increment infinitely; mitigated using Split Horizon and Poison Reverse",
        "explanation": "Slow convergence in Bellman-Ford causes loops incrementing hop count to infinity; Split Horizon prevents sending routes back to their source."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of the Time-to-Live (TTL) field in the IPv4 header?",
        "options": ["Prevents packets from circulating endlessly in routing loops by decrementing at each hop and dropping packet when TTL reaches 0", "Specifies packet encryption lifetime", "Measures client download speed", "Indicates HTTP cookie expiry"],
        "answer": "Prevents packets from circulating endlessly in routing loops by decrementing at each hop and dropping packet when TTL reaches 0",
        "explanation": "Each router decrements TTL by 1; when TTL hits 0, the router discards the packet and sends an ICMP Time Exceeded message."
    },
    {
        "difficulty": "Medium",
        "question": "What does the Spanning Tree Protocol (STP / IEEE 802.1D) accomplish in Ethernet switched networks?",
        "options": ["Disables redundant bridge links logically to prevent broadcast radiation loops while providing backup path failover", "Assigns IP addresses automatically", "Compresses audio/video packets", "Routes packets across the Internet"],
        "answer": "Disables redundant bridge links logically to prevent broadcast radiation loops while providing backup path failover",
        "explanation": "STP builds a loop-free logical tree topology across Layer 2 switches by placing redundant ports into blocking state."
    },
    {
        "difficulty": "Medium",
        "question": "What is CSMA/CD used for in legacy half-duplex Ethernet networks?",
        "options": ["Carrier Sense Multiple Access with Collision Detection to manage shared medium access and detect collisions", "Encrypting WiFi frames", "Modulating analog signals on fiber", "Compressing HTTP payloads"],
        "answer": "Carrier Sense Multiple Access with Collision Detection to manage shared medium access and detect collisions",
        "explanation": "CSMA/CD listens before transmitting, detects simultaneous transmissions (collisions), aborts, and waits a random exponential backoff time."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between TCP Flow Control and TCP Congestion Control?",
        "options": ["Flow Control prevents sender from overwhelming receiver buffer (Receiver Window); Congestion Control prevents sender from overwhelming network intermediate links (Congestion Window)", "Flow control manages routers; Congestion control manages client RAM", "They are two names for the same algorithm", "Flow control is handled by UDP"],
        "answer": "Flow Control prevents sender from overwhelming receiver buffer (Receiver Window); Congestion Control prevents sender from overwhelming network intermediate links (Congestion Window)",
        "explanation": "Flow control protects the receiver end-host using `rwnd`; congestion control protects intermediate network routers using `cwnd`."
    },
    {
        "difficulty": "Medium",
        "question": "What is Border Gateway Protocol (BGP)?",
        "options": ["The standard Path-Vector exterior gateway protocol used for routing traffic between Autonomous Systems (AS) across the global Internet", "An interior routing protocol for small home offices", "A protocol for assigning MAC addresses", "A wireless mesh routing algorithm"],
        "answer": "The standard Path-Vector exterior gateway protocol used for routing traffic between Autonomous Systems (AS) across the global Internet",
        "explanation": "BGP is the core routing protocol that binds the Internet together by making policy-based routing decisions between distinct Autonomous Systems."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of the Sliding Window mechanism in TCP?",
        "options": ["Allows multiple packet segments to be sent without waiting for an individual ACK for every single packet, maximizing bandwidth utilization", "Resizes browser windows during video streaming", "Filters firewall packets", "Compresses TCP headers"],
        "answer": "Allows multiple packet segments to be sent without waiting for an individual ACK for every single packet, maximizing bandwidth utilization",
        "explanation": "Sliding window enables pipelining of multiple frames/packets within a window size, improving throughput over high-latency links."
    },
    {
        "difficulty": "Medium",
        "question": "What is the maximum payload size (Maximum Transmission Unit - MTU) of standard Ethernet frame?",
        "options": ["1024 bytes", "1500 bytes", "4096 bytes", "65535 bytes"],
        "answer": "1500 bytes",
        "explanation": "Standard Ethernet MTU is 1500 bytes; packets larger than this must undergo IP fragmentation unless Jumbo Frames are enabled."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Symmetric and Asymmetric encryption in network security protocols (TLS/SSL)?",
        "options": ["Symmetric uses the same shared key for encryption and decryption; Asymmetric uses a public key to encrypt and private key to decrypt", "Asymmetric is much faster than symmetric", "Symmetric does not require keys", "Asymmetric is used for streaming bulk video files"],
        "answer": "Symmetric uses the same shared key for encryption and decryption; Asymmetric uses a public key to encrypt and private key to decrypt",
        "explanation": "Asymmetric encryption (e.g. RSA, ECC) is used to authenticate and negotiate a shared session key, which symmetric ciphers (AES) then use for high-speed bulk data transfer."
    },
    {
        "difficulty": "Medium",
        "question": "What happens during a TCP FIN four-way teardown handshake?",
        "options": ["Both endpoints send FIN and acknowledge with ACK independently to cleanly close full-duplex transmission", "The server abruptly drops the socket", "A reset (RST) packet wipes router caches", "The client sends a DNS unregister request"],
        "answer": "Both endpoints send FIN and acknowledge with ACK independently to cleanly close full-duplex transmission",
        "explanation": "Because TCP is full-duplex, each side must send a FIN and receive an ACK to close its half of the connection."
    },
    {
        "difficulty": "Medium",
        "question": "What is the primary difference between HTTP/1.1 and HTTP/2?",
        "options": ["HTTP/2 supports multiplexing multiple requests/responses over a single TCP connection in binary format and header compression (HPACK)", "HTTP/2 requires UDP protocol exclusively", "HTTP/1.1 is fully encrypted by default", "HTTP/2 does not support cookies"],
        "answer": "HTTP/2 supports multiplexing multiple requests/responses over a single TCP connection in binary format and header compression (HPACK)",
        "explanation": "HTTP/2 introduces binary framing, multiplexing over a single TCP connection to eliminate Head-of-Line blocking at application layer, and HPACK header compression."
    },
    {
        "difficulty": "Medium",
        "question": "What transport layer protocol does QUIC (the basis for HTTP/3) run over?",
        "options": ["TCP", "UDP", "SCTP", "Raw IP"],
        "answer": "UDP",
        "explanation": "HTTP/3 uses QUIC running on top of UDP to achieve zero-RTT handshakes and eliminate TCP Head-of-Line blocking."
    },
    {
        "difficulty": "Medium",
        "question": "What is VLAN (Virtual Local Area Network) Tagging (IEEE 802.1Q)?",
        "options": ["Inserting a 4-byte header into Ethernet frames containing a VLAN ID (1-4094) to partition physical switches into multiple logical broadcast domains", "Assigning names to Wi-Fi access points", "Encrypting Layer 2 packets", "Configuring firewall ACLs"],
        "answer": "Inserting a 4-byte header into Ethernet frames containing a VLAN ID (1-4094) to partition physical switches into multiple logical broadcast domains",
        "explanation": "802.1Q inserts a VLAN tag into Ethernet frames, allowing multiple isolated virtual networks to share common trunk links."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of Port Address Translation (PAT / NAT Overload)?",
        "options": ["Mapping thousands of internal private host connections to a single public IP using unique source port numbers", "Translating HTTP port 80 to 443", "Opening router admin console", "Assigning static IPs to printers"],
        "answer": "Mapping thousands of internal private host connections to a single public IP using unique source port numbers",
        "explanation": "PAT tracks TCP/UDP source ports to multiplex thousands of internal hosts onto one single routable public IP."
    },

    # Hard (10)
    {
        "difficulty": "Hard",
        "question": "What is the BGP Path Selection algorithm order of precedence?",
        "options": ["Highest Weight -> Highest Local Preference -> Locally Originated -> Shortest AS_PATH -> Lowest Origin Type -> Lowest MED -> eBGP over iBGP", "Shortest AS_PATH -> Lowest Port -> Random", "Lowest IP address -> First received", "Fastest ping response time"],
        "answer": "Highest Weight -> Highest Local Preference -> Locally Originated -> Shortest AS_PATH -> Lowest Origin Type -> Lowest MED -> eBGP over iBGP",
        "explanation": "BGP evaluates routes through a strict deterministic tie-breaking hierarchy beginning with Weight and Local Preference."
    },
    {
        "difficulty": "Hard",
        "question": "What is TCP Selective Acknowledgment (SACK) and what performance issue does it solve?",
        "options": ["Allows receiver to inform sender of all non-contiguous segments received, avoiding retransmission of already received data when multiple packets drop", "Encrypts individual packet payloads", "Allows TCP to skip checksum computation", "Reduces connection teardown time to 0 RTT"],
        "answer": "Allows receiver to inform sender of all non-contiguous segments received, avoiding retransmission of already received data when multiple packets drop",
        "explanation": "SACK provides explicit blocks of successfully received packets, enabling precise retransmission of only dropped segments."
    },
    {
        "difficulty": "Hard",
        "question": "What is the Silly Window Syndrome in TCP and how is Nagle's Algorithm paired with Clark's Solution to fix it?",
        "options": ["Sender transmits tiny 1-byte payloads in full TCP headers; Nagle buffers small outgoing chunks until full MSS or ACK received, while Clark prevents receiver from advertising tiny window updates", "A buffer overflow in switches", "A bug in DNS resolution", "A deadlock in 3-way handshake"],
        "answer": "Sender transmits tiny 1-byte payloads in full TCP headers; Nagle buffers small outgoing chunks until full MSS or ACK received, while Clark prevents receiver from advertising tiny window updates",
        "explanation": "Silly Window Syndrome creates extreme header overhead; Nagle solves it sender-side by coalescing small packets, and Clark solves it receiver-side."
    },
    {
        "difficulty": "Hard",
        "question": "What is Multiprotocol Label Switching (MPLS)?",
        "options": ["A high-performance routing technique that forwards packets based on short fixed-length Layer 2.5 labels rather than inspecting long IP routing tables", "A protocol for sending multi-part emails", "A VPN protocol for home routers", "A WiFi mesh protocol"],
        "answer": "A high-performance routing technique that forwards packets based on short fixed-length Layer 2.5 labels rather than inspecting long IP routing tables",
        "explanation": "MPLS places label tags between Layer 2 and Layer 3 headers, allowing label-switched routers (LSR) to forward packets with fast index lookups."
    },
    {
        "difficulty": "Hard",
        "question": "What is Bufferbloat in network routers?",
        "options": ["Excessive buffering of packets in intermediate routers causing high latency and packet delay variation (jitter) under load", "Corrupting packet data buffers", "Overallocating RAM in client browsers", "Stack overflow in network drivers"],
        "answer": "Excessive buffering of packets in intermediate routers causing high latency and packet delay variation (jitter) under load",
        "explanation": "Bufferbloat occurs when oversized router queues prevent TCP congestion mechanisms from dropping packets timely, spiking round-trip latency."
    },
    {
        "difficulty": "Hard",
        "question": "What is the purpose of Active Queue Management algorithms like CoDel (Controlled Delay) and RED (Random Early Detection)?",
        "options": ["Dropping or marking packets proactively before router buffers fill to signal TCP senders to slow down and maintain low latency", "Sorting incoming packets alphabetically", "Prioritizing gaming packets over video", "Balancing CPU temperature"],
        "answer": "Dropping or marking packets proactively before router buffers fill to signal TCP senders to slow down and maintain low latency",
        "explanation": "AQM algorithms drop packets early to trigger TCP congestion backoff before buffers saturate, preventing bufferbloat."
    },
    {
        "difficulty": "Hard",
        "question": "What is Anycast routing?",
        "options": ["A network addressing and routing methodology where a single destination IP address is shared by multiple physical routing endpoints, routing requests to the topologically nearest node", "Broadcasting to every device worldwide", "Unicasting to satellite dishes", "Sending frames to all VLANs"],
        "answer": "A network addressing and routing methodology where a single destination IP address is shared by multiple physical routing endpoints, routing requests to the topologically nearest node",
        "explanation": "Anycast allows multiple servers (e.g. root DNS, Cloudflare CDNs) to announce the same IP over BGP, directing users to the closest point of presence."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between TCP BBR (Bottleneck Bandwidth and RTT) and loss-based congestion control like Reno/Cubic?",
        "options": ["BBR models the network pipeline to maximize throughput and minimize delay without relying on packet loss as a primary signal of congestion", "BBR only runs on local networks", "Cubic runs over UDP", "BBR requires changes to all intermediate routers"],
        "answer": "BBR models the network pipeline to maximize throughput and minimize delay without relying on packet loss as a primary signal of congestion",
        "explanation": "BBR estimates delivery rate and minimum RTT to keep the bottleneck link full without inflating packet queues."
    },
    {
        "difficulty": "Hard",
        "question": "What is DNSSEC (Domain Name System Security Extensions)?",
        "options": ["A suite of specifications providing cryptographic authentication of DNS data to prevent DNS spoofing and cache poisoning", "An SSL certificate for domain registrars", "A hardware firewall for DNS servers", "A protocol to block adult websites"],
        "answer": "A suite of specifications providing cryptographic authentication of DNS data to prevent DNS spoofing and cache poisoning",
        "explanation": "DNSSEC uses digital signatures (RRSIG, DNSKEY, DS records) to authenticate the origin and integrity of DNS query responses."
    },
    {
        "difficulty": "Hard",
        "question": "What is DiffServ (Differentiated Services) in Quality of Service (QoS)?",
        "options": ["A scalable architecture that classifies and marks IP packets using the DSCP (Differentiated Services Code Point) 6-bit field for per-hop treatment", "A load balancing algorithm for web servers", "A network backup scheduling service", "A wireless frequency multiplexing technique"],
        "answer": "A scalable architecture that classifies and marks IP packets using the DSCP (Differentiated Services Code Point) 6-bit field for per-hop treatment",
        "explanation": "DiffServ marks packets at the edge with DSCP codes, enabling core routers to apply priority forwarding without maintaining per-flow state."
    }
]
