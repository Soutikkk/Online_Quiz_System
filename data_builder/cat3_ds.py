CATEGORY = "Data Structures"

QUESTIONS = [
    # Easy (20)
    {
        "difficulty": "Easy",
        "question": "Which data structure follows the Last-In-First-Out (LIFO) principle?",
        "options": ["Queue", "Stack", "Array", "Linked List"],
        "answer": "Stack",
        "explanation": "A Stack follows the LIFO principle where the last inserted element is popped first."
    },
    {
        "difficulty": "Easy",
        "question": "Which data structure follows the First-In-First-Out (FIFO) principle?",
        "options": ["Queue", "Stack", "Tree", "Graph"],
        "answer": "Queue",
        "explanation": "A Queue operates on the FIFO principle where elements are dequeued in the order they were enqueued."
    },
    {
        "difficulty": "Easy",
        "question": "What is the time complexity to access an element by index in a standard static array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "answer": "O(1)",
        "explanation": "Arrays provide constant time O(1) random access using base address + index * element_size formula."
    },
    {
        "difficulty": "Easy",
        "question": "In a singly linked list, what does each node contain?",
        "options": ["Only data", "Data and a pointer/reference to the next node", "Data and pointers to both next and previous nodes", "Only pointers"],
        "answer": "Data and a pointer/reference to the next node",
        "explanation": "A singly linked list node contains a data field and a next pointer to the subsequent node."
    },
    {
        "difficulty": "Easy",
        "question": "What is the term for a tree where every node has at most two children?",
        "options": ["Binary Tree", "Trie", "B-Tree", "AVL Tree"],
        "answer": "Binary Tree",
        "explanation": "A Binary Tree is a hierarchical structure where each node has at most two children (left and right)."
    },
    {
        "difficulty": "Easy",
        "question": "What is the maximum number of children a node can have in a binary tree?",
        "options": ["1", "2", "3", "Unlimited"],
        "answer": "2",
        "explanation": "By definition, a binary tree node can have at most 2 child nodes."
    },
    {
        "difficulty": "Easy",
        "question": "Which data structure is primarily used to implement Breadth-First Search (BFS) on graphs?",
        "options": ["Stack", "Queue", "Binary Heap", "Hash Table"],
        "answer": "Queue",
        "explanation": "BFS explores neighbors level-by-level using a FIFO Queue."
    },
    {
        "difficulty": "Easy",
        "question": "Which data structure is primarily used to implement Depth-First Search (DFS) or recursion?",
        "options": ["Queue", "Stack", "Circular Queue", "Priority Queue"],
        "answer": "Stack",
        "explanation": "DFS explores deep into branches using a LIFO Stack (explicit or system call stack)."
    },
    {
        "difficulty": "Easy",
        "question": "In a doubly linked list, how many pointers does each intermediate node contain?",
        "options": ["1", "2", "3", "0"],
        "answer": "2",
        "explanation": "Each node in a doubly linked list contains a previous pointer (`prev`) and a next pointer (`next`)."
    },
    {
        "difficulty": "Easy",
        "question": "What is the top pointer in a stack initialized to when implemented with an array of size N (0-indexed)?",
        "options": ["0", "-1", "N", "NULL"],
        "answer": "-1",
        "explanation": "An empty stack array representation typically sets `top = -1`."
    },
    {
        "difficulty": "Easy",
        "question": "What is the root of a tree?",
        "options": ["The topmost node with no parent", "A node with no children", "A node with only one child", "The deepest leaf node"],
        "answer": "The topmost node with no parent",
        "explanation": "The root is the entry point of a tree hierarchy with zero parent nodes."
    },
    {
        "difficulty": "Easy",
        "question": "What is a node in a tree with zero children called?",
        "options": ["Root node", "Internal node", "Leaf node", "Ancestor node"],
        "answer": "Leaf node",
        "explanation": "A leaf node (or terminal node) is a node that has no child nodes."
    },
    {
        "difficulty": "Easy",
        "question": "Which linear data structure avoids unused space at the front during dequeue operations?",
        "options": ["Linear Queue", "Circular Queue", "Simple Array", "Static Stack"],
        "answer": "Circular Queue",
        "explanation": "A circular queue connects the last position back to the first, reusing vacated spots."
    },
    {
        "difficulty": "Easy",
        "question": "What is the minimum number of nodes in a complete binary tree of height 0 (single root)?",
        "options": ["0", "1", "2", "3"],
        "answer": "1",
        "explanation": "A tree with height 0 contains just the root node, which is 1 node."
    },
    {
        "difficulty": "Easy",
        "question": "What is the condition for an empty queue in a standard array implementation with front and rear?",
        "options": ["front == rear == -1", "front > rear", "rear == capacity", "front == 0"],
        "answer": "front == rear == -1",
        "explanation": "Initializing front and rear to -1 typically indicates an empty queue."
    },
    {
        "difficulty": "Easy",
        "question": "Which data structure maps keys directly to values using a hash function?",
        "options": ["Array", "Linked List", "Hash Table (Hash Map)", "Binary Search Tree"],
        "answer": "Hash Table (Hash Map)",
        "explanation": "A hash table uses a hash function to compute an index into an array of buckets to store key-value pairs."
    },
    {
        "difficulty": "Easy",
        "question": "What is the time complexity of pushing an element onto a stack?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        "answer": "O(1)",
        "explanation": "Pushing onto a stack involves inserting at the top pointer in constant O(1) time."
    },
    {
        "difficulty": "Easy",
        "question": "What is the time complexity of inserting a node at the head of a singly linked list?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "answer": "O(1)",
        "explanation": "Inserting at the head simply requires pointing the new node to the old head and updating head pointer in O(1)."
    },
    {
        "difficulty": "Easy",
        "question": "Which traversal of a Binary Search Tree (BST) visits nodes in ascending sorted order?",
        "options": ["Pre-order", "In-order", "Post-order", "Level-order"],
        "answer": "In-order",
        "explanation": "In-order traversal (Left, Root, Right) of a BST always yields keys in ascending order."
    },
    {
        "difficulty": "Easy",
        "question": "What is a graph that contains directed edges called?",
        "options": ["Undirected Graph", "Directed Graph (Digraph)", "Bipartite Graph", "Tree"],
        "answer": "Directed Graph (Digraph)",
        "explanation": "A directed graph (digraph) has ordered pairs of vertices represented as arrows/directions."
    },

    # Medium (20)
    {
        "difficulty": "Medium",
        "question": "What is the balance factor of a node in an AVL tree defined as?",
        "options": ["Height(Left Subtree) - Height(Right Subtree)", "Number of Left Children - Number of Right Children", "Depth of Node", "Height of Tree / 2"],
        "answer": "Height(Left Subtree) - Height(Right Subtree)",
        "explanation": "In an AVL tree, the balance factor is height(left_subtree) - height(right_subtree) and must be -1, 0, or +1."
    },
    {
        "difficulty": "Medium",
        "question": "What is the worst-case time complexity of searching for an element in an unbalanced Binary Search Tree (BST)?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "answer": "O(n)",
        "explanation": "If a BST degenerates into a linear chain (skewed tree), search degrades to O(n)."
    },
    {
        "difficulty": "Medium",
        "question": "How many null pointers exist in a singly linked list of N nodes?",
        "options": ["0", "1", "N", "N - 1"],
        "answer": "1",
        "explanation": "Only the final (tail) node points to NULL in a standard singly linked list."
    },
    {
        "difficulty": "Medium",
        "question": "Which collision resolution technique uses linked lists attached to each hash bucket?",
        "options": ["Linear Probing", "Quadratic Probing", "Separate Chaining", "Double Hashing"],
        "answer": "Separate Chaining",
        "explanation": "Separate chaining stores all colliding elements in a linked list at the hashed bucket index."
    },
    {
        "difficulty": "Medium",
        "question": "In a Min-Heap, where is the smallest element always located?",
        "options": ["At the root (index 0 / 1)", "At the leftmost leaf", "At the rightmost leaf", "At any leaf node"],
        "answer": "At the root (index 0 / 1)",
        "explanation": "The min-heap property ensures that every parent is smaller than or equal to its children, placing minimum at the root."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity to insert an element into a Binary Max-Heap of size N?",
        "options": ["O(1)", "O(log N)", "O(N)", "O(N log N)"],
        "answer": "O(log N)",
        "explanation": "Inserting adds a leaf and bubbles/sifts up along the tree height, taking O(log N) time."
    },
    {
        "difficulty": "Medium",
        "question": "What is the prefix expression for the infix expression `(A + B) * C`?",
        "options": ["* + A B C", "+ * A B C", "A B + C *", "* A + B C"],
        "answer": "* + A B C",
        "explanation": "(A + B) becomes + A B; multiplying by C gives * + A B C."
    },
    {
        "difficulty": "Medium",
        "question": "What is the postfix expression for the infix expression `A + B * C`?",
        "options": ["A B C * +", "+ A * B C", "A B + C *", "A * B C +"],
        "answer": "A B C * +",
        "explanation": "Multiplication has higher precedence: B * C becomes BC*; then A + (BC*) becomes ABC*+."
    },
    {
        "difficulty": "Medium",
        "question": "Which data structure is most efficient for evaluating arithmetic expressions in Postfix notation?",
        "options": ["Queue", "Stack", "Binary Tree", "Hash Map"],
        "answer": "Stack",
        "explanation": "A stack pushes operands and pops the top two when an operator is encountered."
    },
    {
        "difficulty": "Medium",
        "question": "In a circular singly linked list, what does the next pointer of the last node point to?",
        "options": ["NULL", "Head node", "Previous node", "Itself"],
        "answer": "Head node",
        "explanation": "In a circular singly linked list, the tail node points back to the head node."
    },
    {
        "difficulty": "Medium",
        "question": "What is the total number of edges in a complete undirected graph with N vertices?",
        "options": ["N", "N(N - 1) / 2", "N(N - 1)", "2N - 1"],
        "answer": "N(N - 1) / 2",
        "explanation": "Every vertex connects to every other vertex: N choose 2 = N(N - 1) / 2 edges."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Deque (Double Ended Queue)?",
        "options": ["A queue that supports insertion and deletion at both ends", "A queue with priority", "A queue implemented using two stacks only", "A circular queue of fixed size"],
        "answer": "A queue that supports insertion and deletion at both ends",
        "explanation": "A deque (Double-Ended Queue) allows push and pop operations at both the front and rear."
    },
    {
        "difficulty": "Medium",
        "question": "What is the worst-case time complexity of lookup in a Hash Table when many collisions occur?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "answer": "O(n)",
        "explanation": "If all keys hash to the same bucket, searching degrades to traversing an O(n) linked list."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Trie data structure primarily optimized for?",
        "options": ["Integer sorting", "Fast prefix-based string searches and retrieval", "Shortest path routing", "Memory compaction"],
        "answer": "Fast prefix-based string searches and retrieval",
        "explanation": "A Trie (prefix tree) stores strings character-by-character for fast O(L) prefix searching."
    },
    {
        "difficulty": "Medium",
        "question": "What is the maximum number of nodes in a binary tree of depth/height `k` (where root is at depth 0)?",
        "options": ["2^k", "2^(k+1) - 1", "2^k - 1", "2k + 1"],
        "answer": "2^(k+1) - 1",
        "explanation": "The maximum nodes in a binary tree of height k is 1 + 2 + 4 + ... + 2^k = 2^(k+1) - 1."
    },
    {
        "difficulty": "Medium",
        "question": "Which of the following is true for a B-Tree?",
        "options": ["All leaf nodes are at the same depth", "Every internal node has at most 2 children", "It cannot store keys in internal nodes", "It is an unbalanced binary tree"],
        "answer": "All leaf nodes are at the same depth",
        "explanation": "A B-Tree is a self-balancing m-way search tree where all leaves remain at the exact same depth."
    },
    {
        "difficulty": "Medium",
        "question": "How many queues are required at minimum to implement a Stack?",
        "options": ["1", "2", "3", "4"],
        "answer": "2",
        "explanation": "A standard stack can be implemented using two FIFO queues by moving elements during push or pop."
    },
    {
        "difficulty": "Medium",
        "question": "How many stacks are required at minimum to implement a Queue?",
        "options": ["1", "2", "3", "4"],
        "answer": "2",
        "explanation": "A FIFO queue can be implemented using two LIFO stacks (inbox and outbox stacks)."
    },
    {
        "difficulty": "Medium",
        "question": "What is the space complexity of an adjacency matrix for a graph with V vertices?",
        "options": ["O(V)", "O(V + E)", "O(V^2)", "O(E^2)"],
        "answer": "O(V^2)",
        "explanation": "An adjacency matrix allocates a 2D matrix of size V x V, consuming O(V^2) memory."
    },
    {
        "difficulty": "Medium",
        "question": "In a binary search tree, what is the in-order successor of a node with a non-empty right subtree?",
        "options": ["The right child itself", "The minimum (leftmost) node in the right subtree", "The parent node", "The maximum node in the left subtree"],
        "answer": "The minimum (leftmost) node in the right subtree",
        "explanation": "The next value in sorted order is found by taking the right branch and traversing left to the minimum."
    },

    # Hard (10)
    {
        "difficulty": "Hard",
        "question": "In a Red-Black tree, what is the maximum possible height of a tree with N internal nodes?",
        "options": ["log2(N)", "2 * log2(N + 1)", "N / 2", "sqrt(N)"],
        "answer": "2 * log2(N + 1)",
        "explanation": "Red-Black properties guarantee that no simple path is more than twice as long as any other, bounding height to 2 * log2(N + 1)."
    },
    {
        "difficulty": "Hard",
        "question": "What is the amortized time complexity of union and find operations in a Disjoint Set Union (DSU) with Path Compression and Union by Rank?",
        "options": ["O(1)", "O(alpha(N)) where alpha is inverse Ackermann function", "O(log N)", "O(N)"],
        "answer": "O(alpha(N)) where alpha is inverse Ackermann function",
        "explanation": "With both optimizations, DSU operations run in near-constant O(alpha(N)) amortized time."
    },
    {
        "difficulty": "Hard",
        "question": "What is the time complexity to build a binary heap from an unsorted array of N elements using Floyd's build-heap algorithm?",
        "options": ["O(N log N)", "O(N)", "O(log N)", "O(N^2)"],
        "answer": "O(N)",
        "explanation": "Floyd's bottom-up sift-down algorithm runs in linear O(N) time due to the sum of node heights geometric series."
    },
    {
        "difficulty": "Hard",
        "question": "What is the primary operational difference between an AVL tree and a Red-Black tree?",
        "options": ["AVL trees are more strictly balanced leading to faster lookups, while Red-Black trees allow faster insertions/deletions with fewer rotations", "Red-Black trees do not store keys in internal nodes", "AVL trees cannot store duplicate values", "Red-Black trees cannot be traversed in-order"],
        "answer": "AVL trees are more strictly balanced leading to faster lookups, while Red-Black trees allow faster insertions/deletions with fewer rotations",
        "explanation": "AVL trees maintain stricter balance (height diff <= 1), making lookups faster, whereas Red-Black trees rebalance with fewer rotations."
    },
    {
        "difficulty": "Hard",
        "question": "What is a Splay Tree?",
        "options": ["A static binary tree that never changes", "A self-adjusting binary search tree where recently accessed elements are moved to the root via splay rotations", "A 3-dimensional multiway tree", "A tree that only supports inserts"],
        "answer": "A self-adjusting binary search tree where recently accessed elements are moved to the root via splay rotations",
        "explanation": "Splay trees adjust on every access (search/insert/delete) by performing zig/zig-zag rotations to bring the node to the root, achieving O(log n) amortized time."
    },
    {
        "difficulty": "Hard",
        "question": "In a Fibonacci Heap, what is the amortized time complexity for the `decrease-key` operation?",
        "options": ["O(log N)", "O(1)", "O(N)", "O(N log N)"],
        "answer": "O(1)",
        "explanation": "Fibonacci heaps support `decrease-key` and `insert` in O(1) amortized time, which improves Dijkstra's algorithm."
    },
    {
        "difficulty": "Hard",
        "question": "What is the primary advantage of a Skip List over a balanced binary search tree?",
        "options": ["It uses zero memory pointers", "It provides O(log n) search/insert with simpler probabilistic balancing and lock-free concurrent implementation", "It guarantees O(1) worst case search", "It stores keys in continuous array memory"],
        "answer": "It provides O(log n) search/insert with simpler probabilistic balancing and lock-free concurrent implementation",
        "explanation": "Skip lists use multi-level linked lists with probabilistic height promotion, avoiding complex tree rotation logic and easing concurrent lock-free access."
    },
    {
        "difficulty": "Hard",
        "question": "What is a Segment Tree typically used for?",
        "options": ["Storing strings with common prefixes", "Answering range queries (e.g., range sum/min/max) and point/range updates in O(log N) time", "Representing dense bipartite graphs", "Sorting numbers in external hard drives"],
        "answer": "Answering range queries (e.g., range sum/min/max) and point/range updates in O(log N) time",
        "explanation": "Segment trees represent intervals/segments, allowing efficient range queries and point/range modifications in O(log N)."
    },
    {
        "difficulty": "Hard",
        "question": "What data structure does the Fenwick Tree (Binary Indexed Tree) efficiently compute?",
        "options": ["Topological ordering in DAGs", "Prefix sums and frequency updates in an array in O(log N) time and O(N) space", "Biconnected components", "Strongly connected components"],
        "answer": "Prefix sums and frequency updates in an array in O(log N) time and O(N) space",
        "explanation": "Fenwick trees store cumulative frequency/prefix sums using bit manipulation of indices in compact O(N) array memory."
    },
    {
        "difficulty": "Hard",
        "question": "What is the worst-case number of rotations required to rebalance an AVL tree after an insertion?",
        "options": ["At most 1 single or double rotation (O(1))", "O(log N) rotations", "O(N) rotations", "No rotations are ever required"],
        "answer": "At most 1 single or double rotation (O(1))",
        "explanation": "After inserting into an AVL tree, at most one single or double rotation (2 single rotations) is required to restore balance."
    }
]
