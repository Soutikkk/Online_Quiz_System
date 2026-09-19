CATEGORY = "Computer Organization & Architecture"

QUESTIONS = [
    # Easy (16)
    {
        "difficulty": "Easy",
        "question": "What is the primary function of the Arithmetic Logic Unit (ALU)?",
        "options": ["Performing arithmetic operations and logical decisions", "Storing permanent OS files", "Managing network connections", "Generating video display signals"],
        "answer": "Performing arithmetic operations and logical decisions",
        "explanation": "The ALU is the digital circuit within the CPU that executes arithmetic (add, subtract) and logical (AND, OR, NOT) operations."
    },
    {
        "difficulty": "Easy",
        "question": "Which CPU register holds the memory address of the next instruction to be fetched and executed?",
        "options": ["Program Counter (PC)", "Instruction Register (IR)", "Memory Data Register (MDR)", "Accumulator (ACC)"],
        "answer": "Program Counter (PC)",
        "explanation": "The Program Counter (PC) stores the memory address of the next instruction to be fetched in the instruction cycle."
    },
    {
        "difficulty": "Easy",
        "question": "Which CPU register holds the current instruction that is being decoded and executed?",
        "options": ["Instruction Register (IR)", "Program Counter (PC)", "Memory Address Register (MAR)", "Stack Pointer (SP)"],
        "answer": "Instruction Register (IR)",
        "explanation": "The Instruction Register (IR) holds the binary opcode and operands of the instruction currently being executed."
    },
    {
        "difficulty": "Easy",
        "question": "What does RISC stand for in computer architecture?",
        "options": ["Reduced Instruction Set Computer", "Rapid Instruction System Core", "Redundant Interface Storage Chip", "Relocatable Instruction Set Controller"],
        "answer": "Reduced Instruction Set Computer",
        "explanation": "RISC stands for Reduced Instruction Set Computer, emphasizing simple instructions executed in single clock cycles."
    },
    {
        "difficulty": "Easy",
        "question": "What does CISC stand for in computer architecture?",
        "options": ["Complex Instruction Set Computer", "Central Instruction Storage Core", "Calculated Instruction Serial Chip", "Compact Integrated System Circuit"],
        "answer": "Complex Instruction Set Computer",
        "explanation": "CISC stands for Complex Instruction Set Computer, supporting multi-clock cycle instructions capable of complex multi-step operations."
    },
    {
        "difficulty": "Easy",
        "question": "Which memory level in the computer hierarchy is the fastest and closest to the CPU execution core?",
        "options": ["CPU Registers", "L1 Cache", "Main RAM", "Solid State Drive"],
        "answer": "CPU Registers",
        "explanation": "Registers reside directly inside the CPU core and offer sub-nanosecond single-cycle access speeds."
    },
    {
        "difficulty": "Easy",
        "question": "What is Von Neumann Architecture characterized by?",
        "options": ["Shared memory and bus for both program instructions and data", "Completely separate physical memories for instructions and data", "Absence of an Arithmetic Logic Unit", "Purely analog processing circuits"],
        "answer": "Shared memory and bus for both program instructions and data",
        "explanation": "The Von Neumann architecture stores both program code and data in the same unified physical memory."
    },
    {
        "difficulty": "Easy",
        "question": "What is Harvard Architecture characterized by?",
        "options": ["Physically separate storage and signal pathways for instructions and data", "Unified memory bus for code and data", "Eliminating cache memory", "Having no control unit"],
        "answer": "Physically separate storage and signal pathways for instructions and data",
        "explanation": "Harvard architecture uses physically separate memories and buses for program instructions and data."
    },
    {
        "difficulty": "Easy",
        "question": "What are the three fundamental phases of the basic CPU execution cycle?",
        "options": ["Fetch, Decode, Execute", "Compile, Link, Load", "Read, Write, Erase", "Interrupt, Poll, Return"],
        "answer": "Fetch, Decode, Execute",
        "explanation": "The CPU repeats the Fetch-Decode-Execute cycle continuously to run instructions."
    },
    {
        "difficulty": "Easy",
        "question": "What type of memory is volatile and loses its content when power is turned off?",
        "options": ["RAM (Random Access Memory)", "ROM (Read Only Memory)", "Hard Disk", "Flash EEPROM"],
        "answer": "RAM (Random Access Memory)",
        "explanation": "Dynamic and Static RAM require continuous power to retain stored bits, making them volatile."
    },
    {
        "difficulty": "Easy",
        "question": "What is the primary function of the Control Unit (CU) in a processor?",
        "options": ["Directing and coordinating operations of hardware by generating timing and control signals", "Performing floating point multiplication", "Storing user database files", "Cooling the CPU heatsink"],
        "answer": "Directing and coordinating operations of hardware by generating timing and control signals",
        "explanation": "The Control Unit decodes instructions and orchestrates the flow of data through the ALU, registers, and buses."
    },
    {
        "difficulty": "Easy",
        "question": "What is a system bus composed of?",
        "options": ["Data Bus, Address Bus, Control Bus", "PCI Bus, USB, SATA", "Fiber, Coaxial, Twisted Pair", "Input Bus, Output Bus, Screen Bus"],
        "answer": "Data Bus, Address Bus, Control Bus",
        "explanation": "The system bus consists of the Address Bus (location), Data Bus (payload), and Control Bus (read/write signals)."
    },
    {
        "difficulty": "Easy",
        "question": "What is Pipelining in processor architecture?",
        "options": ["Overlapping the execution of multiple instructions across successive stages simultaneously", "Cooling CPU using liquid pipes", "Connecting multiple computers via LAN", "Writing data directly to disk"],
        "answer": "Overlapping the execution of multiple instructions across successive stages simultaneously",
        "explanation": "Pipelining divides instruction execution into stages (e.g. IF, ID, EX, MEM, WB) running in parallel like an assembly line."
    },
    {
        "difficulty": "Easy",
        "question": "Which cache level is typically smallest, fastest, and integrated directly into each processor core?",
        "options": ["L1 Cache", "L2 Cache", "L3 Cache", "RAM"],
        "answer": "L1 Cache",
        "explanation": "Level 1 (L1) cache is the fastest on-die SRAM cache closest to the CPU execution units."
    },
    {
        "difficulty": "Easy",
        "question": "What is an Interrupt in computer systems?",
        "options": ["A hardware or software signal indicating an event that needs immediate attention from the CPU", "A short circuit in the power supply", "A syntax error in code", "A broken network cable"],
        "answer": "A hardware or software signal indicating an event that needs immediate attention from the CPU",
        "explanation": "An interrupt suspends the current CPU execution sequence to run an Interrupt Service Routine (ISR)."
    },
    {
        "difficulty": "Easy",
        "question": "What is Cache Hit and Cache Miss?",
        "options": ["Cache Hit means requested data is found in cache; Cache Miss means data must be fetched from slower lower-level memory", "Cache Hit is an error; Cache Miss is a success", "Cache Hit deletes the cache", "They refer to internet web browser caching only"],
        "answer": "Cache Hit means requested data is found in cache; Cache Miss means data must be fetched from slower lower-level memory",
        "explanation": "A cache hit satisfies the memory request immediately from fast SRAM; a miss causes latency to fetch from main DRAM."
    },

    # Medium (16)
    {
        "difficulty": "Medium",
        "question": "What are the three major types of Pipeline Hazards in computer architecture?",
        "options": ["Structural, Data, and Control hazards", "Memory, Disk, and CPU hazards", "Compiler, Assembler, and Linker hazards", "Voltage, Clock, and Thermal hazards"],
        "answer": "Structural, Data, and Control hazards",
        "explanation": "Pipeline hazards that prevent continuous single-cycle execution include Structural (hardware conflicts), Data (dependencies like RAW), and Control (branching)."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Read-After-Write (RAW) data hazard?",
        "options": ["When an instruction depends on the result of a previous instruction that has not yet completed its write-back stage", "When two writes happen simultaneously", "When reading uninitialized memory", "When cache is cleared during write"],
        "answer": "When an instruction depends on the result of a previous instruction that has not yet completed its write-back stage",
        "explanation": "RAW (true dependency) occurs when instruction j tries to read a source register before instruction i has written to it."
    },
    {
        "difficulty": "Medium",
        "question": "What is Operand Forwarding (Bypassing) in pipelined processors?",
        "options": ["Routing intermediate execution results directly from ALU output stages to subsequent instruction inputs without waiting for register write-back", "Forwarding emails over network", "Skipping conditional branches", "Passing arguments to stack"],
        "answer": "Routing intermediate execution results directly from ALU output stages to subsequent instruction inputs without waiting for register write-back",
        "explanation": "Operand forwarding feeds the computed result directly from ALU output buffers back into the ALU inputs of subsequent stages to resolve RAW hazards without stalling."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Direct-Mapped, Set-Associative, and Fully-Associative cache mapping?",
        "options": ["Direct mapped has 1 block per set; Set-associative has N blocks per set; Fully associative allows blocks to reside in any cache line", "Direct mapped allows any line placement", "Fully associative has highest conflict misses", "Set associative cannot be used in L2 cache"],
        "answer": "Direct mapped has 1 block per set; Set-associative has N blocks per set; Fully associative allows blocks to reside in any cache line",
        "explanation": "Direct-mapped maps each block to exactly 1 line; N-way set-associative maps to N lines in a set; fully-associative maps to any position in cache."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Write-Through and Write-Back cache write policies?",
        "options": ["Write-Through writes data to both cache and main RAM simultaneously; Write-Back updates RAM only when dirty block is evicted", "Write-Back writes to RAM immediately", "Write-Through does not update cache", "They are identical in speed"],
        "answer": "Write-Through writes data to both cache and main RAM simultaneously; Write-Back updates RAM only when dirty block is evicted",
        "explanation": "Write-through ensures consistency by updating lower memory immediately; write-back reduces memory bus traffic by writing back only modified dirty blocks upon eviction."
    },
    {
        "difficulty": "Medium",
        "question": "What is Branch Prediction in modern out-of-order processors?",
        "options": ["A technique predicting whether a conditional branch will be taken before it is evaluated, allowing speculative instruction execution", "Choosing which thread to kill", "Selecting memory bus frequency", "Balancing CPU power consumption"],
        "answer": "A technique predicting whether a conditional branch will be taken before it is evaluated, allowing speculative instruction execution",
        "explanation": "Branch prediction speculatively fetches and executes instructions down the predicted path to prevent pipeline branch penalty stalls."
    },
    {
        "difficulty": "Medium",
        "question": "What is Amdahl's Law used to calculate?",
        "options": ["The theoretical maximum speedup of a program when using multiple parallel processors with a fixed serial portion", "The power dissipation of transistors", "The latency of cache access", "The bandwidth of hard drives"],
        "answer": "The theoretical maximum speedup of a program when using multiple parallel processors with a fixed serial portion",
        "explanation": "Amdahl's law defines speedup `S(N) = 1 / ((1 - P) + P / N)`, showing performance is bounded by the sequential serial fraction `(1 - P)`."
    },
    {
        "difficulty": "Medium",
        "question": "What is Micro-programming in Control Unit design?",
        "options": ["Implementing the control unit by storing micro-instructions (control words) in a specialized Control ROM rather than hardwired combinational logic", "Programming in 8-bit assembly", "Writing small Python scripts", "Programming microcontroller firmware"],
        "answer": "Implementing the control unit by storing micro-instructions (control words) in a specialized Control ROM rather than hardwired combinational logic",
        "explanation": "Microprogrammed control units fetch microcode sequences from control memory to generate control signals, offering high flexibility over hardwired logic."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Spatial Locality and Temporal Locality of reference?",
        "options": ["Spatial locality: accessing memory near recently accessed memory; Temporal locality: accessing the same memory location repeatedly in near future", "Temporal refers to disk; Spatial refers to network", "They describe pipeline stages", "They are identical"],
        "answer": "Spatial locality: accessing memory near recently accessed memory; Temporal locality: accessing the same memory location repeatedly in near future",
        "explanation": "Temporal locality exploits repeated access to the same data (loops); spatial locality exploits sequential array/code access within the same cache line."
    },
    {
        "difficulty": "Medium",
        "question": "What is Memory-Mapped I/O versus Isolated (Port-Mapped) I/O?",
        "options": ["Memory-Mapped uses identical address space and instructions for both RAM and I/O devices; Isolated I/O uses separate I/O address space and dedicated instructions (like IN/OUT)", "Memory mapped requires external graphics cards", "Isolated I/O does not use registers", "They have identical hardware wiring"],
        "answer": "Memory-Mapped uses identical address space and instructions for both RAM and I/O devices; Isolated I/O uses separate I/O address space and dedicated instructions (like IN/OUT)",
        "explanation": "In memory-mapped I/O, device registers appear as standard memory addresses; port-mapped I/O (e.g. x86 IN/OUT) uses dedicated bus control lines."
    },
    {
        "difficulty": "Medium",
        "question": "What is SIMD (Single Instruction, Multiple Data) in Flynn's taxonomy?",
        "options": ["An architecture where a single instruction operates on multiple data points simultaneously (vector processing / GPU shaders)", "A multi-processor cluster", "A single-core serial processor", "An instruction with multiple opcodes"],
        "answer": "An architecture where a single instruction operates on multiple data points simultaneously (vector processing / GPU shaders)",
        "explanation": "SIMD performs identical arithmetic operations across parallel vector registers (e.g. AVX, SSE, GPUs) in a single instruction cycle."
    },
    {
        "difficulty": "Medium",
        "question": "What is the Von Neumann Bottleneck?",
        "options": ["The throughput limit imposed by the shared bus between CPU and main memory, which is significantly slower than CPU processing rate", "A bug in compiler parsing", "Overheating of the ALU", "Lack of register storage"],
        "answer": "The throughput limit imposed by the shared bus between CPU and main memory, which is significantly slower than CPU processing rate",
        "explanation": "The Von Neumann bottleneck refers to CPU idle time waiting for instruction/data transfer over the relatively slow memory bus."
    },
    {
        "difficulty": "Medium",
        "question": "What is an Addressing Mode in machine instructions?",
        "options": ["The method by which the operand's effective memory address is calculated (e.g., immediate, direct, indirect, indexed)", "The MAC address of CPU", "The IP address of the motherboard", "The compiler output format"],
        "answer": "The method by which the operand's effective memory address is calculated (e.g., immediate, direct, indirect, indexed)",
        "explanation": "Addressing modes specify how machine instructions identify where operands reside (in registers, immediate values, or calculated memory addresses)."
    },
    {
        "difficulty": "Medium",
        "question": "What is Booth's Multiplication Algorithm?",
        "options": ["An algorithm for multiplying signed binary numbers in two's complement representation by encoding strings of consecutive 1s", "A division algorithm for floating points", "A square root calculation", "A base-10 adder design"],
        "answer": "An algorithm for multiplying signed binary numbers in two's complement representation by encoding strings of consecutive 1s",
        "explanation": "Booth's algorithm accelerates signed two's complement multiplication by treating consecutive ones as a subtraction and addition."
    },
    {
        "difficulty": "Medium",
        "question": "What is the 3C model of cache misses?",
        "options": ["Compulsory (cold start), Capacity (cache too small), and Conflict (set collision) misses", "Core, Chip, and Circuit misses", "Control, Calculation, and Check misses", "Compile, Create, and Connect misses"],
        "answer": "Compulsory (cold start), Capacity (cache too small), and Conflict (set collision) misses",
        "explanation": "Hill's 3C model categorizes cache misses into Compulsory (first access), Capacity (working set > cache size), and Conflict (mapping collisions)."
    },
    {
        "difficulty": "Medium",
        "question": "What is DMA Cycle Stealing?",
        "options": ["When the DMA controller takes control of the system bus for one bus cycle at a time, momentarily pausing CPU memory access", "When CPU steals clock cycles from GPU", "When RAM is unmounted", "When interrupts are dropped"],
        "answer": "When the DMA controller takes control of the system bus for one bus cycle at a time, momentarily pausing CPU memory access",
        "explanation": "Cycle stealing allows the DMA controller to transfer one word per bus cycle intermingled with CPU bus cycles without monopolizing the bus."
    },

    # Hard (8)
    {
        "difficulty": "Hard",
        "question": "What is the Tomasulo Algorithm used for in high-performance superscalar processors?",
        "options": ["Hardware dynamic instruction scheduling and register renaming using Reservation Stations to enable out-of-order execution and eliminate WAR/WAW hazards", "Software compiler optimization for loops", "Thermal throttling of CPU cores", "Branch prediction state machine"],
        "answer": "Hardware dynamic instruction scheduling and register renaming using Reservation Stations to enable out-of-order execution and eliminate WAR/WAW hazards",
        "explanation": "Tomasulo tracks operand readiness in reservation stations and broadcasts computed results across a Common Data Bus (CDB) to execute instructions out-of-order."
    },
    {
        "difficulty": "Hard",
        "question": "What is the MESI protocol used for in multi-core shared memory systems?",
        "options": ["Maintaining Cache Coherence across private L1/L2 caches using states: Modified, Exclusive, Shared, and Invalid", "Balancing thread workloads", "Paging virtual memory across sockets", "Encoding GPU instructions"],
        "answer": "Maintaining Cache Coherence across private L1/L2 caches using states: Modified, Exclusive, Shared, and Invalid",
        "explanation": "MESI is a hardware snooping cache coherence protocol ensuring all CPU cores observe consistent views of shared memory."
    },
    {
        "difficulty": "Hard",
        "question": "What is the purpose of the Reorder Buffer (ROB) in modern out-of-order processors?",
        "options": ["Ensuring that out-of-order executed instructions commit their results in strict original program order, supporting precise interrupt handling", "Buffering disk reads", "Reordering bytes for Big Endian architectures", "Sorting memory addresses"],
        "answer": "Ensuring that out-of-order executed instructions commit their results in strict original program order, supporting precise interrupt handling",
        "explanation": "The ROB holds speculative execution results and commits them in-order to the architectural register state upon retirement, preserving precise exceptions."
    },
    {
        "difficulty": "Hard",
        "question": "What is Simultaneous Multi-Threading (SMT / Hyper-Threading)?",
        "options": ["Allowing multiple independent architectural hardware threads to issue instructions to a single core's execution units in the same clock cycle", "Running dual operating systems", "Doubling CPU physical silicon cores", "Running two programs over network"],
        "answer": "Allowing multiple independent architectural hardware threads to issue instructions to a single core's execution units in the same clock cycle",
        "explanation": "SMT duplicates architectural register state so multiple threads can utilize execution units that would otherwise sit idle during memory stalls."
    },
    {
        "difficulty": "Hard",
        "question": "What is Non-Uniform Memory Access (NUMA) architecture?",
        "options": ["A multi-processor memory design where access time depends on the memory region's physical proximity to the accessing CPU core", "A memory that changes speed randomly", "Memory with unaligned byte addresses", "Memory without cache hierarchy"],
        "answer": "A multi-processor memory design where access time depends on the memory region's physical proximity to the accessing CPU core",
        "explanation": "In NUMA systems, each multi-core socket has local memory with fast low-latency access, while accessing remote socket memory incurs interconnect delay."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between VLIW (Very Long Instruction Word) and Superscalar architectures?",
        "options": ["VLIW relies on the static software compiler to bundle independent parallel operations into one wide word; Superscalar uses dynamic runtime hardware logic to detect parallelism", "Superscalar requires manual assembly bundling", "VLIW is used in all standard x86 consumer CPUs", "VLIW has zero pipelines"],
        "answer": "VLIW relies on the static software compiler to bundle independent parallel operations into one wide word; Superscalar uses dynamic runtime hardware logic to detect parallelism",
        "explanation": "VLIW shifts the burden of scheduling instruction-level parallelism to the compiler, eliminating complex dynamic hazard hardware in the CPU core."
    },
    {
        "difficulty": "Hard",
        "question": "What is False Sharing in multi-threaded multi-core computing?",
        "options": ["When threads on different cores modify independent variables that happen to reside on the same shared cache line, causing continuous cache invalidation thrashing", "When two processes share the same file descriptor", "When virtual memory maps to bad RAM", "When passwords are shared across networks"],
        "answer": "When threads on different cores modify independent variables that happen to reside on the same shared cache line, causing continuous cache invalidation thrashing",
        "explanation": "False sharing occurs when independent variables share a single 64-byte cache line, forcing cores to constantly bounce ownership of the cache line via MESI."
    },
    {
        "difficulty": "Hard",
        "question": "What is Speculative Execution and how did vulnerabilities like Spectre exploit it?",
        "options": ["CPUs execute branch instructions ahead of time based on predictions; Spectre extracted secrets by observing microarchitectural cache side-effects left by transiently executed speculative instructions", "A hardware overclocking failure", "A stack overflow in kernel drivers", "A BIOS flashing corruption"],
        "answer": "CPUs execute branch instructions ahead of time based on predictions; Spectre extracted secrets by observing microarchitectural cache side-effects left by transiently executed speculative instructions",
        "explanation": "Speculative instructions that are squashed still modify the L1/L2 cache state, allowing attackers to reconstruct unauthorized memory contents via side-channel timing."
    }
]
