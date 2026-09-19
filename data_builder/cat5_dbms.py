CATEGORY = "DBMS"

QUESTIONS = [
    # Easy (20)
    {
        "difficulty": "Easy",
        "question": "What does DBMS stand for?",
        "options": ["Database Management System", "Data Base Multi System", "Direct Business Management Service", "Data Backup Management Schema"],
        "answer": "Database Management System",
        "explanation": "DBMS stands for Database Management System, software for creating and managing databases."
    },
    {
        "difficulty": "Easy",
        "question": "What does SQL stand for?",
        "options": ["Structured Query Language", "Simple Question Language", "Standard Query Logic", "System Query Link"],
        "answer": "Structured Query Language",
        "explanation": "SQL stands for Structured Query Language, the standard language for relational databases."
    },
    {
        "difficulty": "Easy",
        "question": "Which SQL command is used to retrieve data from a database table?",
        "options": ["GET", "FETCH", "SELECT", "RETRIEVE"],
        "answer": "SELECT",
        "explanation": "The SELECT statement is used to query and extract records from database tables."
    },
    {
        "difficulty": "Easy",
        "question": "Which key uniquely identifies each record in a database table and cannot contain NULL values?",
        "options": ["Primary Key", "Foreign Key", "Candidate Key", "Super Key"],
        "answer": "Primary Key",
        "explanation": "A primary key uniquely identifies each row in a relation and strictly forbids NULL values."
    },
    {
        "difficulty": "Easy",
        "question": "Which key establishes a link between two relational tables?",
        "options": ["Primary Key", "Foreign Key", "Super Key", "Alternate Key"],
        "answer": "Foreign Key",
        "explanation": "A foreign key is a column that references the primary key of another table, enforcing referential integrity."
    },
    {
        "difficulty": "Easy",
        "question": "In the relational model, what is a row in a table called?",
        "options": ["Tuple", "Attribute", "Domain", "Relation"],
        "answer": "Tuple",
        "explanation": "In relational calculus and theory, a row of a table is referred to as a Tuple."
    },
    {
        "difficulty": "Easy",
        "question": "In the relational model, what is a column in a table called?",
        "options": ["Tuple", "Attribute", "Record", "Schema"],
        "answer": "Attribute",
        "explanation": "Columns in a relational table represent properties called Attributes."
    },
    {
        "difficulty": "Easy",
        "question": "What does ACID stand for in database transaction management?",
        "options": ["Atomicity, Consistency, Isolation, Durability", "Accuracy, Control, Integration, Design", "Access, Concurrency, Indexing, Data", "Automated, Consistent, Isolated, Distributed"],
        "answer": "Atomicity, Consistency, Isolation, Durability",
        "explanation": "ACID properties ensure reliable processing of database transactions."
    },
    {
        "difficulty": "Easy",
        "question": "Which SQL clause is used to filter records matching specified conditions?",
        "options": ["WHERE", "HAVING", "ORDER BY", "GROUP BY"],
        "answer": "WHERE",
        "explanation": "The WHERE clause filters rows based on a given boolean condition before aggregation."
    },
    {
        "difficulty": "Easy",
        "question": "Which SQL command is used to insert new records into a table?",
        "options": ["ADD RECORD", "INSERT INTO", "PUT", "UPDATE"],
        "answer": "INSERT INTO",
        "explanation": "The `INSERT INTO table_name VALUES (...)` statement adds new rows to a table."
    },
    {
        "difficulty": "Easy",
        "question": "Which SQL command deletes all records from a table while maintaining the table structure without logging individual row deletions?",
        "options": ["DELETE", "DROP", "TRUNCATE", "REMOVE"],
        "answer": "TRUNCATE",
        "explanation": "TRUNCATE is a DDL command that quickly deallocates table data pages without individual row-level rollback logging."
    },
    {
        "difficulty": "Easy",
        "question": "Which SQL clause sorts the retrieved result set in ascending or descending order?",
        "options": ["GROUP BY", "SORT BY", "ORDER BY", "ARRANGE BY"],
        "answer": "ORDER BY",
        "explanation": "ORDER BY sorts the returned rows by one or more columns (ASC or DESC)."
    },
    {
        "difficulty": "Easy",
        "question": "What type of SQL sublanguage do `CREATE`, `ALTER`, and `DROP` belong to?",
        "options": ["DML (Data Manipulation Language)", "DDL (Data Definition Language)", "DCL (Data Control Language)", "TCL (Transaction Control Language)"],
        "answer": "DDL (Data Definition Language)",
        "explanation": "DDL commands define and modify the schema and structure of database objects."
    },
    {
        "difficulty": "Easy",
        "question": "What type of SQL sublanguage do `COMMIT` and `ROLLBACK` belong to?",
        "options": ["DML", "DDL", "DCL", "TCL (Transaction Control Language)"],
        "answer": "TCL (Transaction Control Language)",
        "explanation": "TCL commands manage changes made by DML statements to maintain transaction integrity."
    },
    {
        "difficulty": "Easy",
        "question": "Which SQL aggregate function calculates the average value of a numeric column?",
        "options": ["COUNT()", "AVG()", "SUM()", "MEAN()"],
        "answer": "AVG()",
        "explanation": "The AVG() function returns the arithmetic mean of numeric column values."
    },
    {
        "difficulty": "Easy",
        "question": "What is an Entity-Relationship (ER) diagram used for?",
        "options": ["Visualizing logical database structure and relationships between entities", "Tracking network bandwidth", "Writing SQL triggers", "Compiling query plans"],
        "answer": "Visualizing logical database structure and relationships between entities",
        "explanation": "ER diagrams represent entities, attributes, and relationships conceptually during database design."
    },
    {
        "difficulty": "Easy",
        "question": "Which symbol represents an entity in a standard Chen ER diagram?",
        "options": ["Rectangle", "Ellipse", "Diamond", "Double Ellipse"],
        "answer": "Rectangle",
        "explanation": "In Chen's ER notation, rectangles represent entities, ellipses represent attributes, and diamonds represent relationships."
    },
    {
        "difficulty": "Easy",
        "question": "Which normal form requires the elimination of repeating groups and atomic attribute values?",
        "options": ["First Normal Form (1NF)", "Second Normal Form (2NF)", "Third Normal Form (3NF)", "Boyce-Codd Normal Form (BCNF)"],
        "answer": "First Normal Form (1NF)",
        "explanation": "1NF requires that each column contain only atomic (indivisible) values and each row be unique."
    },
    {
        "difficulty": "Easy",
        "question": "Which constraint ensures that all values in a column are distinct?",
        "options": ["NOT NULL", "UNIQUE", "CHECK", "DEFAULT"],
        "answer": "UNIQUE",
        "explanation": "The UNIQUE constraint prevents duplicate values in a column or set of columns."
    },
    {
        "difficulty": "Easy",
        "question": "Which SQL command is used to permanently delete an entire table and its schema from the database?",
        "options": ["DELETE TABLE", "DROP TABLE", "REMOVE TABLE", "CLEAR TABLE"],
        "answer": "DROP TABLE",
        "explanation": "DROP TABLE deletes both the data and the structural definition of the table from the database catalog."
    },

    # Medium (20)
    {
        "difficulty": "Medium",
        "question": "What is the requirement for a relation to be in Second Normal Form (2NF)?",
        "options": ["It must be in 1NF and have no partial functional dependencies on candidate keys", "It must have no transitive dependencies", "It must have multi-valued dependencies resolved", "It must contain at most 3 tables"],
        "answer": "It must be in 1NF and have no partial functional dependencies on candidate keys",
        "explanation": "2NF requires 1NF compliance and that no non-prime attribute is partially dependent on any proper subset of a composite candidate key."
    },
    {
        "difficulty": "Medium",
        "question": "What is the requirement for a relation to be in Third Normal Form (3NF)?",
        "options": ["It must be in 2NF and have no transitive functional dependencies of non-prime attributes on candidate keys", "Every determinant must be a candidate key", "All foreign keys must be null", "It must be in BCNF"],
        "answer": "It must be in 2NF and have no transitive functional dependencies of non-prime attributes on candidate keys",
        "explanation": "3NF eliminates transitive dependencies where a non-prime attribute depends on another non-prime attribute."
    },
    {
        "difficulty": "Medium",
        "question": "What is Boyce-Codd Normal Form (BCNF)?",
        "options": ["A stronger version of 3NF where for every functional dependency X -> Y, X must be a super key", "A normal form allowing multi-valued attributes", "A normal form that replaces 1NF", "A normal form for non-relational databases"],
        "answer": "A stronger version of 3NF where for every functional dependency X -> Y, X must be a super key",
        "explanation": "BCNF eliminates all redundancy from functional dependencies by requiring every determinant X in X -> Y to be a super key."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between `HAVING` and `WHERE` clauses in SQL?",
        "options": ["`WHERE` filters rows before grouping; `HAVING` filters aggregate groups after `GROUP BY`", "`HAVING` can only be used with numbers", "`WHERE` is used only after `GROUP BY`", "There is no difference"],
        "answer": "`WHERE` filters rows before grouping; `HAVING` filters aggregate groups after `GROUP BY`",
        "explanation": "`WHERE` filters individual rows prior to aggregation, while `HAVING` applies filtering on grouped and aggregated results."
    },
    {
        "difficulty": "Medium",
        "question": "What does an `INNER JOIN` between two tables return?",
        "options": ["All rows from both tables", "Only rows that have matching values in both tables based on the join condition", "All rows from the left table and NULLs from right", "A Cartesian product of all rows"],
        "answer": "Only rows that have matching values in both tables based on the join condition",
        "explanation": "INNER JOIN combines rows from two tables where there is a match on the specified join predicate."
    },
    {
        "difficulty": "Medium",
        "question": "What does a `LEFT OUTER JOIN` return?",
        "options": ["All rows from the left table, along with matched rows from right table (and NULL for unmatched right rows)", "Only unmatched rows from left table", "Only matching rows", "All rows from right table only"],
        "answer": "All rows from the left table, along with matched rows from right table (and NULL for unmatched right rows)",
        "explanation": "LEFT JOIN returns all records from the left table and the matched records from the right table; unmatched right fields return NULL."
    },
    {
        "difficulty": "Medium",
        "question": "What is a view in SQL?",
        "options": ["A virtual table based on the result-set of an SQL query", "A physical file stored separately on disk", "A hardware graphics buffer", "A primary key constraint"],
        "answer": "A virtual table based on the result-set of an SQL query",
        "explanation": "A view is a stored query that behaves like a virtual table without storing data redundantly."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between clustered and non-clustered indexes?",
        "options": ["A clustered index physically sorts table rows on disk (max 1 per table); non-clustered index stores pointers to rows (multiple allowed)", "Non-clustered indexes physically rearrange data", "Clustered indexes can only be created on text columns", "Non-clustered indexes take zero storage"],
        "answer": "A clustered index physically sorts table rows on disk (max 1 per table); non-clustered index stores pointers to rows (multiple allowed)",
        "explanation": "A clustered index dictates the physical storage order of the data on disk, allowing only one per table."
    },
    {
        "difficulty": "Medium",
        "question": "What is the Dirty Read problem in database transactions?",
        "options": ["When a transaction reads uncommitted data written by another concurrent transaction that later rolls back", "When two transactions insert identical primary keys", "When disk sectors are corrupt", "When a transaction reads twice and gets different committed values"],
        "answer": "When a transaction reads uncommitted data written by another concurrent transaction that later rolls back",
        "explanation": "A dirty read occurs when transaction T1 reads data modified by T2 that has not yet been committed."
    },
    {
        "difficulty": "Medium",
        "question": "Which transaction isolation level prevents Dirty Reads but still allows Non-Repeatable Reads?",
        "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
        "answer": "Read Committed",
        "explanation": "Read Committed guarantees that any data read was committed at the moment it is read, preventing dirty reads."
    },
    {
        "difficulty": "Medium",
        "question": "What is a database Trigger?",
        "options": ["A procedural code block that automatically executes in response to specified database events (INSERT, UPDATE, DELETE)", "A shortcut key in database GUI", "A hardware interrupt from storage controller", "A command to restart the database engine"],
        "answer": "A procedural code block that automatically executes in response to specified database events (INSERT, UPDATE, DELETE)",
        "explanation": "Triggers are special stored procedures that run automatically when an event occurs in the database server."
    },
    {
        "difficulty": "Medium",
        "question": "What is Write-Ahead Logging (WAL) in database recovery?",
        "options": ["Writing log records to persistent disk storage before corresponding changes are written to the database pages", "Writing data before user presses enter", "Backing up tables to remote servers weekly", "Writing queries in uppercase letters"],
        "answer": "Writing log records to persistent disk storage before corresponding changes are written to the database pages",
        "explanation": "WAL guarantees Atomicity and Durability by ensuring log records are flushed to non-volatile disk before dirty data pages."
    },
    {
        "difficulty": "Medium",
        "question": "What is a natural join in relational algebra?",
        "options": ["A join that matches tuples based on all columns having common attribute names and removes duplicate columns", "A cross product without conditions", "A join that selects only odd-numbered rows", "A join on primary keys only"],
        "answer": "A join that matches tuples based on all columns having common attribute names and removes duplicate columns",
        "explanation": "Natural join (⋈) equates all columns with identical names in both relations and retains only one copy of each common attribute."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of Checkpoint in database recovery systems?",
        "options": ["To flush all dirty log and data buffers to disk so recovery doesn't have to scan the entire log from the beginning", "To pause all incoming user connections", "To validate table schema syntax", "To clean up expired user passwords"],
        "answer": "To flush all dirty log and data buffers to disk so recovery doesn't have to scan the entire log from the beginning",
        "explanation": "Checkpoints bound the recovery time by writing all dirty buffer pages to disk and writing a checkpoint record to log."
    },
    {
        "difficulty": "Medium",
        "question": "What does Cardinality refer to in database relations?",
        "options": ["The number of columns in a table", "The number of tuples (rows) in a relation", "The storage size of index files", "The version number of SQL engine"],
        "answer": "The number of tuples (rows) in a relation",
        "explanation": "Cardinality is the total count of tuples (rows) in a relation; Degree refers to the number of attributes (columns)."
    },
    {
        "difficulty": "Medium",
        "question": "What is the degree (or arity) of a table in relational database terminology?",
        "options": ["The number of rows", "The number of columns (attributes)", "The count of foreign key links", "The depth of B-tree index"],
        "answer": "The number of columns (attributes)",
        "explanation": "The degree (arity) of a relation is the number of attributes (columns) it contains."
    },
    {
        "difficulty": "Medium",
        "question": "What does the Two-Phase Locking (2PL) protocol guarantee?",
        "options": ["Deadlock-free execution", "Conflict serializability of concurrent schedules", "Instant query execution", "Zero disk usage"],
        "answer": "Conflict serializability of concurrent schedules",
        "explanation": "Strict or basic 2PL guarantees serializability by dividing lock operations into Growing (acquiring) and Shrinking (releasing) phases."
    },
    {
        "difficulty": "Medium",
        "question": "What is the Phantom Read phenomenon?",
        "options": ["When a transaction re-executes a range query and finds rows that were inserted/deleted by another committed transaction", "When the server shuts down during reading", "When NULL values turn into zeros", "When reading from an empty table"],
        "answer": "When a transaction re-executes a range query and finds rows that were inserted/deleted by another committed transaction",
        "explanation": "Phantom reads happen when range queries return different sets of matching rows due to concurrent inserts/deletes."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Stored Procedure in SQL databases?",
        "options": ["A prepared SQL code segment that can be saved and reused across multiple client calls", "A backup copy of raw SQL files", "A physical hard drive partition", "A temporary table created during joins"],
        "answer": "A prepared SQL code segment that can be saved and reused across multiple client calls",
        "explanation": "Stored procedures are compiled subroutines stored in the database catalog that encapsulate reusable business logic."
    },
    {
        "difficulty": "Medium",
        "question": "What is the result of `SELECT COUNT(*)` on a table with 5 rows where one row contains NULL in all columns?",
        "options": ["4", "5", "0", "NULL"],
        "answer": "5",
        "explanation": "`COUNT(*)` counts the total number of rows in the table regardless of whether columns contain NULL values."
    },

    # Hard (10)
    {
        "difficulty": "Hard",
        "question": "What is the Strict Two-Phase Locking (Strict 2PL) protocol?",
        "options": ["A 2PL protocol where all exclusive (X) locks acquired by a transaction are held until transaction commits or aborts", "A protocol that releases locks immediately after each read", "A protocol requiring locks to be acquired in ascending ID order", "A lock-free protocol using timestamps"],
        "answer": "A 2PL protocol where all exclusive (X) locks acquired by a transaction are held until transaction commits or aborts",
        "explanation": "Strict 2PL holds all exclusive locks until end-of-transaction (EOT) to prevent cascading aborts/rollbacks."
    },
    {
        "difficulty": "Hard",
        "question": "In the ARIES recovery algorithm, what are the three main phases executed during database crash recovery?",
        "options": ["Analysis, Redo, and Undo", "Scan, Parse, and Execute", "Check, Lock, and Commit", "Verify, Clean, and Flush"],
        "answer": "Analysis, Redo, and Undo",
        "explanation": "ARIES recovery performs Analysis (identifies dirty pages and active transactions), Redo (repeats history to crash state), and Undo (rolls back uncommitted transactions)."
    },
    {
        "difficulty": "Hard",
        "question": "What is the primary difference between a B-Tree and a B+ Tree index in relational databases?",
        "options": ["In a B+ Tree, data pointers are stored only in leaf nodes and leaf nodes are linked sequentially; B-Tree stores data keys in internal nodes as well", "B-Tree leaves are always linked in a doubly linked list", "B+ Trees cannot handle range queries", "B-Trees have greater fan-out than B+ Trees"],
        "answer": "In a B+ Tree, data pointers are stored only in leaf nodes and leaf nodes are linked sequentially; B-Tree stores data keys in internal nodes as well",
        "explanation": "B+ Trees store all actual record pointers in leaf nodes linked as a list, maximizing internal node fan-out and speeding range scans."
    },
    {
        "difficulty": "Hard",
        "question": "What is Multi-Version Concurrency Control (MVCC)?",
        "options": ["A concurrency control mechanism where readers do not block writers and writers do not block readers by maintaining multiple snapshot versions of rows", "A system where transactions run on multiple databases simultaneously", "A locking mechanism that uses 4-phase locks", "A database replication backup system"],
        "answer": "A concurrency control mechanism where readers do not block writers and writers do not block readers by maintaining multiple snapshot versions of rows",
        "explanation": "MVCC provides snapshot isolation by creating new versions of updated rows, enabling concurrent non-blocking reads and writes."
    },
    {
        "difficulty": "Hard",
        "question": "What is a Lossless-Join Decomposition in database normalization?",
        "options": ["Decomposing relation R into R1 and R2 such that natural join of R1 and R2 equals original relation R without generating spurious tuples", "A decomposition that loses duplicate rows", "A join that runs in O(1) time", "Decomposing into non-overlapping primary keys"],
        "answer": "Decomposing relation R into R1 and R2 such that natural join of R1 and R2 equals original relation R without generating spurious tuples",
        "explanation": "Lossless join ensures R1 ⋈ R2 = R, which holds if R1 ∩ R2 -> R1 or R1 ∩ R2 -> R2."
    },
    {
        "difficulty": "Hard",
        "question": "What does Dependency Preservation in database normalization guarantee?",
        "options": ["All functional dependencies in the original relation can be checked by inspecting individual decomposed relations without performing joins", "No foreign keys can ever be deleted", "Every table preserves 100% of candidate keys", "Foreign keys cannot have cascade delete"],
        "answer": "All functional dependencies in the original relation can be checked by inspecting individual decomposed relations without performing joins",
        "explanation": "Dependency preservation ensures the union of FDs on decomposed relations logically implies all FDs in the original relation."
    },
    {
        "difficulty": "Hard",
        "question": "In distributed database transactions, what is the role of the Two-Phase Commit (2PC) protocol?",
        "options": ["To ensure atomic commitment across distributed participant nodes via Prepare and Commit phases", "To execute queries in two CPU clock cycles", "To prevent SQL injection attacks", "To synchronize local caching with RAM"],
        "answer": "To ensure atomic commitment across distributed participant nodes via Prepare and Commit phases",
        "explanation": "2PC coordinates all distributed database nodes to either all commit or all abort a transaction consistently."
    },
    {
        "difficulty": "Hard",
        "question": "What is the difference between Conflict Serializability and View Serializability?",
        "options": ["Every conflict serializable schedule is view serializable, but not all view serializable schedules are conflict serializable (due to blind writes)", "View serializability can be checked in polynomial time O(N^2)", "Conflict serializability allows cycles in serialization graph", "They are mathematically identical"],
        "answer": "Every conflict serializable schedule is view serializable, but not all view serializable schedules are conflict serializable (due to blind writes)",
        "explanation": "Conflict serializability is a stricter subset that can be verified in polynomial time using precedence graphs; view serializability testing is NP-complete."
    },
    {
        "difficulty": "Hard",
        "question": "What is the Write-Skew anomaly under Snapshot Isolation in databases?",
        "options": ["Two concurrent transactions read overlapping data, make disjoint updates based on that data, and violate a global integrity constraint", "Writing data to wrong hard drive sectors", "When two writers deadlock on the same lock", "When a transaction reads corrupted dirty pages"],
        "answer": "Two concurrent transactions read overlapping data, make disjoint updates based on that data, and violate a global integrity constraint",
        "explanation": "Write skew happens when concurrent transactions satisfy local constraints based on snapshot reads, but their combined updates violate global constraints."
    },
    {
        "difficulty": "Hard",
        "question": "What is the purpose of Cost-Based Query Optimization (CBO) in modern database engines?",
        "options": ["Estimating physical I/O and CPU costs for multiple candidate execution plans using data distribution histograms to select the lowest-cost plan", "Calculating billing costs for cloud servers", "Measuring disk wear and tear", "Minimizing lines of SQL source code"],
        "answer": "Estimating physical I/O and CPU costs for multiple candidate execution plans using data distribution histograms to select the lowest-cost plan",
        "explanation": "CBO evaluates alternative relational algebra operator trees and join algorithms using catalog statistics/histograms to pick the optimal execution plan."
    }
]
