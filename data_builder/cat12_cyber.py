CATEGORY = "Cyber Security"

QUESTIONS = [
    # Easy (10)
    {
        "difficulty": "Easy",
        "question": "What is the CIA Triad in information security?",
        "options": ["Confidentiality, Integrity, Availability", "Control, Inspection, Authentication", "Cryptographic Information Algorithm", "Central Intelligence Agency"],
        "answer": "Confidentiality, Integrity, Availability",
        "explanation": "The CIA Triad (Confidentiality, Integrity, Availability) represents the foundational model for security policies and controls."
    },
    {
        "difficulty": "Easy",
        "question": "What is Phishing in cybersecurity?",
        "options": ["A social engineering attack where attackers impersonate legitimate entities to deceive victims into revealing sensitive credentials or data", "Scanning open ports on a firewall", "Overclocking CPU processors", "Cracking passwords via brute force"],
        "answer": "A social engineering attack where attackers impersonate legitimate entities to deceive victims into revealing sensitive credentials or data",
        "explanation": "Phishing relies on deceptive emails or fraudulent websites to trick users into divulging passwords, credit card numbers, or MFA tokens."
    },
    {
        "difficulty": "Easy",
        "question": "What is Malware that encrypts a victim's files and demands payment to restore access called?",
        "options": ["Ransomware", "Spyware", "Adware", "Worm"],
        "answer": "Ransomware",
        "explanation": "Ransomware uses strong asymmetric/symmetric encryption to lock victim files and demands ransom payment (often in cryptocurrency) for decryption keys."
    },
    {
        "difficulty": "Easy",
        "question": "What does a Firewall do in network security?",
        "options": ["Monitors and filters incoming and outgoing network traffic based on predetermined security rules", "Increases internet broadband speed", "Cools down data center servers", "Encrypts local hard drives"],
        "answer": "Monitors and filters incoming and outgoing network traffic based on predetermined security rules",
        "explanation": "A firewall acts as a security barrier between a trusted internal network and untrusted external networks (the Internet)."
    },
    {
        "difficulty": "Easy",
        "question": "What does MFA stand for in access control?",
        "options": ["Multi-Factor Authentication", "Main File Access", "Master Firewall Algorithm", "Multiple Frame Array"],
        "answer": "Multi-Factor Authentication",
        "explanation": "MFA requires users to provide two or more verification factors (something you know, something you have, something you are) to gain system access."
    },
    {
        "difficulty": "Easy",
        "question": "What is a Denial of Service (DoS) attack?",
        "options": ["An attack aimed at making a machine or network resource unavailable to its intended users by overwhelming it with bogus traffic", "Stealing user passwords from a database", "Modifying source code repositories", "Intercepting Wi-Fi passwords"],
        "answer": "An attack aimed at making a machine or network resource unavailable to its intended users by overwhelming it with bogus traffic",
        "explanation": "DoS attacks flood targets with bogus requests or exploit vulnerabilities to deplete memory, bandwidth, or CPU resources, causing service outage."
    },
    {
        "difficulty": "Easy",
        "question": "What is a Computer Worm?",
        "options": ["A standalone malware program that replicates itself autonomously to spread to other computers across networks without needing a host file", "A virus that attaches to PDF files only", "A hardware component on a motherboard", "An open-source debugger"],
        "answer": "A standalone malware program that replicates itself autonomously to spread to other computers across networks without needing a host file",
        "explanation": "Unlike viruses that require user execution of host files, worms replicate independently across network vulnerabilities."
    },
    {
        "difficulty": "Easy",
        "question": "What is a Trojan Horse in computer security?",
        "options": ["A type of malware disguised as legitimate or useful software to trick users into installing it", "A hardware device inserted into USB ports", "An encryption key algorithm", "A strong password generator"],
        "answer": "A type of malware disguised as legitimate or useful software to trick users into installing it",
        "explanation": "Trojan horses masquerade as benign utilities, games, or updates while executing malicious payloads in the background."
    },
    {
        "difficulty": "Easy",
        "question": "What is SQL Injection (SQLi)?",
        "options": ["A code injection technique where malicious SQL statements are inserted into entry fields for execution by the backend database", "A method to optimize SQL queries", "A database backup procedure", "A technique to create primary keys"],
        "answer": "A code injection technique where malicious SQL statements are inserted into entry fields for execution by the backend database",
        "explanation": "SQLi exploits improper input sanitization to execute arbitrary SQL commands, bypassing authentication or reading confidential records."
    },
    {
        "difficulty": "Easy",
        "question": "What does VPN stand for?",
        "options": ["Virtual Private Network", "Visual Processing Node", "Verified Port Network", "Variable Packet Number"],
        "answer": "Virtual Private Network",
        "explanation": "A Virtual Private Network (VPN) creates an encrypted tunnel across public networks to secure communication and shield user activity."
    },

    # Medium (10)
    {
        "difficulty": "Medium",
        "question": "What is Cross-Site Scripting (XSS)?",
        "options": ["A vulnerability that enables attackers to inject malicious client-side scripts (JavaScript) into web pages viewed by other users", "A database corruption error", "A router hardware malfunction", "An attack against CPU caches"],
        "answer": "A vulnerability that enables attackers to inject malicious client-side scripts (JavaScript) into web pages viewed by other users",
        "explanation": "XSS allows attackers to execute unauthorized JavaScript in victims' browsers to hijack sessions, steal cookies, or deface websites."
    },
    {
        "difficulty": "Medium",
        "question": "What is Cross-Site Request Forgery (CSRF)?",
        "options": ["An attack that tricks an authenticated end-user into executing unwanted actions on a trusted web application where they are currently logged in", "An attack to steal database passwords via brute force", "Intercepting DNS packets", "Flooding a network with UDP packets"],
        "answer": "An attack that tricks an authenticated end-user into executing unwanted actions on a trusted web application where they are currently logged in",
        "explanation": "CSRF exploits ambient credentials (cookies) to forge state-changing HTTP requests without the victim's knowledge, mitigated by Anti-CSRF tokens and SameSite cookies."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between a Vulnerability, a Threat, and a Risk in cybersecurity?",
        "options": ["Vulnerability is a weakness in system; Threat is a potential danger that could exploit it; Risk is the probability and impact of loss if exploited", "Threat is the software bug; Vulnerability is the hacker; Risk is the cost", "They are identical synonyms", "Risk is a hardware firewall failure"],
        "answer": "Vulnerability is a weakness in system; Threat is a potential danger that could exploit it; Risk is the probability and impact of loss if exploited",
        "explanation": "Security frameworks define Risk = Threat × Vulnerability × Impact."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Man-in-the-Middle (MITM) attack and what prevents it?",
        "options": ["An attack where an adversary secretly relays and alters communication between two parties; prevented by end-to-end encryption with authenticated certificates (TLS)", "An attack where an administrator locks a user out", "A collision in hash tables", "A bug in compiler linkers"],
        "answer": "An attack where an adversary secretly relays and alters communication between two parties; prevented by end-to-end encryption with authenticated certificates (TLS)",
        "explanation": "MITM intercepts unencrypted or unauthenticated streams; TLS with verified CA certificates ensures confidentiality and party authentication."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Salt in password hashing?",
        "options": ["Random data added as additional input to a one-way password hash to safeguard against dictionary attacks and precomputed Rainbow Tables", "An encryption algorithm for Wi-Fi", "A firewall setting for blocking ports", "A temporary session cookie"],
        "answer": "Random data added as additional input to a one-way password hash to safeguard against dictionary attacks and precomputed Rainbow Tables",
        "explanation": "Salting ensures that identical passwords produce distinct hash values, nullifying precomputed lookup tables (rainbow tables)."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Zero-Day Vulnerability?",
        "options": ["A software security flaw that is unknown to the vendor and has no patch available, leaving systems open to exploitation", "A bug that occurs on day zero of project setup", "A virus that deletes files after 0 days", "An expired SSL certificate"],
        "answer": "A software security flaw that is unknown to the vendor and has no patch available, leaving systems open to exploitation",
        "explanation": "Zero-day vulnerabilities refer to unknown flaws where developers have had 'zero days' to fix the problem before attackers exploit it."
    },
    {
        "difficulty": "Medium",
        "question": "What does a Cryptographic Hash Function guarantee (e.g. SHA-256)?",
        "options": ["Deterministic output, pre-image resistance (one-way), second pre-image resistance, and collision resistance", "Reversible decryption using a public key", "Infinite compression of all input files", "Zero bit size outputs"],
        "answer": "Deterministic output, pre-image resistance (one-way), second pre-image resistance, and collision resistance",
        "explanation": "Secure hash functions map arbitrary inputs to fixed-size digests such that reversing or finding collisions is computationally infeasible."
    },
    {
        "difficulty": "Medium",
        "question": "What is the Principle of Least Privilege (PoLP)?",
        "options": ["Giving users and processes only the minimum levels of access/permissions necessary to perform their legitimate job functions", "Denying all network access to employees", "Using the lowest price firewall software", "Limiting CPU usage to 50%"],
        "answer": "Giving users and processes only the minimum levels of access/permissions necessary to perform their legitimate job functions",
        "explanation": "PoLP limits the blast radius of compromises by restricting privileges to the minimum essential scope."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Symmetric ciphers (AES) and Asymmetric ciphers (RSA/ECC) regarding key distribution?",
        "options": ["Symmetric requires sharing a secret key over a secure channel; Asymmetric allows distributing public keys freely while keeping private keys secret", "Asymmetric uses the same key for both encryption and decryption", "Symmetric does not need keys", "Asymmetric cannot encrypt text"],
        "answer": "Symmetric requires sharing a secret key over a secure channel; Asymmetric allows distributing public keys freely while keeping private keys secret",
        "explanation": "Asymmetric cryptography solves the fundamental key distribution problem by splitting key pairs into public and private keys."
    },
    {
        "difficulty": "Medium",
        "question": "What is Address Space Layout Randomization (ASLR)?",
        "options": ["A memory-protection defense that randomizes the locations of key data areas (stack, heap, libraries) in process address space to obstruct buffer overflow exploits", "A hard drive defragmentation strategy", "A DHCP IP allocation method", "A technique for sorting RAM addresses"],
        "answer": "A memory-protection defense that randomizes the locations of key data areas (stack, heap, libraries) in process address space to obstruct buffer overflow exploits",
        "explanation": "ASLR makes return-oriented programming (ROP) and memory corruption attacks difficult by randomizing memory offsets at load time."
    },

    # Hard (5)
    {
        "difficulty": "Hard",
        "question": "What is Return-Oriented Programming (ROP) exploitation?",
        "options": ["An advanced exploitation technique where an attacker chains together short existing machine code sequences ('gadgets') ending in `ret` instructions to bypass executable-space protection (DEP/NX)", "A technique for programming recursive functions", "A method for reversing compiled binaries", "A tool for recovering lost stack frames"],
        "answer": "An advanced exploitation technique where an attacker chains together short existing machine code sequences ('gadgets') ending in `ret` instructions to bypass executable-space protection (DEP/NX)",
        "explanation": "ROP reuses existing executable code sequences (gadgets) already mapped in process memory, circumventing Non-Executable (DEP/W^X) stack protections."
    },
    {
        "difficulty": "Hard",
        "question": "What is the Diffie-Hellman Key Exchange and what protects it against active eavesdropping?",
        "options": ["A cryptographic protocol allowing two parties to establish a shared secret over an insecure channel based on discrete logarithms; protected against MITM using digital signatures/certificates", "A symmetric encryption algorithm for hard drives", "A password cracking algorithm", "A protocol for hashing emails"],
        "answer": "A cryptographic protocol allowing two parties to establish a shared secret over an insecure channel based on discrete logarithms; protected against MITM using digital signatures/certificates",
        "explanation": "Diffie-Hellman (and ECDH) enables secure forward-secret shared key agreement over untrusted links, authenticated via PKI certificates."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between Forward Secrecy (Perfect Forward Secrecy - PFS) and standard key exchange?",
        "options": ["PFS generates ephemeral unique session keys for every session, ensuring that compromise of long-term server private keys cannot decrypt past recorded sessions", "PFS allows servers to predict future hacker attacks", "PFS eliminates the need for public keys", "PFS makes encryption reversible without keys"],
        "answer": "PFS generates ephemeral unique session keys for every session, ensuring that compromise of long-term server private keys cannot decrypt past recorded sessions",
        "explanation": "PFS (using Ephemeral Diffie-Hellman - DHE/ECDHE) ensures that past traffic cannot be retroactively decrypted even if the server's master private key is leaked in the future."
    },
    {
        "difficulty": "Hard",
        "question": "What is a Timing Attack in side-channel cryptanalysis?",
        "options": ["Extracting cryptographic keys or sensitive data by precisely measuring the variations in time taken to execute cryptographic operations (e.g., non-constant time string/MAC comparisons)", "Changing the system clock to bypass expiration dates", "Overclocking CPU to crack hashes faster", "Delaying packet delivery to cause timeout"],
        "answer": "Extracting cryptographic keys or sensitive data by precisely measuring the variations in time taken to execute cryptographic operations (e.g., non-constant time string/MAC comparisons)",
        "explanation": "Timing attacks exploit data-dependent execution times (such as early-exit `memcmp`), requiring constant-time cryptographic primitives."
    },
    {
        "difficulty": "Hard",
        "question": "What is the Zero Trust security model architectural principle?",
        "options": ["'Never Trust, Always Verify' — strictly verifying every user, device, and connection with least privilege access control regardless of whether they are inside or outside the corporate perimeter", "Blocking all incoming internet traffic permanently", "Eliminating passwords completely", "Disallowing all third-party software"],
        "answer": "'Never Trust, Always Verify' — strictly verifying every user, device, and connection with least privilege access control regardless of whether they are inside or outside the corporate perimeter",
        "explanation": "Zero Trust eliminates implicit trust based on network perimeter, requiring continuous dynamic authentication, authorization, and microsegmentation."
    }
]
