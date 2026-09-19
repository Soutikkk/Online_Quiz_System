CATEGORY = "Python Programming"

QUESTIONS = [
    # Easy (20)
    {
        "difficulty": "Easy",
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def",
        "explanation": "The 'def' keyword is used to define a function in Python."
    },
    {
        "difficulty": "Easy",
        "question": "Which symbol is used for single-line comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#",
        "explanation": "In Python, the hash character (#) starts a single-line comment."
    },
    {
        "difficulty": "Easy",
        "question": "Which of the following built-in data types in Python is immutable?",
        "options": ["list", "dict", "set", "tuple"],
        "answer": "tuple",
        "explanation": "Tuples, strings, and ints are immutable in Python; lists, dicts, and sets are mutable."
    },
    {
        "difficulty": "Easy",
        "question": "What is the output of `type(5.0)` in Python 3?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'double'>", "<class 'number'>"],
        "answer": "<class 'float'>",
        "explanation": "5.0 is a floating-point number, represented by the class 'float'."
    },
    {
        "difficulty": "Easy",
        "question": "Which function is used to take user input as a string in Python 3?",
        "options": ["input()", "raw_input()", "scanf()", "read()"],
        "answer": "input()",
        "explanation": "In Python 3, `input()` reads a line from standard input and returns it as a string."
    },
    {
        "difficulty": "Easy",
        "question": "How do you calculate exponentiation (e.g., 2 to the power 3) in Python?",
        "options": ["2 ^ 3", "2 ** 3", "2 pow 3", "2 exp 3"],
        "answer": "2 ** 3",
        "explanation": "The `**` operator is Python's exponentiation operator (2 ** 3 = 8)."
    },
    {
        "difficulty": "Easy",
        "question": "Which built-in function returns the number of items in a list or sequence?",
        "options": ["count()", "size()", "len()", "length()"],
        "answer": "len()",
        "explanation": "The `len()` function returns the length (the number of items) of an object."
    },
    {
        "difficulty": "Easy",
        "question": "What is the correct file extension for standard Python files?",
        "options": [".pt", ".py", ".pyt", ".p"],
        "answer": ".py",
        "explanation": "Standard Python source files use the `.py` extension."
    },
    {
        "difficulty": "Easy",
        "question": "Which statement is used to handle exceptions in Python?",
        "options": ["try ... except", "try ... catch", "do ... catch", "try ... handle"],
        "answer": "try ... except",
        "explanation": "Python uses `try ... except` blocks for exception handling."
    },
    {
        "difficulty": "Easy",
        "question": "What is the result of `bool([])` in Python?",
        "options": ["True", "False", "None", "Error"],
        "answer": "False",
        "explanation": "An empty list `[]` evaluates to `False` in a boolean context."
    },
    {
        "difficulty": "Easy",
        "question": "Which collection type stores unique elements in unordered fashion?",
        "options": ["list", "tuple", "set", "array"],
        "answer": "set",
        "explanation": "A `set` in Python contains unique elements with no duplicates and no fixed order."
    },
    {
        "difficulty": "Easy",
        "question": "What is the keyword used to create an anonymous/inline function in Python?",
        "options": ["anonymous", "lambda", "inline", "func"],
        "answer": "lambda",
        "explanation": "The `lambda` keyword creates small, anonymous functions in Python."
    },
    {
        "difficulty": "Easy",
        "question": "What is the output of `\"Hello\" + \" \" + \"World\"`?",
        "options": ["Hello World", "HelloWorld", "Error", "Hello+World"],
        "answer": "Hello World",
        "explanation": "The `+` operator concatenates strings in Python."
    },
    {
        "difficulty": "Easy",
        "question": "Which method is used to add an item to the end of a list?",
        "options": ["add()", "append()", "push()", "insert_last()"],
        "answer": "append()",
        "explanation": "The `.append(item)` method adds a single element to the end of a list."
    },
    {
        "difficulty": "Easy",
        "question": "What value does a function in Python return by default if no return statement is specified?",
        "options": ["0", "False", "None", "empty string"],
        "answer": "None",
        "explanation": "Functions without an explicit return statement return `None` upon reaching the end."
    },
    {
        "difficulty": "Easy",
        "question": "Which operator performs floor (integer) division in Python?",
        "options": ["/", "//", "%", "div"],
        "answer": "//",
        "explanation": "The `//` operator performs floor division, truncating towards negative infinity."
    },
    {
        "difficulty": "Easy",
        "question": "Which keyword is used to import modules in Python?",
        "options": ["include", "using", "import", "require"],
        "answer": "import",
        "explanation": "The `import` statement is used to import modules or packages into the current namespace."
    },
    {
        "difficulty": "Easy",
        "question": "What does the `range(1, 5)` function generate?",
        "options": ["[1, 2, 3, 4, 5]", "[1, 2, 3, 4]", "[0, 1, 2, 3, 4]", "[1, 5]"],
        "answer": "[1, 2, 3, 4]",
        "explanation": "The `range(start, stop)` function produces integers from start up to (but not including) stop."
    },
    {
        "difficulty": "Easy",
        "question": "What is the output of `'python'.upper()`?",
        "options": ["Python", "PYTHON", "PyThOn", "Error"],
        "answer": "PYTHON",
        "explanation": "The `.upper()` method returns a copy of the string converted to uppercase."
    },
    {
        "difficulty": "Easy",
        "question": "Which keyword is used to check if a key exists in a dictionary?",
        "options": ["has", "in", "exists", "contains"],
        "answer": "in",
        "explanation": "The `in` keyword checks membership (e.g. `'key' in my_dict`)."
    },

    # Medium (20)
    {
        "difficulty": "Medium",
        "question": "What is the output of `[x**2 for x in range(4)]` in Python?",
        "options": ["[0, 1, 4, 9]", "[1, 4, 9, 16]", "[0, 1, 4, 9, 16]", "[1, 2, 3, 4]"],
        "answer": "[0, 1, 4, 9]",
        "explanation": "List comprehension squares 0, 1, 2, and 3, resulting in [0, 1, 4, 9]."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between `is` and `==` in Python?",
        "options": ["`is` checks identity (same memory address), `==` checks value equality", "`is` checks value equality, `==` checks identity", "Both are exact synonyms in Python 3", "`is` is used only for numeric types"],
        "answer": "`is` checks identity (same memory address), `==` checks value equality",
        "explanation": "`==` compares whether the contents/values are equal, whereas `is` checks whether two variables refer to the exact same object in memory."
    },
    {
        "difficulty": "Medium",
        "question": "What does the `*args` syntax in a Python function definition allow?",
        "options": ["Accepting any number of positional arguments as a tuple", "Accepting keyword arguments as a dictionary", "Forcing keyword-only arguments", "Passing pointers"],
        "answer": "Accepting any number of positional arguments as a tuple",
        "explanation": "`*args` collects arbitrary positional arguments passed to the function into a tuple."
    },
    {
        "difficulty": "Medium",
        "question": "What does the `**kwargs` syntax in a Python function definition allow?",
        "options": ["Passing double pointers", "Accepting arbitrary keyword arguments as a dictionary", "Multiplying keyword values", "Declaring private methods"],
        "answer": "Accepting arbitrary keyword arguments as a dictionary",
        "explanation": "`**kwargs` captures arbitrary named/keyword arguments into a dictionary."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Python generator function?",
        "options": ["A function that creates random numbers", "A function that uses the `yield` statement to return an iterator one value at a time", "A function that compiles code into bytecode", "A function that cannot take arguments"],
        "answer": "A function that uses the `yield` statement to return an iterator one value at a time",
        "explanation": "A generator function uses `yield` to pause execution and yield items lazily on demand."
    },
    {
        "difficulty": "Medium",
        "question": "What is the output of `list(zip(['a', 'b'], [1, 2]))`?",
        "options": ["[['a', 1], ['b', 2]]", "[('a', 1), ('b', 2)]", "{'a': 1, 'b': 2}", "['a1', 'b2']"],
        "answer": "[('a', 1), ('b', 2)]",
        "explanation": "`zip()` pairs elements from multiple iterables into tuples."
    },
    {
        "difficulty": "Medium",
        "question": "What does the `__init__` method represent in a Python class?",
        "options": ["Class destructor", "Instance initializer / constructor", "Static factory method", "Garbage collector"],
        "answer": "Instance initializer / constructor",
        "explanation": "`__init__` is the constructor method called automatically when a new instance of a class is created."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of the `pass` statement in Python?",
        "options": ["Terminates the program", "Serves as a syntactic placeholder that does nothing when executed", "Passes control to the parent function", "Skips to next iteration of a loop"],
        "answer": "Serves as a syntactic placeholder that does nothing when executed",
        "explanation": "`pass` is a null statement used when syntax requires a statement but no action is needed."
    },
    {
        "difficulty": "Medium",
        "question": "What will `a = [1, 2]; b = a; b.append(3); print(a)` output?",
        "options": ["[1, 2]", "[1, 2, 3]", "[3]", "Error"],
        "answer": "[1, 2, 3]",
        "explanation": "`b = a` assigns the reference; modifying `b` modifies the same list in memory referenced by `a`."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of the `with` statement in Python?",
        "options": ["Imports all functions from a module", "Ensures proper acquisition and release of resources via context managers", "Defines a block with multiple threads", "Enables type safety"],
        "answer": "Ensures proper acquisition and release of resources via context managers",
        "explanation": "`with` ensures clean setup and teardown (e.g. closing files or releasing locks) via `__enter__` and `__exit__` methods."
    },
    {
        "difficulty": "Medium",
        "question": "What is the output of `'hello'[::-1]` in Python?",
        "options": ["'olleh'", "'hello'", "'h'", "Error"],
        "answer": "'olleh'",
        "explanation": "The slice step `-1` reverses the sequence."
    },
    {
        "difficulty": "Medium",
        "question": "What is the Global Interpreter Lock (GIL) in CPython?",
        "options": ["A lock that prevents Python from reading files concurrently", "A mutex that prevents multiple native threads from executing Python bytecodes simultaneously", "A security lock that encrypts Python scripts", "A mechanism to lock variable names"],
        "answer": "A mutex that prevents multiple native threads from executing Python bytecodes simultaneously",
        "explanation": "The GIL is a mutex in CPython that protects access to Python objects, preventing true parallel thread execution of Python bytecode on multi-core CPUs."
    },
    {
        "difficulty": "Medium",
        "question": "How do you achieve shallow copy vs deep copy in Python?",
        "options": ["Using `copy.copy()` and `copy.deepcopy()` from the `copy` module", "Using `clone()` and `duplicate()`", "Using `is` and `==`", "Using `slice()` and `map()`"],
        "answer": "Using `copy.copy()` and `copy.deepcopy()` from the `copy` module",
        "explanation": "The `copy` module provides `copy()` for shallow copying (outer container only) and `deepcopy()` for recursive copying of nested objects."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between a list and a tuple in terms of memory overhead and speed?",
        "options": ["Lists are faster and use less memory", "Tuples are immutable, smaller in memory, and slightly faster to create and iterate", "Both have identical memory footprints", "Tuples cannot be used as function arguments"],
        "answer": "Tuples are immutable, smaller in memory, and slightly faster to create and iterate",
        "explanation": "Because tuples are immutable, Python optimizes their memory allocation and avoids dynamic over-allocation overhead required by mutable lists."
    },
    {
        "difficulty": "Medium",
        "question": "What does `@staticmethod` decorator do in a Python class?",
        "options": ["Makes the method run faster", "Defines a method that does not receive an implicit first argument (`self` or `cls`)", "Prevents the method from being called outside the class", "Creates a singleton instance"],
        "answer": "Defines a method that does not receive an implicit first argument (`self` or `cls`)",
        "explanation": "A static method is bound to the class rather than the object and does not receive implicit `self` or `cls` parameters."
    },
    {
        "difficulty": "Medium",
        "question": "What is the output of `dict.fromkeys(['a', 'b'], 0)`?",
        "options": ["{'a': 0, 'b': 0}", "{0: 'a', 0: 'b'}", "['a': 0, 'b': 0]", "[('a', 0), ('b', 0)]"],
        "answer": "{'a': 0, 'b': 0}",
        "explanation": "`dict.fromkeys(keys, default_value)` creates a new dictionary with specified keys set to the default value."
    },
    {
        "difficulty": "Medium",
        "question": "What does the `enumerate()` function return when iterating over a sequence?",
        "options": ["Only the index", "Only the value", "Tuples containing the index and corresponding value", "A reversed list"],
        "answer": "Tuples containing the index and corresponding value",
        "explanation": "`enumerate(iterable)` yields pairs of `(index, item)` on each iteration."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Python decorator?",
        "options": ["A tool for formatting code style", "A callable that takes a function and returns a modified or enhanced version of that function", "A class decorator for CSS styling", "A GUI widget"],
        "answer": "A callable that takes a function and returns a modified or enhanced version of that function",
        "explanation": "Decorators allow you to wrap or alter the behavior of a callable dynamically using `@decorator_name` syntax."
    },
    {
        "difficulty": "Medium",
        "question": "Which built-in module is used to work with regular expressions in Python?",
        "options": ["regex", "re", "regexp", "patterns"],
        "answer": "re",
        "explanation": "The `re` module provides regular expression matching operations in Python standard library."
    },
    {
        "difficulty": "Medium",
        "question": "What is the output of `set([1, 2, 2, 3, 1])`?",
        "options": ["{1, 2, 3}", "[1, 2, 3]", "{1, 2, 2, 3, 1}", "(1, 2, 3)"],
        "answer": "{1, 2, 3}",
        "explanation": "Sets automatically deduplicate elements, keeping only unique values."
    },

    # Hard (10)
    {
        "difficulty": "Hard",
        "question": "What is the Method Resolution Order (MRO) algorithm used in modern Python (Python 3)?",
        "options": ["Depth First Search (DFS)", "Breadth First Search (BFS)", "C3 Linearization algorithm", "Dijkstra algorithm"],
        "answer": "C3 Linearization algorithm",
        "explanation": "Python 3 uses the C3 Linearization algorithm to determine the Method Resolution Order in multiple inheritance."
    },
    {
        "difficulty": "Hard",
        "question": "What is the purpose of `__slots__` in a Python class definition?",
        "options": ["To define abstract methods", "To explicitly declare data members and prevent the creation of `__dict__`, saving substantial memory", "To restrict class inheritance", "To enable multi-threading"],
        "answer": "To explicitly declare data members and prevent the creation of `__dict__`, saving substantial memory",
        "explanation": "`__slots__` tells Python not to use a dynamic `__dict__` for instance attributes, drastically reducing memory usage per instance."
    },
    {
        "difficulty": "Hard",
        "question": "What is a metaclass in Python?",
        "options": ["A class that inherits from multiple parent classes", "The 'class of a class' that defines how classes themselves are constructed and behave", "A class written in C", "A class that cannot be instantiated"],
        "answer": "The 'class of a class' that defines how classes themselves are constructed and behave",
        "explanation": "Just as an object is an instance of a class, a class is an instance of a metaclass (by default, `type`)."
    },
    {
        "difficulty": "Hard",
        "question": "What is the danger of using a mutable default argument like `def func(lst=[])` in Python?",
        "options": ["It causes a syntax error", "The default list is created once at function definition time and shared across all subsequent invocations", "It converts integers to strings", "It causes stack overflow"],
        "answer": "The default list is created once at function definition time and shared across all subsequent invocations",
        "explanation": "Default arguments are evaluated once when the function is defined, so mutating `lst` modifies the same list across future calls."
    },
    {
        "difficulty": "Hard",
        "question": "How does Python handle memory management and cyclic garbage collection?",
        "options": ["Manual memory management via free()", "Reference counting combined with a generational cyclic garbage collector", "Mark and sweep without reference counts", "Stop-the-world compaction only"],
        "answer": "Reference counting combined with a generational cyclic garbage collector",
        "explanation": "CPython uses reference counting as its primary mechanism and a generational cycle detector to clean up circular references."
    },
    {
        "difficulty": "Hard",
        "question": "What does the `functools.wraps` decorator do when writing custom decorators?",
        "options": ["Compiles the wrapped function to C", "Preserves original function metadata such as `__name__`, `__doc__`, and signature", "Makes the function thread-safe", "Converts positional arguments to keyword arguments"],
        "answer": "Preserves original function metadata such as `__name__`, `__doc__`, and signature",
        "explanation": "`@functools.wraps(func)` copies the name, docstring, arguments list, etc., from the original function to the wrapper function."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between `asyncio.create_task()` and `await coroutine()` in Python?",
        "options": ["`create_task` schedules the coroutine to run concurrently on the event loop, while `await` immediately yields control waiting for it to finish", "`create_task` runs in a separate OS thread", "There is no difference", "`await` creates a new sub-process"],
        "answer": "`create_task` schedules the coroutine to run concurrently on the event loop, while `await` immediately yields control waiting for it to finish",
        "explanation": "`create_task` wraps a coroutine into a Task and schedules it on the event loop concurrently without immediately blocking."
    },
    {
        "difficulty": "Hard",
        "question": "What is the descriptor protocol in Python?",
        "options": ["A way to document code using docstrings", "Objects that define `__get__`, `__set__`, or `__delete__` methods to customize attribute access behavior", "A network socket serialization standard", "A protocol for sorting lists"],
        "answer": "Objects that define `__get__`, `__set__`, or `__delete__` methods to customize attribute access behavior",
        "explanation": "Descriptors power properties, methods, `classmethod`, and `staticmethod` by intercepting dot-lookup attribute access."
    },
    {
        "difficulty": "Hard",
        "question": "In Python, what is the effect of calling `sys.intern(string)`?",
        "options": ["Encrypts the string", "Enters the string into a global table of interned strings so comparisons can use pointer equality (`is`) instead of character comparison", "Deletes the string from RAM", "Converts ASCII to UTF-32"],
        "answer": "Enters the string into a global table of interned strings so comparisons can use pointer equality (`is`) instead of character comparison",
        "explanation": "String interning ensures only one copy of distinct string values is stored, allowing O(1) comparison via pointer equality."
    },
    {
        "difficulty": "Hard",
        "question": "What does `__new__` do differently from `__init__` in a Python class?",
        "options": ["`__new__` destroys the instance, `__init__` initializes it", "`__new__` is the static method responsible for creating and returning the new instance, while `__init__` initializes the newly created instance", "`__new__` is only for private classes", "Both are completely identical"],
        "answer": "`__new__` is the static method responsible for creating and returning the new instance, while `__init__` initializes the newly created instance",
        "explanation": "`__new__` actually allocates and returns the new object (essential for subclassing immutable types and creating singletons), whereas `__init__` initializes its state."
    }
]
