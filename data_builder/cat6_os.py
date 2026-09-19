CATEGORY = "Operating Systems"

QUESTIONS = [
    # Easy (20)
    {
        "difficulty": "Easy",
        "question": "What is the core component of an Operating System that manages system resources and hardware interaction?",
        "options": ["Kernel", "Shell", "Compiler", "File Explorer"],
        "answer": "Kernel",
        "explanation": "The Kernel is the central core of an operating system responsible for managing CPU, memory, and hardware I/O."
    },
    {
        "difficulty": "Easy",
        "question": "What is a Process in operating system terminology?",
        "options": ["A program stored on disk", "A program in execution", "A thread in waiting state", "A hardware interrupt"],
        "answer": "A program in execution",
        "explanation": "A process is an active program currently being executed by the CPU, complete with program counter, stack, and state."
    },
    {
        "difficulty": "Easy",
        "question": "Which scheduling algorithm serves processes strictly in the order they arrive in the ready queue?",
        "options": ["First-Come, First-Served (FCFS)", "Shortest Job First (SJF)", "Round Robin (RR)", "Priority Scheduling"],
        "answer": "First-Come, First-Served (FCFS)",
        "explanation": "FCFS is a non-preemptive scheduling policy that executes processes in arrival sequence."
    },
    {
        "difficulty": "Easy",
        "question": "What is the time-sharing scheduling algorithm that assigns a fixed time slice (time quantum) to each process?",
        "options": ["Round Robin (RR)", "FCFS", "SJF", "Multilevel Queue"],
        "answer": "Round Robin (RR)",
        "explanation": "Round Robin assigns equal fixed time slices to processes cyclically, preventing CPU starvation in interactive systems."
    },
    {
        "difficulty": "Easy",
        "question": "What is a Thread often referred to as?",
        "options": ["Heavyweight Process", "Lightweight Process (LWP)", "Kernel Module", "Virtual Machine"],
        "answer": "Lightweight Process (LWP)",
        "explanation": "A thread is called a lightweight process because it shares memory space and resources with other threads in the same process."
    },
    {
        "difficulty": "Easy",
        "question": "What is Deadlock in operating systems?",
        "options": ["A condition where two or more processes are blocked indefinitely waiting for resources held by each other", "A CPU crash due to overheating", "When a file is deleted accidentally", "A process that consumes 100% CPU"],
        "answer": "A condition where two or more processes are blocked indefinitely waiting for resources held by each other",
        "explanation": "Deadlock occurs when every process in a set is waiting for an event that only another process in the set can cause."
    },
    {
        "difficulty": "Easy",
        "question": "What does PCB stand for in process management?",
        "options": ["Process Control Block", "Program Central Board", "Priority Control Bus", "Processor Configuration Base"],
        "answer": "Process Control Block",
        "explanation": "The PCB stores essential process information including PID, register states, program counter, and memory limits."
    },
    {
        "difficulty": "Easy",
        "question": "What is Virtual Memory?",
        "options": ["Physical RAM chips installed on motherboard", "A memory management capability of an OS that uses secondary storage to let software use more memory than physically present RAM", "ROM memory containing BIOS", "Cache memory in L1/L2"],
        "answer": "A memory management capability of an OS that uses secondary storage to let software use more memory than physically present RAM",
        "explanation": "Virtual memory maps virtual addresses to physical pages and disk swap space, creating the illusion of a large contiguous address space."
    },
    {
        "difficulty": "Easy",
        "question": "What occurs when a requested page is not currently present in physical main memory (RAM)?",
        "options": ["Page Fault", "Segmentation Fault", "Stack Overflow", "Bus Error"],
        "answer": "Page Fault",
        "explanation": "A page fault is an interrupt raised by hardware when a program accesses a memory page not loaded in RAM."
    },
    {
        "difficulty": "Easy",
        "question": "Which of the following is a non-preemptive scheduling algorithm?",
        "options": ["Round Robin", "Shortest Remaining Time First (SRTF)", "Standard First-Come First-Served (FCFS)", "Preemptive Priority"],
        "answer": "Standard First-Come First-Served (FCFS)",
        "explanation": "In standard FCFS, once a process gets CPU access, it runs until termination or I/O request without being preempted."
    },
    {
        "difficulty": "Easy",
        "question": "What is Context Switching?",
        "options": ["Saving the state of a currently running process and restoring the state of another process to resume execution", "Switching from Windows to Linux", "Changing network IP address", "Reallocating hard drive partitions"],
        "answer": "Saving the state of a currently running process and restoring the state of another process to resume execution",
        "explanation": "Context switching stores CPU registers/PCB of the old process and loads the PCB state of the new process."
    },
    {
        "difficulty": "Easy",
        "question": "What is a System Call?",
        "options": ["A programmatic way in which a computer program requests a privileged service from the operating system kernel", "A voice call over IP", "A hardware reset button", "A network ping request"],
        "answer": "A programmatic way in which a computer program requests a privileged service from the operating system kernel",
        "explanation": "System calls (e.g. read, write, fork) provide the interface between user-space applications and kernel services."
    },
    {
        "difficulty": "Easy",
        "question": "What is the critical section problem concerned with?",
        "options": ["Ensuring only one process accesses a shared resource at a given time to avoid race conditions", "Optimizing compiler loop execution", "Formatting damaged hard drive sectors", "Balancing network traffic load"],
        "answer": "Ensuring only one process accesses a shared resource at a given time to avoid race conditions",
        "explanation": "The critical section is code accessing shared resources that requires mutual exclusion to prevent data corruption."
    },
    {
        "difficulty": "Easy",
        "question": "What is a Semaphore in process synchronization?",
        "options": ["An integer variable used for signaling and mutual exclusion access to shared resources via `wait()` and `signal()`", "A type of network router", "A hardware graphics processor", "A physical printer spooler"],
        "answer": "An integer variable used for signaling and mutual exclusion access to shared resources via `wait()` and `signal()`",
        "explanation": "A semaphore is a synchronization tool providing atomic `wait` (P) and `signal` (V) operations to regulate access."
    },
    {
        "difficulty": "Easy",
        "question": "What is Thrashing in operating systems?",
        "options": ["When the system spends more time servicing page faults and swapping pages than executing instructions", "When a disk controller catches fire", "When the CPU fan fails", "When infinite print jobs queue up"],
        "answer": "When the system spends more time servicing page faults and swapping pages than executing instructions",
        "explanation": "Thrashing occurs when the working sets of active processes exceed available physical memory, collapsing CPU throughput."
    },
    {
        "difficulty": "Easy",
        "question": "Which Unix command is used to create a new child process?",
        "options": ["spawn()", "fork()", "create_proc()", "new()"],
        "answer": "fork()",
        "explanation": "The `fork()` system call creates a new process by duplicating the calling parent process."
    },
    {
        "difficulty": "Easy",
        "question": "What is the main purpose of Spooling (Simultaneous Peripheral Operations On-Line)?",
        "options": ["Buffering data for slow peripheral devices (like printers) so the CPU can continue processing other tasks", "Encrypting passwords", "Speeding up RAM clock speed", "Compressing image files"],
        "answer": "Buffering data for slow peripheral devices (like printers) so the CPU can continue processing other tasks",
        "explanation": "Spooling buffers input/output jobs on disk (such as print jobs) to bridge the speed mismatch between fast CPU and slow devices."
    },
    {
        "difficulty": "Easy",
        "question": "What is an Orphan Process in Linux/Unix?",
        "options": ["A process whose parent has terminated, causing it to be adopted by init/systemd (PID 1)", "A process that never terminates", "A process without CPU allocation", "A virus program"],
        "answer": "A process whose parent has terminated, causing it to be adopted by init/systemd (PID 1)",
        "explanation": "When a parent process exits before its child, the child becomes an orphan and is re-parented to PID 1 (`init`)."
    },
    {
        "difficulty": "Easy",
        "question": "What is a Zombie Process in Unix?",
        "options": ["A process that has completed execution but still has an entry in the process table because its parent hasn't read its exit status", "A process that restarts automatically after reboot", "A thread with corrupted stack", "A process that hogs memory"],
        "answer": "A process that has completed execution but still has an entry in the process table because its parent hasn't read its exit status",
        "explanation": "A zombie (defunct) process has finished execution but remains in the process table until its parent calls `wait()`."
    },
    {
        "difficulty": "Easy",
        "question": "What are the two standard execution modes in modern CPU architectures for OS security?",
        "options": ["User Mode and Kernel (Supervisor) Mode", "Fast Mode and Slow Mode", "Debug Mode and Production Mode", "Single Mode and Dual Mode"],
        "answer": "User Mode and Kernel (Supervisor) Mode",
        "explanation": "CPUs use dual-mode operation (User mode for applications, Kernel mode for OS kernel) to protect critical hardware and memory."
    },

    # Medium (20)
    {
        "difficulty": "Medium",
        "question": "What are the four necessary Coffman conditions for a Deadlock to occur?",
        "options": ["Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait", "Preemption, Starvation, Aging, Thrashing", "Paging, Segmentation, Swapping, Compaction", "Fork, Exec, Wait, Exit"],
        "answer": "Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait",
        "explanation": "All four conditions must hold simultaneously for deadlock: mutual exclusion, hold and wait, no preemption, and circular wait."
    },
    {
        "difficulty": "Medium",
        "question": "What is Banker's Algorithm used for in operating systems?",
        "options": ["Deadlock Avoidance by testing for safe states before allocating requested resources", "Calculating interest rates in financial DBs", "Disk defragmentation", "CPU overclocking"],
        "answer": "Deadlock Avoidance by testing for safe states before allocating requested resources",
        "explanation": "Dijkstra's Banker's algorithm avoids deadlock by simulating resource allocation and ensuring the system remains in a safe state."
    },
    {
        "difficulty": "Medium",
        "question": "What is Belady's Anomaly in page replacement algorithms?",
        "options": ["When increasing the number of page frames results in an increased number of page faults (observable in FIFO)", "When RAM fails unexpectedly", "When LRU page replacement performs worse than Random", "When page size is doubled"],
        "answer": "When increasing the number of page frames results in an increased number of page faults (observable in FIFO)",
        "explanation": "Belady's Anomaly occurs in FIFO page replacement where allocating more physical page frames causes more total page faults."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Internal and External Fragmentation?",
        "options": ["Internal fragmentation is unused allocated memory inside a fixed partition; External fragmentation is unused free space scattered outside allocated partitions", "External fragmentation occurs only in cache", "Internal fragmentation cannot be solved by paging", "They are identical"],
        "answer": "Internal fragmentation is unused allocated memory inside a fixed partition; External fragmentation is unused free space scattered outside allocated partitions",
        "explanation": "Internal fragmentation occurs when allocated blocks exceed requested size; external fragmentation occurs when total free memory is fragmented into small non-contiguous blocks."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Translation Lookaside Buffer (TLB)?",
        "options": ["A fast hardware cache of virtual-to-physical address translations located inside the MMU", "A buffer for disk write requests", "A network packet queue", "A stack frame pointer"],
        "answer": "A fast hardware cache of virtual-to-physical address translations located inside the MMU",
        "explanation": "The TLB caches recent page table translations to speed up virtual memory address resolution without querying RAM twice."
    },
    {
        "difficulty": "Medium",
        "question": "What is the Inverted Page Table structure?",
        "options": ["A page table indexed by physical frame numbers rather than virtual page numbers, with one entry per physical frame", "A page table stored on disk swap", "A page table that reverses bit order", "A page table for multi-threaded processes only"],
        "answer": "A page table indexed by physical frame numbers rather than virtual page numbers, with one entry per physical frame",
        "explanation": "An inverted page table has one entry for each real physical memory frame, dramatically reducing page table size across large 64-bit address spaces."
    },
    {
        "difficulty": "Medium",
        "question": "Which page replacement algorithm achieves theoretically optimal lowest page fault rate by replacing the page not needed for longest time in the future?",
        "options": ["Optimal Page Replacement (OPT / Belady's Algorithm)", "First-In-First-Out (FIFO)", "Least Recently Used (LRU)", "Least Frequently Used (LFU)"],
        "answer": "Optimal Page Replacement (OPT / Belady's Algorithm)",
        "explanation": "Optimal Page Replacement (OPT) replaces the page that will not be referenced for the longest duration in the future (serving as theoretical benchmark)."
    },
    {
        "difficulty": "Medium",
        "question": "What is Peterson's Solution in concurrent programming?",
        "options": ["A software-based algorithm for mutual exclusion between two processes that avoids race conditions using flags and a turn variable", "A disk scheduling algorithm", "A page allocation strategy", "A deadlock recovery routine"],
        "answer": "A software-based algorithm for mutual exclusion between two processes that avoids race conditions using flags and a turn variable",
        "explanation": "Peterson's algorithm provides mutual exclusion, progress, and bounded waiting for two processes using shared `flag` and `turn` variables."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of the `exec()` family of system calls in Unix?",
        "options": ["Replaces the current process image, code, and data with a new executable program binary", "Terminates the operating system", "Duplicates file descriptors", "Pauses process execution"],
        "answer": "Replaces the current process image, code, and data with a new executable program binary",
        "explanation": "While `fork()` duplicates the calling process, `exec()` loads and runs a new program inside the existing process."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Preemptive and Non-Preemptive scheduling?",
        "options": ["Preemptive allows OS to forcibly take CPU away from running process; Non-preemptive lets process run until it voluntarily yields or terminates", "Preemptive runs only on single-core CPUs", "Non-preemptive allows infinite time slices", "Preemptive cannot use priorities"],
        "answer": "Preemptive allows OS to forcibly take CPU away from running process; Non-preemptive lets process run until it voluntarily yields or terminates",
        "explanation": "Preemptive schedulers can interrupt and switch active tasks via timer interrupts; non-preemptive schedulers wait until the process releases CPU."
    },
    {
        "difficulty": "Medium",
        "question": "What is the Convoy Effect in CPU scheduling?",
        "options": ["When small, short processes wait for a long CPU-bound process to finish in FCFS scheduling, lowering CPU and device utilization", "When multiple threads run at identical speeds", "When disk tracks are read sequentially", "When priority inversion occurs"],
        "answer": "When small, short processes wait for a long CPU-bound process to finish in FCFS scheduling, lowering CPU and device utilization",
        "explanation": "Convoy effect happens in FCFS when multiple I/O bound processes queue behind a single heavy CPU-bound process."
    },
    {
        "difficulty": "Medium",
        "question": "What is Priority Inversion in real-time operating systems?",
        "options": ["When a high-priority task is indirectly preempted by a lower-priority task holding a resource needed by high-priority task", "When negative priorities are assigned", "When round-robin ignores priorities", "When kernel threads run slower than user threads"],
        "answer": "When a high-priority task is indirectly preempted by a lower-priority task holding a resource needed by high-priority task",
        "explanation": "Priority inversion happens when a medium task prevents a low task from releasing a lock needed by a high task, solvable by Priority Inheritance."
    },
    {
        "difficulty": "Medium",
        "question": "What is an Inode in Unix/Linux file systems?",
        "options": ["A data structure that stores metadata (size, permissions, timestamps, block pointers) about a file system object", "The physical sector address of a file", "The file name string", "A user account identifier"],
        "answer": "A data structure that stores metadata (size, permissions, timestamps, block pointers) about a file system object",
        "explanation": "An inode stores all metadata and data block pointers of a file except its filename and raw content."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between a Hard Link and a Symbolic (Soft) Link in Linux?",
        "options": ["A Hard Link points directly to the inode of the target file; a Soft Link stores the path to the target file as independent file/inode", "Soft links cannot link directories", "Hard links break when file is moved", "Soft links share the exact same inode"],
        "answer": "A Hard Link points directly to the inode of the target file; a Soft Link stores the path to the target file as independent file/inode",
        "explanation": "Hard links are additional directory entries pointing to the same inode; soft links are separate files storing target path strings."
    },
    {
        "difficulty": "Medium",
        "question": "Which disk scheduling algorithm moves the disk arm from one end to the other servicing requests, reversing direction when it reaches the end?",
        "options": ["SCAN (Elevator Algorithm)", "C-SCAN", "FCFS", "SSTF (Shortest Seek Time First)"],
        "answer": "SCAN (Elevator Algorithm)",
        "explanation": "The SCAN (Elevator) algorithm sweeps the disk head back and forth across tracks servicing pending cylinder requests."
    },
    {
        "difficulty": "Medium",
        "question": "What is the primary difference between C-SCAN and SCAN disk scheduling algorithms?",
        "options": ["C-SCAN only services requests in one direction, then immediately returns to the beginning without servicing requests on the return pass", "C-SCAN never services cylinders at the edge", "SCAN is circular, C-SCAN is linear", "C-SCAN requires SSD storage"],
        "answer": "C-SCAN only services requests in one direction, then immediately returns to the beginning without servicing requests on the return pass",
        "explanation": "C-SCAN (Circular SCAN) provides a more uniform wait time by servicing requests in one direction and returning straight to start."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of the `mmap()` system call?",
        "options": ["Maps files or devices directly into the application's virtual memory address space", "Formats flash memory", "Displays memory usage statistics", "Allocates thread stack space"],
        "answer": "Maps files or devices directly into the application's virtual memory address space",
        "explanation": "`mmap()` maps a file into virtual memory so file I/O can be performed via direct memory pointer reads/writes."
    },
    {
        "difficulty": "Medium",
        "question": "What is Copy-on-Write (COW) during process creation?",
        "options": ["Child process shares pages with parent read-only; pages are duplicated in RAM only when either process modifies them", "Copying disk blocks upon write error", "Writing memory to two RAM sticks simultaneously", "Backing up inodes"],
        "answer": "Child process shares pages with parent read-only; pages are duplicated in RAM only when either process modifies them",
        "explanation": "COW optimizes `fork()` by postponing page copying until a write occurs, saving time and memory if `exec()` follows immediately."
    },
    {
        "difficulty": "Medium",
        "question": "What is Direct Memory Access (DMA)?",
        "options": ["A hardware feature that allows I/O devices to transfer data directly to/from main memory without continuous CPU intervention", "A command to bypass virtual memory", "Direct CPU access to L1 cache", "Accessing RAM over WiFi"],
        "answer": "A hardware feature that allows I/O devices to transfer data directly to/from main memory without continuous CPU intervention",
        "explanation": "DMA controllers transfer entire data blocks between I/O peripherals and RAM, interrupting CPU only when transfer completes."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Spinlock in OS kernel synchronization?",
        "options": ["A lock where a waiting thread repeatedly checks a condition in a tight busy-waiting loop rather than sleeping", "A circular linked list lock", "A lock used for HDD platters", "A lock that times out in 1 millisecond"],
        "answer": "A lock where a waiting thread repeatedly checks a condition in a tight busy-waiting loop rather than sleeping",
        "explanation": "Spinlocks use busy-waiting (spinning) to wait for lock release, ideal for multi-core systems where lock hold times are extremely brief."
    },

    # Hard (10)
    {
        "difficulty": "Hard",
        "question": "In the Linux Completely Fair Scheduler (CFS), what metric is used to determine which process to schedule next?",
        "options": ["Virtual Runtime (`vruntime`) tracked using a time-ordered Red-Black tree", "Fixed priority numbers from 0 to 99", "Remaining time quantum in round robin", "Shortest burst time remaining"],
        "answer": "Virtual Runtime (`vruntime`) tracked using a time-ordered Red-Black tree",
        "explanation": "CFS selects the process with the smallest `vruntime` (leftmost node in its red-black tree) to ensure proportional fairness."
    },
    {
        "difficulty": "Hard",
        "question": "What is the Multi-Level Feedback Queue (MLFQ) scheduling algorithm designed to solve?",
        "options": ["Balancing responsive turn-around time for interactive I/O tasks while preventing starvation and minimizing overhead for long CPU tasks without prior burst time knowledge", "Scheduling network packets", "Sorting hard disk blocks", "Managing virtual page allocations"],
        "answer": "Balancing responsive turn-around time for interactive I/O tasks while preventing starvation and minimizing overhead for long CPU tasks without prior burst time knowledge",
        "explanation": "MLFQ dynamically adjusts process priorities based on observed execution behavior (giving priority to short/interactive I/O bursts)."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between Microkernel and Monolithic kernel architectures?",
        "options": ["Microkernels keep only core primitives in kernel space (running drivers/filesystems in user space via IPC); Monolithic kernels run all OS services in kernel address space", "Monolithic kernels are slower for all operations", "Microkernels do not support multi-threading", "Monolithic kernels cannot run on x86"],
        "answer": "Microkernels keep only core primitives in kernel space (running drivers/filesystems in user space via IPC); Monolithic kernels run all OS services in kernel address space",
        "explanation": "Microkernels enhance modularity and fault isolation by running servers in user mode; monolithic kernels run everything in kernel mode for raw performance."
    },
    {
        "difficulty": "Hard",
        "question": "What is the Working Set Model in memory management?",
        "options": ["An approximation of process locality that defines the set of pages referenced by a process during a sliding time window Δ to prevent thrashing", "The set of open file handles", "The total size of physical RAM", "The number of active background threads"],
        "answer": "An approximation of process locality that defines the set of pages referenced by a process during a sliding time window Δ to prevent thrashing",
        "explanation": "Working Set Model ensures a process is allocated enough page frames to hold its active working set `W(t, Δ)`, preventing thrashing."
    },
    {
        "difficulty": "Hard",
        "question": "How does the RCU (Read-Copy-Update) synchronization mechanism achieve high read scalability in Linux kernel?",
        "options": ["Readers access data concurrently without locking or atomic operations; writers make a copy, update it, atomically swap pointers, and defer old memory reclamation until a grace period elapses", "By locking all cores on every read", "By disabling interrupts during read operations", "By serializing all reader threads"],
        "answer": "Readers access data concurrently without locking or atomic operations; writers make a copy, update it, atomically swap pointers, and defer old memory reclamation until a grace period elapses",
        "explanation": "RCU allows concurrent lock-free reads while deferring memory destruction until all pre-existing read critical sections complete (grace period)."
    },
    {
        "difficulty": "Hard",
        "question": "What is the purpose of Page Coloring in OS virtual memory subsystem?",
        "options": ["Assigning physical page frames to virtual pages such that consecutive pages map to distinct L1/L2 cache sets, minimizing hardware cache conflicts", "Highlighting kernel memory in debuggers", "Encrypting memory pages with distinct keys", "Tagging pages by process ID"],
        "answer": "Assigning physical page frames to virtual pages such that consecutive pages map to distinct L1/L2 cache sets, minimizing hardware cache conflicts",
        "explanation": "Page coloring aligns page frame allocation with CPU hardware cache line indexing to prevent cache thrashing."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between Asymmetric and Symmetric Multi-Processing (SMP)?",
        "options": ["In SMP, all processors share a common memory space and run identical kernel code with equal status; in Asymmetric, one master CPU manages OS tasks while slaves execute user code", "SMP uses discrete GPUs only", "Asymmetric multiprocessing is used in all modern multi-core PCs", "SMP requires separate physical memory per core"],
        "answer": "In SMP, all processors share a common memory space and run identical kernel code with equal status; in Asymmetric, one master CPU manages OS tasks while slaves execute user code",
        "explanation": "Symmetric Multiprocessing (SMP) treats all CPUs identically with peer access to memory, whereas Asymmetric assigns designated master-slave roles."
    },
    {
        "difficulty": "Hard",
        "question": "What is the TLB Shootdown phenomenon in multi-core operating systems?",
        "options": ["The process where an OS core broadcasts Inter-Processor Interrupts (IPI) to invalidate stale cached virtual-to-physical address mappings in other CPUs' TLBs", "When TLB hardware overheats", "When page faults crash the CPU", "When virtual address space exceeds 48 bits"],
        "answer": "The process where an OS core broadcasts Inter-Processor Interrupts (IPI) to invalidate stale cached virtual-to-physical address mappings in other CPUs' TLBs",
        "explanation": "When page mappings change in multi-core architectures, an OS sends IPI interrupts across cores to force TLB flush (TLB shootdown)."
    },
    {
        "difficulty": "Hard",
        "question": "What is a Memory Barrier (Memory Fence) instruction in concurrent programming?",
        "options": ["A CPU instruction that forces strict ordering constraints on memory reads and writes, preventing hardware/compiler out-of-order reordering across the fence", "A firewall that blocks unauthorized RAM access", "A hardware limit register for user space", "A routine that zeroes memory"],
        "answer": "A CPU instruction that forces strict ordering constraints on memory reads and writes, preventing hardware/compiler out-of-order reordering across the fence",
        "explanation": "Memory barriers prevent processor and compiler instruction reordering, enforcing memory visibility and coherence across multi-threaded cores."
    },
    {
        "difficulty": "Hard",
        "question": "What is the Slab Allocator used for in the Linux kernel?",
        "options": ["Eliminating internal fragmentation and caching frequently created kernel objects (inodes, task_structs) for fast O(1) reuse without invoking page allocator", "Managing swap partition blocks", "Allocating user-space malloc() heaps", "Defragmenting SSD blocks"],
        "answer": "Eliminating internal fragmentation and caching frequently created kernel objects (inodes, task_structs) for fast O(1) reuse without invoking page allocator",
        "explanation": "Slab allocation pre-allocates pools of contiguous memory chunks tailored to specific kernel object sizes, avoiding allocation overhead."
    }
]
