CATEGORY = "Software Engineering"

QUESTIONS = [
    # Easy (12)
    {
        "difficulty": "Easy",
        "question": "What does SDLC stand for in software engineering?",
        "options": ["Software Development Life Cycle", "System Design and Logic Control", "Standard Development Language Code", "Software Delivery and Launch Cycle"],
        "answer": "Software Development Life Cycle",
        "explanation": "SDLC stands for Software Development Life Cycle, the structured process used by the software industry to design, develop, and test high-quality software."
    },
    {
        "difficulty": "Easy",
        "question": "Which traditional SDLC model follows a strict linear sequential flow from requirements to maintenance?",
        "options": ["Waterfall Model", "Agile Model", "Spiral Model", "RAD Model"],
        "answer": "Waterfall Model",
        "explanation": "The Waterfall model is a classic linear-sequential lifecycle where each phase must be completed before the next begins."
    },
    {
        "difficulty": "Easy",
        "question": "What does SRS stand for in requirement engineering?",
        "options": ["Software Requirements Specification", "System Release Schedule", "Software Resource Standard", "Standard Requirements Sheet"],
        "answer": "Software Requirements Specification",
        "explanation": "An SRS document describes the functional and non-functional requirements of a software system to be built."
    },
    {
        "difficulty": "Easy",
        "question": "Which testing level focuses on verifying individual functions, methods, or modules in isolation?",
        "options": ["Unit Testing", "Integration Testing", "System Testing", "Acceptance Testing"],
        "answer": "Unit Testing",
        "explanation": "Unit testing tests individual units or components of software in isolation to ensure each part functions correctly."
    },
    {
        "difficulty": "Easy",
        "question": "What is Black-Box Testing?",
        "options": ["Testing software functionality without knowledge of its internal code structure or implementation", "Testing with internal source code visible", "Testing in dark rooms", "Testing server power supplies"],
        "answer": "Testing software functionality without knowledge of its internal code structure or implementation",
        "explanation": "Black-box testing focuses solely on inputs and expected outputs without looking at the internal code."
    },
    {
        "difficulty": "Easy",
        "question": "What is White-Box (Glass-Box) Testing?",
        "options": ["Testing that examines internal code structures, logic paths, and implementation details", "Testing by external end-users", "Testing without reading source code", "Testing UI mockups"],
        "answer": "Testing that examines internal code structures, logic paths, and implementation details",
        "explanation": "White-box testing uses knowledge of internal program logic, data flows, and statement coverage."
    },
    {
        "difficulty": "Easy",
        "question": "What is Git in software engineering?",
        "options": ["A Distributed Version Control System (DVCS)", "A programming language compiler", "A database server", "An operating system"],
        "answer": "A Distributed Version Control System (DVCS)",
        "explanation": "Git is a distributed version control system for tracking changes in source code during software development."
    },
    {
        "difficulty": "Easy",
        "question": "In Agile Scrum methodology, what is a time-boxed iteration typically lasting 1 to 4 weeks called?",
        "options": ["Sprint", "Milestone", "Release", "Epic"],
        "answer": "Sprint",
        "explanation": "A Sprint is a repeatable time-boxed period during which a specific set of work is completed and made ready for review."
    },
    {
        "difficulty": "Easy",
        "question": "What is Regression Testing?",
        "options": ["Re-running functional and non-functional tests to ensure previously working software still works after code modifications", "Testing beta software on new users", "Testing hardware degradation", "Testing performance on older OS versions"],
        "answer": "Re-running functional and non-functional tests to ensure previously working software still works after code modifications",
        "explanation": "Regression testing ensures that bug fixes or new features have not inadvertently broken existing functionality."
    },
    {
        "difficulty": "Easy",
        "question": "Which role in Scrum represents the voice of the customer and manages the product backlog?",
        "options": ["Product Owner", "Scrum Master", "Development Team Lead", "QA Manager"],
        "answer": "Product Owner",
        "explanation": "The Product Owner is responsible for maximizing product value and managing the prioritized Product Backlog."
    },
    {
        "difficulty": "Easy",
        "question": "What is Refactoring in software development?",
        "options": ["Restructuring existing code without changing its external observable behavior to improve readability and maintainability", "Rewriting code in a completely new language", "Fixing critical production outages", "Deleting test cases"],
        "answer": "Restructuring existing code without changing its external observable behavior to improve readability and maintainability",
        "explanation": "Refactoring improves non-functional attributes of software (design, readability, complexity) while preserving existing functionality."
    },
    {
        "difficulty": "Easy",
        "question": "What does CI/CD stand for in modern DevOps pipelines?",
        "options": ["Continuous Integration / Continuous Delivery (or Deployment)", "Code Inspection / Code Debugging", "Central Interface / Central Database", "Component Integration / Component Development"],
        "answer": "Continuous Integration / Continuous Delivery (or Deployment)",
        "explanation": "CI/CD automates code integration, automated testing, and software deployment to production environments."
    },

    # Medium (12)
    {
        "difficulty": "Medium",
        "question": "What is the desired relationship between Cohesion and Coupling in well-architected software systems?",
        "options": ["High Cohesion and Low Coupling", "Low Cohesion and High Coupling", "High Cohesion and High Coupling", "Low Cohesion and Low Coupling"],
        "answer": "High Cohesion and Low Coupling",
        "explanation": "High cohesion ensures a module focuses on a single well-defined task, while low coupling minimizes interdependencies between modules."
    },
    {
        "difficulty": "Medium",
        "question": "What is Cyclomatic Complexity in software metrics?",
        "options": ["A quantitative measure of the number of linearly independent paths through a program's source code", "The number of lines of source code", "The CPU cycle count to run a function", "The number of classes in a package"],
        "answer": "A quantitative measure of the number of linearly independent paths through a program's source code",
        "explanation": "McCabe's Cyclomatic Complexity `M = E - N + 2P` measures control flow complexity and the minimum test cases needed for full branch coverage."
    },
    {
        "difficulty": "Medium",
        "question": "What are the SOLID principles in Object-Oriented Design?",
        "options": ["Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion", "Security, Optimization, Logging, Integration, Deployment", "Speed, Objectivity, Linearity, Inheritance, Delegation", "Scalable, Observable, Logical, Isolated, Dynamic"],
        "answer": "Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion",
        "explanation": "SOLID is a mnemonic acronym for 5 design principles intended to make software designs more understandable, flexible, and maintainable."
    },
    {
        "difficulty": "Medium",
        "question": "What does the Open/Closed Principle (in SOLID) state?",
        "options": ["Software entities should be open for extension, but closed for modification", "Source code must be open source but closed for commercial use", "Functions should open database connections and close them immediately", "Files should be opened in binary mode"],
        "answer": "Software entities should be open for extension, but closed for modification",
        "explanation": "Open/Closed principle means you should be able to extend class behavior without altering its existing source code (using polymorphism/interfaces)."
    },
    {
        "difficulty": "Medium",
        "question": "Which design pattern ensures a class has only one instance and provides a global access point to it?",
        "options": ["Singleton Pattern", "Factory Pattern", "Observer Pattern", "Strategy Pattern"],
        "answer": "Singleton Pattern",
        "explanation": "The Singleton pattern restricts instantiation of a class to one single shared object instance."
    },
    {
        "difficulty": "Medium",
        "question": "Which design pattern defines a one-to-many dependency between objects so that when one object changes state, all dependents are notified automatically?",
        "options": ["Observer Pattern", "Adapter Pattern", "Decorator Pattern", "Facade Pattern"],
        "answer": "Observer Pattern",
        "explanation": "The Observer pattern is a behavioral pattern where subject objects broadcast state changes to registered observers (publish-subscribe)."
    },
    {
        "difficulty": "Medium",
        "question": "What is the primary characteristic of the Spiral Model in SDLC?",
        "options": ["Risk-driven approach combining iterative development with systematic risk assessment at each loop", "Strict non-iterative phase transitions", "Zero documentation requirements", "Automatic code generation"],
        "answer": "Risk-driven approach combining iterative development with systematic risk assessment at each loop",
        "explanation": "Boehm's Spiral model is risk-driven, adopting spiral iterations with explicit risk identification, resolution, and prototyping."
    },
    {
        "difficulty": "Medium",
        "question": "What is Boundary Value Analysis (BVA) in black-box test design?",
        "options": ["Testing edge cases at and immediately around the boundaries of input domains (e.g. min, min+1, max-1, max)", "Testing RAM memory allocation limits", "Testing internet bandwidth boundaries", "Measuring source code indentation margins"],
        "answer": "Testing edge cases at and immediately around the boundaries of input domains (e.g. min, min+1, max-1, max)",
        "explanation": "BVA focuses test cases on input domain boundaries where coding errors (such as off-by-one errors) most frequently occur."
    },
    {
        "difficulty": "Medium",
        "question": "What is Equivalence Partitioning?",
        "options": ["Dividing input data into valid and invalid partitions from which test cases are sampled, assuming all values in a partition behave identically", "Splitting code across multiple CPU cores", "Partitioning hard drives equally", "Dividing team tasks equally"],
        "answer": "Dividing input data into valid and invalid partitions from which test cases are sampled, assuming all values in a partition behave identically",
        "explanation": "Equivalence partitioning groups inputs into equivalence classes to minimize redundant test cases while maintaining test coverage."
    },
    {
        "difficulty": "Medium",
        "question": "What is the COCOMO (Constructive Cost Model) used for?",
        "options": ["Estimating software project effort, cost, and schedule based on size (KLOC - Kilo Lines of Code)", "Measuring compiler optimization speed", "Estimating database query performance", "Calculating UI render latency"],
        "answer": "Estimating software project effort, cost, and schedule based on size (KLOC - Kilo Lines of Code)",
        "explanation": "COCOMO is an algorithmic software cost estimation model developed by Barry Boehm based on regression formulas."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of the Adapter Design Pattern?",
        "options": ["Converting the interface of a class into another interface that clients expect, allowing incompatible interfaces to work together", "Caching database queries", "Encrypting communication streams", "Creating deep copies of objects"],
        "answer": "Converting the interface of a class into another interface that clients expect, allowing incompatible interfaces to work together",
        "explanation": "The Adapter (wrapper) pattern bridges two incompatible interfaces without altering their underlying source code."
    },
    {
        "difficulty": "Medium",
        "question": "What is Test-Driven Development (TDD) cycle?",
        "options": ["Red-Green-Refactor: Write a failing test, write minimal code to make it pass, then clean up and refactor", "Write all code first, test at delivery", "Generate tests with AI", "Test only in production"],
        "answer": "Red-Green-Refactor: Write a failing test, write minimal code to make it pass, then clean up and refactor",
        "explanation": "TDD follows Red (failing unit test), Green (minimal code to pass test), and Refactor (optimizing structure)."
    },

    # Hard (6)
    {
        "difficulty": "Hard",
        "question": "What is Mutation Testing in software quality assurance?",
        "options": ["Systematically introducing small artificial faults (mutants) into source code to evaluate the effectiveness and fault-detection capability of a test suite", "Testing genetic algorithms", "Fuzzing network packets randomly", "Testing across biological data sets"],
        "answer": "Systematically introducing small artificial faults (mutants) into source code to evaluate the effectiveness and fault-detection capability of a test suite",
        "explanation": "Mutation testing measures test suite quality (mutation score) by checking whether tests fail when small syntactical mutants are seeded into the codebase."
    },
    {
        "difficulty": "Hard",
        "question": "What is the Liskov Substitution Principle (LSP) formal definition?",
        "options": ["If S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desirable properties of the program", "Child classes must inherit all parent methods as final", "Classes should not implement more than one interface", "Subclasses must override private methods"],
        "answer": "If S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desirable properties of the program",
        "explanation": "LSP ensures behavioral subtyping: derived classes must extend base class behavior without violating pre-conditions, post-conditions, or invariants."
    },
    {
        "difficulty": "Hard",
        "question": "What is Technical Debt in software engineering?",
        "options": ["The implied cost of additional future rework caused by choosing an easy/expedient limited solution now instead of using a better approach that takes longer", "Money owed to cloud hosting providers", "Unpaid licensing fees for software libraries", "The financial cost of purchasing development hardware"],
        "answer": "The implied cost of additional future rework caused by choosing an easy/expedient limited solution now instead of using a better approach that takes longer",
        "explanation": "Ward Cunningham coined Technical Debt to describe the compounding maintenance cost incurred when short-term hacks are implemented over robust designs."
    },
    {
        "difficulty": "Hard",
        "question": "In software architecture, what is the Strangler Fig Application Pattern?",
        "options": ["Incrementally migrating a legacy monolithic application by gradually replacing specific features with microservices until the legacy system is completely superseded", "Killing deadlocked threads forcibly", "Compressing database logs", "Throttling malicious DDoS connections"],
        "answer": "Incrementally migrating a legacy monolithic application by gradually replacing specific features with microservices until the legacy system is completely superseded",
        "explanation": "The Strangler Fig pattern allows low-risk refactoring of monolithic systems by intercepting calls and directing them to new microservices piece-by-piece."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between Verification and Validation in software engineering (Boehm's definition)?",
        "options": ["Verification: 'Are we building the product right?' (conformance to specs); Validation: 'Are we building the right product?' (meeting user needs)", "Verification is done by users; Validation is done by compilers", "They are exact synonyms in IEEE standards", "Verification is dynamic testing; Validation is static code analysis only"],
        "answer": "Verification: 'Are we building the product right?' (conformance to specs); Validation: 'Are we building the right product?' (meeting user needs)",
        "explanation": "Verification checks process and technical conformance to specifications; Validation assesses whether the system fulfills intended customer purpose."
    },
    {
        "difficulty": "Hard",
        "question": "What does Conway's Law state regarding software architecture and organization?",
        "options": ["Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations", "Software bugs double every 18 months", "Every large software system will exceed its initial budget", "Code complexity grows exponentially with team size"],
        "answer": "Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations",
        "explanation": "Conway's Law notes that system architecture inevitably mirrors the social communication boundaries and structure of the teams creating it."
    }
]
