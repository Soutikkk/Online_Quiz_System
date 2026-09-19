CATEGORY = "Programming Fundamentals"

QUESTIONS = [
    # Easy (20)
    {
        "difficulty": "Easy",
        "question": "Which of the following is an example of a primitive data type in C?",
        "options": ["int", "struct", "class", "union"],
        "answer": "int",
        "explanation": "In C, 'int' is a basic primitive data type, whereas struct, class, and union are user-defined/composite types."
    },
    {
        "difficulty": "Easy",
        "question": "What is the correct syntax for a single-line comment in C++ and Java?",
        "options": ["// comment", "/* comment */", "# comment", "<!-- comment -->"],
        "answer": "// comment",
        "explanation": "Double slashes (//) denote a single-line comment in C, C++, Java, and C#."
    },
    {
        "difficulty": "Easy",
        "question": "Which loop is guaranteed to execute at least once?",
        "options": ["for loop", "while loop", "do-while loop", "nested loop"],
        "answer": "do-while loop",
        "explanation": "A do-while loop evaluates its condition after executing the loop body, guaranteeing at least one execution."
    },
    {
        "difficulty": "Easy",
        "question": "What is the output of the logical expression: (true && false)?",
        "options": ["true", "false", "null", "undefined"],
        "answer": "false",
        "explanation": "The logical AND (&&) operator evaluates to true only if both operands are true."
    },
    {
        "difficulty": "Easy",
        "question": "Which keyword is used to exit prematurely from a loop in most programming languages?",
        "options": ["continue", "break", "exit", "return"],
        "answer": "break",
        "explanation": "The 'break' statement terminates the nearest enclosing loop immediately."
    },
    {
        "difficulty": "Easy",
        "question": "What is the index of the first element in standard zero-indexed arrays?",
        "options": ["0", "1", "-1", "null"],
        "answer": "0",
        "explanation": "In zero-indexed languages (C, C++, Java, Python, JS), array indices start at 0."
    },
    {
        "difficulty": "Easy",
        "question": "Which component translates high-level code line-by-line during execution?",
        "options": ["Compiler", "Interpreter", "Assembler", "Linker"],
        "answer": "Interpreter",
        "explanation": "An interpreter translates and executes high-level source code line-by-line."
    },
    {
        "difficulty": "Easy",
        "question": "Which of the following represents the logical NOT operator in C-family languages?",
        "options": ["~", "!", "not", "^"],
        "answer": "!",
        "explanation": "The exclamation mark (!) is the logical NOT operator in C, C++, Java, and JavaScript."
    },
    {
        "difficulty": "Easy",
        "question": "What is the binary representation of decimal number 10?",
        "options": ["1010", "1100", "1001", "1110"],
        "answer": "1010",
        "explanation": "8 + 2 = 10, which in 4-bit binary is 1010."
    },
    {
        "difficulty": "Easy",
        "question": "Which data type would be best suited to store the value of Pi (3.14159)?",
        "options": ["int", "char", "float", "boolean"],
        "answer": "float",
        "explanation": "Floating-point types (float or double) represent real numbers with fractional parts."
    },
    {
        "difficulty": "Easy",
        "question": "What does IDE stand for in software development?",
        "options": ["Integrated Development Environment", "Internal Design Engine", "Interactive Development Explorer", "Integrated Debugger & Editor"],
        "answer": "Integrated Development Environment",
        "explanation": "IDE stands for Integrated Development Environment, providing editor, compiler/debugger, and tools in one package."
    },
    {
        "difficulty": "Easy",
        "question": "Which operator is used to compare two values for equality in C/C++/Java?",
        "options": ["=", "==", "===", "!="],
        "answer": "==",
        "explanation": "The '==' operator checks equality, while '=' is the assignment operator."
    },
    {
        "difficulty": "Easy",
        "question": "What is a function that calls itself known as?",
        "options": ["Nested function", "Inline function", "Recursive function", "Virtual function"],
        "answer": "Recursive function",
        "explanation": "A recursive function is a function that solves a problem by calling a smaller instance of itself."
    },
    {
        "difficulty": "Easy",
        "question": "Which arithmetic operator calculates the remainder of a division?",
        "options": ["/", "%", "//", "**"],
        "answer": "%",
        "explanation": "The modulo operator (%) yields the remainder of integer division."
    },
    {
        "difficulty": "Easy",
        "question": "What is the typical size of a standard `char` data type in C?",
        "options": ["1 byte", "2 bytes", "4 bytes", "8 bytes"],
        "answer": "1 byte",
        "explanation": "In C standard, sizeof(char) is defined to be 1 byte (8 bits)."
    },
    {
        "difficulty": "Easy",
        "question": "Which stage of compilation combines object files into a single executable file?",
        "options": ["Preprocessor", "Lexical Analyzer", "Linker", "Loader"],
        "answer": "Linker",
        "explanation": "The linker takes one or more object files generated by the compiler and combines them into an executable."
    },
    {
        "difficulty": "Easy",
        "question": "What is the default return type of the main() function in standard C?",
        "options": ["void", "int", "float", "char"],
        "answer": "int",
        "explanation": "Standard C (C99 and later) defines the return type of main as int (e.g., int main())."
    },
    {
        "difficulty": "Easy",
        "question": "Which control statement skips the rest of the current iteration and begins the next?",
        "options": ["break", "continue", "goto", "pass"],
        "answer": "continue",
        "explanation": "The continue statement bypasses remaining code in the loop iteration and moves to the next iteration."
    },
    {
        "difficulty": "Easy",
        "question": "What term describes a variable that is accessible throughout an entire program?",
        "options": ["Local variable", "Global variable", "Static variable", "Register variable"],
        "answer": "Global variable",
        "explanation": "Global variables are declared outside all functions and accessible throughout the file or program."
    },
    {
        "difficulty": "Easy",
        "question": "What character is used to terminate statements in C, C++, and Java?",
        "options": [":", ";", ".", ","],
        "answer": ";",
        "explanation": "Semicolon (;) is the standard statement terminator in C, C++, and Java."
    },

    # Medium (20)
    {
        "difficulty": "Medium",
        "question": "What will be the result of integer division `7 / 2` in C language?",
        "options": ["3.5", "3", "4", "3.0"],
        "answer": "3",
        "explanation": "In C, dividing two integers performs integer division, truncating the fractional part and resulting in 3."
    },
    {
        "difficulty": "Medium",
        "question": "What is a dangling pointer in C/C++?",
        "options": ["A pointer initialized to NULL", "A pointer pointing to a deallocated memory location", "A pointer that points to another pointer", "A pointer that has never been initialized"],
        "answer": "A pointer pointing to a deallocated memory location",
        "explanation": "A dangling pointer points to a memory block that has already been freed or deallocated."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of the `volatile` keyword in C/C++?",
        "options": ["To make variable read-only", "To prevent compiler optimization on variables that may change unexpectedly", "To allocate memory in CPU registers", "To allow variable to be shared across threads automatically"],
        "answer": "To prevent compiler optimization on variables that may change unexpectedly",
        "explanation": "Volatile tells the compiler that the value of the variable may change at any time without any action taken by the code, preventing unsafe caching."
    },
    {
        "difficulty": "Medium",
        "question": "What happens if a recursive function does not have a proper base condition?",
        "options": ["It runs forever without error", "It results in a Stack Overflow runtime error", "It compiles with a warning only", "It returns NULL immediately"],
        "answer": "It results in a Stack Overflow runtime error",
        "explanation": "Without a base case, recursive calls consume stack frames until stack memory is exhausted, causing a stack overflow."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between call by value and call by reference?",
        "options": ["Call by value passes copies, call by reference passes memory addresses", "Call by value modifies the original variable", "Call by reference uses more memory than call by value", "There is no difference in execution"],
        "answer": "Call by value passes copies, call by reference passes memory addresses",
        "explanation": "Call by value creates a copy of the argument, so changes inside the function do not affect the caller's variable."
    },
    {
        "difficulty": "Medium",
        "question": "In C, which memory allocation function initializes the allocated memory to all zeros?",
        "options": ["malloc()", "calloc()", "realloc()", "free()"],
        "answer": "calloc()",
        "explanation": "calloc(num, size) allocates memory and initializes all bytes to zero, whereas malloc() leaves memory uninitialized."
    },
    {
        "difficulty": "Medium",
        "question": "What is short-circuit evaluation in logical expressions?",
        "options": ["Evaluating all operands regardless of result", "Stopping evaluation as soon as the outcome is determined", "Evaluating expressions backwards", "Skipping syntax checking"],
        "answer": "Stopping evaluation as soon as the outcome is determined",
        "explanation": "In short-circuiting (e.g., A && B), if A is false, B is never evaluated because the expression must be false."
    },
    {
        "difficulty": "Medium",
        "question": "What is the output of the bitwise operation `5 ^ 5` (XOR)?",
        "options": ["5", "10", "0", "1"],
        "answer": "0",
        "explanation": "XORing any integer with itself produces 0 because all identical bits become 0 (x ^ x = 0)."
    },
    {
        "difficulty": "Medium",
        "question": "What is the scope of a static local variable declared inside a function in C?",
        "options": ["Global across all files", "Limited to the function, but retains its value across function calls", "Destroyed when function exits", "Visible to parent functions only"],
        "answer": "Limited to the function, but retains its value across function calls",
        "explanation": "Static local variables have function scope, but lifetime is the entire duration of the program."
    },
    {
        "difficulty": "Medium",
        "question": "Which data segment stores uninitialized global and static variables in a C program?",
        "options": ["Text Segment", "Data Segment", "BSS Segment", "Stack Segment"],
        "answer": "BSS Segment",
        "explanation": "BSS (Block Started by Symbol) stores uninitialized global and static variables, initialized to zero by runtime."
    },
    {
        "difficulty": "Medium",
        "question": "What does the `sizeof` operator in C return?",
        "options": ["Size of operand in bits", "Size of operand in bytes as type size_t", "Number of elements in any pointer", "Address of operand"],
        "answer": "Size of operand in bytes as type size_t",
        "explanation": "The sizeof operator yields the storage size of its operand in bytes as an unsigned integer type (size_t)."
    },
    {
        "difficulty": "Medium",
        "question": "What is an enum in C/C++?",
        "options": ["A collection of functions", "A user-defined type consisting of named integer constants", "A dynamic memory block", "A macro substitution rule"],
        "answer": "A user-defined type consisting of named integer constants",
        "explanation": "An enumeration (enum) is a user-defined data type used to assign names to integral constants."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of header guards (`#ifndef`, `#define`, `#endif`) in C/C++ header files?",
        "options": ["To speed up execution speed at runtime", "To prevent multiple inclusions of the same header file", "To hide code from users", "To encrypt source files"],
        "answer": "To prevent multiple inclusions of the same header file",
        "explanation": "Header guards prevent double definition errors by ensuring the header file is only included once per translation unit."
    },
    {
        "difficulty": "Medium",
        "question": "Which of the following best describes type casting?",
        "options": ["Converting a variable from one data type to another", "Deleting unused variables", "Creating aliases for variables", "Passing parameters to a function"],
        "answer": "Converting a variable from one data type to another",
        "explanation": "Type casting is the explicit or implicit conversion of a value from one data type to another."
    },
    {
        "difficulty": "Medium",
        "question": "What will `printf(\"%d\", 10 >> 1);` print in C?",
        "options": ["20", "5", "10", "1"],
        "answer": "5",
        "explanation": "The right shift operator `>> 1` shifts bits one position to the right, which divides the integer by 2 (10 / 2 = 5)."
    },
    {
        "difficulty": "Medium",
        "question": "What is memory leak in programming?",
        "options": ["When program runs out of disk space", "When dynamically allocated memory is no longer referenced but not deallocated", "When variables are overwritten accidentally", "When CPU cache is purged"],
        "answer": "When dynamically allocated memory is no longer referenced but not deallocated",
        "explanation": "A memory leak occurs when heap memory allocated via malloc/new is not released when no longer needed."
    },
    {
        "difficulty": "Medium",
        "question": "Which stage of compilation handles `#include` and `#define` directives in C?",
        "options": ["Lexical Analysis", "Preprocessor", "Code Optimizer", "Assembler"],
        "answer": "Preprocessor",
        "explanation": "The C Preprocessor processes all directives starting with '#' before actual compilation begins."
    },
    {
        "difficulty": "Medium",
        "question": "What is tail recursion?",
        "options": ["A recursion that occurs at the beginning of a function", "A recursive call that is the very last operation performed in the function", "A recursion with two recursive branches", "A recursion that never terminates"],
        "answer": "A recursive call that is the very last operation performed in the function",
        "explanation": "In tail recursion, the recursive call is the final action, allowing compilers to optimize stack frame usage."
    },
    {
        "difficulty": "Medium",
        "question": "What is the ASCII value of the character 'A'?",
        "options": ["65", "97", "48", "32"],
        "answer": "65",
        "explanation": "In the standard ASCII table, uppercase 'A' is 65, lowercase 'a' is 97, and '0' is 48."
    },
    {
        "difficulty": "Medium",
        "question": "What does a pointer variable actually store?",
        "options": ["The value of another variable", "The memory address of another variable or object", "The size of a data structure", "The execution status of a thread"],
        "answer": "The memory address of another variable or object",
        "explanation": "A pointer is a variable whose value is the memory address of another variable."
    },

    # Hard (10)
    {
        "difficulty": "Hard",
        "question": "In C, what is undefined behavior when evaluating expressions like `i = i++ + ++i`?",
        "options": ["The result is strictly determined by left-to-right associativity", "Modifying a scalar object more than once between two sequence points produces undefined behavior", "The compiler always throws a compile-time error", "It is guaranteed to be 2 * i + 1"],
        "answer": "Modifying a scalar object more than once between two sequence points produces undefined behavior",
        "explanation": "In C/C++, modifying a variable multiple times without an intervening sequence point causes undefined behavior according to the standard."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between `const char *p` and `char * const p` in C?",
        "options": ["`const char *p` means pointer is constant; `char * const p` means data pointed to is constant", "`const char *p` means pointed data is constant; `char * const p` means the pointer itself is constant", "Both are completely identical", "`char * const p` cannot point to valid characters"],
        "answer": "`const char *p` means pointed data is constant; `char * const p` means the pointer itself is constant",
        "explanation": "`const char *p` makes the character data read-only, whereas `char * const p` makes the pointer address immutable."
    },
    {
        "difficulty": "Hard",
        "question": "What is memory alignment and padding in structure layout?",
        "options": ["Reordering source code functions", "Arranging data in memory to match CPU word boundaries for faster access, leaving unused pad bytes", "Compressing struct fields to 1 bit each", "Encrypting memory blocks"],
        "answer": "Arranging data in memory to match CPU word boundaries for faster access, leaving unused pad bytes",
        "explanation": "Structure padding inserts empty bytes between members so that each member is stored at an address divisible by its alignment requirement."
    },
    {
        "difficulty": "Hard",
        "question": "What does the declaration `void (*signal(int sig, void (*func)(int)))(int);` represent?",
        "options": ["A function returning a pointer to integer", "A function taking an int and a function pointer, returning a function pointer that takes an int and returns void", "A syntax error in modern C", "A pointer to an array of void pointers"],
        "answer": "A function taking an int and a function pointer, returning a function pointer that takes an int and returns void",
        "explanation": "This is the classic ANSI C declaration of `signal()`, which registers a signal handler function and returns the previous signal handler."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between Little Endian and Big Endian architectures?",
        "options": ["Little Endian stores the least significant byte at the lowest address; Big Endian stores the most significant byte at lowest address", "Big Endian uses 64-bit pointers; Little Endian uses 32-bit", "Little Endian reverses bit order inside each individual byte", "Big Endian does not support floating point"],
        "answer": "Little Endian stores the least significant byte at the lowest address; Big Endian stores the most significant byte at lowest address",
        "explanation": "Endianness defines byte ordering in multi-byte words: Little Endian places LSB first (e.g. x86), Big Endian places MSB first (e.g. network order)."
    },
    {
        "difficulty": "Hard",
        "question": "What is the consequence of stack unwinding during an unhandled exception in C++?",
        "options": ["Memory is instantly zeroed out", "Local destructors are called in reverse order of construction until a catch handler is found", "Global variables are re-initialized", "All threads are converted to coroutines"],
        "answer": "Local destructors are called in reverse order of construction until a catch handler is found",
        "explanation": "Stack unwinding cleans up stack-allocated objects by calling their destructors in reverse order as the call stack is popped during exception propagation."
    },
    {
        "difficulty": "Hard",
        "question": "In C, what is the role of the `restrict` keyword introduced in C99?",
        "options": ["Restricts variable access to a single thread", "Informs the compiler that for the lifetime of the pointer, only it will be used to access the object it points to (no aliasing)", "Prevents pointers from being cast to void*", "Disallows modifying the pointer address"],
        "answer": "Informs the compiler that for the lifetime of the pointer, only it will be used to access the object it points to (no aliasing)",
        "explanation": "`restrict` tells the compiler that the pointer is the sole reference to the memory block, enabling aggressive compiler vectorization and caching optimizations."
    },
    {
        "difficulty": "Hard",
        "question": "What is the purpose of two's complement representation for signed integers?",
        "options": ["To avoid having two representations for zero (+0 and -0) and allow subtraction using standard adder circuits", "To make negative numbers take less memory", "To prevent integer overflow", "To simplify floating point conversions"],
        "answer": "To avoid having two representations for zero (+0 and -0) and allow subtraction using standard adder circuits",
        "explanation": "Two's complement provides a single unique 0 and allows addition and subtraction to be implemented with the exact same hardware ALU circuitry."
    },
    {
        "difficulty": "Hard",
        "question": "What is a reentrant function?",
        "options": ["A function that never returns a value", "A function that can be interrupted and re-invoked safely before its previous execution completes", "A function that only accepts constant arguments", "A function that executes inside the OS kernel only"],
        "answer": "A function that can be interrupted and re-invoked safely before its previous execution completes",
        "explanation": "A reentrant function holds no non-constant static/global data and does not return pointers to static data, making it safe for concurrent/signal interruption."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between static linking and dynamic linking?",
        "options": ["Static linking includes library code directly into the binary at compile time; dynamic linking resolves references at load/run time", "Dynamic linking produces larger binaries than static linking", "Static linking requires an internet connection", "Dynamic linking cannot share libraries between processes"],
        "answer": "Static linking includes library code directly into the binary at compile time; dynamic linking resolves references at load/run time",
        "explanation": "Static linking bundles all library code into the final executable, while dynamic linking keeps shared libraries separate (.so / .dll) loaded into memory dynamically."
    }
]
