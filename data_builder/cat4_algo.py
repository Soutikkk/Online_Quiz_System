CATEGORY = "Algorithms"

QUESTIONS = [
    # Easy (20)
    {
        "difficulty": "Easy",
        "question": "What is the time complexity of Linear Search in an array of size N?",
        "options": ["O(1)", "O(log N)", "O(N)", "O(N^2)"],
        "answer": "O(N)",
        "explanation": "Linear search checks each element sequentially from start to finish, requiring O(N) operations in the worst case."
    },
    {
        "difficulty": "Easy",
        "question": "What is the prerequisite for executing Binary Search on an array?",
        "options": ["The array must contain only positive integers", "The array must be sorted", "The array must have an even number of elements", "The array must not contain duplicates"],
        "answer": "The array must be sorted",
        "explanation": "Binary search divides search space in half based on comparison with middle element, requiring sorted data."
    },
    {
        "difficulty": "Easy",
        "question": "What is the time complexity of Binary Search in a sorted array of size N?",
        "options": ["O(1)", "O(log N)", "O(N)", "O(N log N)"],
        "answer": "O(log N)",
        "explanation": "Binary search halves the remaining search interval at each step, running in O(log N) time."
    },
    {
        "difficulty": "Easy",
        "question": "What is the average and worst-case time complexity of Bubble Sort?",
        "options": ["O(N)", "O(N log N)", "O(N^2)", "O(2^N)"],
        "answer": "O(N^2)",
        "explanation": "Bubble sort compares adjacent pairs across nested loops, resulting in O(N^2) time complexity."
    },
    {
        "difficulty": "Easy",
        "question": "Which algorithmic paradigm does Merge Sort follow?",
        "options": ["Greedy method", "Divide and Conquer", "Dynamic Programming", "Backtracking"],
        "answer": "Divide and Conquer",
        "explanation": "Merge sort divides the list into sub-lists, sorts them recursively, and merges them back together."
    },
    {
        "difficulty": "Easy",
        "question": "What is the worst-case time complexity of Merge Sort?",
        "options": ["O(N)", "O(N log N)", "O(N^2)", "O(log N)"],
        "answer": "O(N log N)",
        "explanation": "Merge sort consistently splits arrays in half (log N levels) and merges in O(N) at each level, ensuring O(N log N)."
    },
    {
        "difficulty": "Easy",
        "question": "Which notation represents the tight asymptotic upper bound of an algorithm's growth rate?",
        "options": ["Big-O (O)", "Big-Omega (Ω)", "Big-Theta (Θ)", "Little-o"],
        "answer": "Big-O (O)",
        "explanation": "Big-O notation describes the upper bound or worst-case asymptotic behavior of an algorithm."
    },
    {
        "difficulty": "Easy",
        "question": "Which notation describes the tight asymptotic lower bound of an algorithm?",
        "options": ["Big-O (O)", "Big-Omega (Ω)", "Big-Theta (Θ)", "Little-omega"],
        "answer": "Big-Omega (Ω)",
        "explanation": "Big-Omega (Ω) notation defines the theoretical lower bound on execution time."
    },
    {
        "difficulty": "Easy",
        "question": "What is an in-place sorting algorithm?",
        "options": ["An algorithm that does not require additional memory beyond O(1) auxiliary space", "An algorithm that sorts only positive numbers", "An algorithm that uses multiple threads", "An algorithm that does not modify original data"],
        "answer": "An algorithm that does not require additional memory beyond O(1) auxiliary space",
        "explanation": "In-place algorithms transform input data structures using small, constant O(1) extra storage."
    },
    {
        "difficulty": "Easy",
        "question": "What does a 'stable' sorting algorithm guarantee?",
        "options": ["The algorithm never runs out of memory", "Elements with equal keys maintain their relative original order", "The algorithm always runs in O(N log N)", "The array is sorted in descending order"],
        "answer": "Elements with equal keys maintain their relative original order",
        "explanation": "Stability ensures duplicate elements retain their initial sequence after sorting."
    },
    {
        "difficulty": "Easy",
        "question": "Which sorting algorithm repeatedly picks the minimum element from the unsorted section and swaps it to front?",
        "options": ["Insertion Sort", "Selection Sort", "Quick Sort", "Radix Sort"],
        "answer": "Selection Sort",
        "explanation": "Selection sort finds the smallest element in the remaining array and places it at the current index."
    },
    {
        "difficulty": "Easy",
        "question": "What is the best-case time complexity of standard Insertion Sort when array is already sorted?",
        "options": ["O(1)", "O(N)", "O(N log N)", "O(N^2)"],
        "answer": "O(N)",
        "explanation": "When already sorted, insertion sort makes 1 comparison per element without shifting, taking O(N) time."
    },
    {
        "difficulty": "Easy",
        "question": "Which algorithm is used to find the shortest path from a single source vertex in a graph with non-negative edge weights?",
        "options": ["Dijkstra's Algorithm", "Kruskal's Algorithm", "Prim's Algorithm", "Floyd-Warshall Algorithm"],
        "answer": "Dijkstra's Algorithm",
        "explanation": "Dijkstra's algorithm computes the shortest path from a single source to all vertices on graphs with non-negative weights."
    },
    {
        "difficulty": "Easy",
        "question": "Which algorithmic design approach makes locally optimal choices at each step hoping to find the global optimum?",
        "options": ["Greedy Algorithm", "Dynamic Programming", "Brute Force", "Branch and Bound"],
        "answer": "Greedy Algorithm",
        "explanation": "Greedy algorithms make the immediate locally best decision without backtracking."
    },
    {
        "difficulty": "Easy",
        "question": "Which algorithm finds the Minimum Spanning Tree (MST) by sorting all edges and adding them if they don't form a cycle?",
        "options": ["Kruskal's Algorithm", "Dijkstra's Algorithm", "Bellman-Ford Algorithm", "BFS"],
        "answer": "Kruskal's Algorithm",
        "explanation": "Kruskal's algorithm sorts all graph edges by weight and uses Disjoint Set Union (DSU) to avoid cycles."
    },
    {
        "difficulty": "Easy",
        "question": "What is the space complexity of standard Merge Sort on an array of size N?",
        "options": ["O(1)", "O(log N)", "O(N)", "O(N^2)"],
        "answer": "O(N)",
        "explanation": "Merge sort requires O(N) temporary buffer space to merge divided subarrays."
    },
    {
        "difficulty": "Easy",
        "question": "What is the average time complexity of Quick Sort?",
        "options": ["O(N)", "O(N log N)", "O(N^2)", "O(log N)"],
        "answer": "O(N log N)",
        "explanation": "On average with balanced partitions, Quick Sort runs in O(N log N) time."
    },
    {
        "difficulty": "Easy",
        "question": "What is the worst-case time complexity of Quick Sort (e.g. when already sorted and pivot chosen poorly)?",
        "options": ["O(N)", "O(N log N)", "O(N^2)", "O(2^N)"],
        "answer": "O(N^2)",
        "explanation": "If the pivot choice creates highly unbalanced partitions of 0 and N-1 elements, recursion depth is N, yielding O(N^2)."
    },
    {
        "difficulty": "Easy",
        "question": "Which algorithm is used to detect connected components in an undirected graph?",
        "options": ["BFS or DFS", "Binary Search", "Kadane's Algorithm", "Karatsuba Multiplication"],
        "answer": "BFS or DFS",
        "explanation": "Traversing unvisited nodes using Breadth-First Search (BFS) or Depth-First Search (DFS) identifies all connected components."
    },
    {
        "difficulty": "Easy",
        "question": "What is the base case in a recursive algorithm?",
        "options": ["The condition that terminates recursive calls and returns a direct result", "The step where memory is allocated", "The initial loop declaration", "The deepest stack error"],
        "answer": "The condition that terminates recursive calls and returns a direct result",
        "explanation": "The base case prevents infinite recursion by returning an answer without making further recursive calls."
    },

    # Medium (20)
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of Kadane's Algorithm for finding the maximum subarray sum in an array of size N?",
        "options": ["O(1)", "O(N)", "O(N log N)", "O(N^2)"],
        "answer": "O(N)",
        "explanation": "Kadane's algorithm solves maximum subarray problem in a single linear scan in O(N) time."
    },
    {
        "difficulty": "Medium",
        "question": "What are the two essential properties required to apply Dynamic Programming?",
        "options": ["Optimal Substructure and Overlapping Subproblems", "Greedy Choice and Constant Time Steps", "Sorting and Binary Division", "Stack Overflow and Memoization"],
        "answer": "Optimal Substructure and Overlapping Subproblems",
        "explanation": "DP is applicable when the problem exhibits optimal substructure (optimal solution composed of optimal subsolutions) and overlapping subproblems."
    },
    {
        "difficulty": "Medium",
        "question": "What is the primary difference between Memoization (Top-Down) and Tabulation (Bottom-Up) in DP?",
        "options": ["Memoization uses recursion with caching; Tabulation builds an iterative table from base cases up", "Tabulation uses recursion only", "Memoization uses no extra memory", "Tabulation cannot solve 0/1 Knapsack"],
        "answer": "Memoization uses recursion with caching; Tabulation builds an iterative table from base cases up",
        "explanation": "Top-down memoization stores recursive subproblem solutions; bottom-up tabulation fills a table iteratively."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of the Floyd-Warshall algorithm for All-Pairs Shortest Path on a graph with V vertices?",
        "options": ["O(V)", "O(V log V)", "O(V^2)", "O(V^3)"],
        "answer": "O(V^3)",
        "explanation": "Floyd-Warshall uses three nested loops over all vertices k, i, and j, taking O(V^3) time."
    },
    {
        "difficulty": "Medium",
        "question": "Which algorithm can detect negative weight cycles in a directed graph?",
        "options": ["Dijkstra's Algorithm", "Bellman-Ford Algorithm", "Prim's Algorithm", "Kruskal's Algorithm"],
        "answer": "Bellman-Ford Algorithm",
        "explanation": "Bellman-Ford relaxes edges V-1 times; if a V-th relaxation reduces a distance, a negative cycle exists."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of Heap Sort for an array of N elements?",
        "options": ["O(N)", "O(N log N)", "O(N^2)", "O(log N)"],
        "answer": "O(N log N)",
        "explanation": "Building the heap takes O(N), and extracting N elements takes N * O(log N), giving O(N log N) in all cases."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of Counting Sort for N elements with range K?",
        "options": ["O(N + K)", "O(N * K)", "O(N log K)", "O(K^2)"],
        "answer": "O(N + K)",
        "explanation": "Counting sort counts frequencies in O(N) and reconstructs elements in O(K), resulting in O(N + K) time."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of standard matrix multiplication of two N x N matrices using Strassen's algorithm?",
        "options": ["O(N^3)", "O(N^2.807)", "O(N^2)", "O(N log N)"],
        "answer": "O(N^2.807)",
        "explanation": "Strassen's algorithm reduces 8 recursive multiplications to 7, achieving O(N^log2(7)) ≈ O(N^2.807)."
    },
    {
        "difficulty": "Medium",
        "question": "Which technique does Huffman Coding use for data compression?",
        "options": ["Dynamic Programming", "Greedy method with a Priority Queue (Min-Heap)", "Divide and Conquer", "Backtracking"],
        "answer": "Greedy method with a Priority Queue (Min-Heap)",
        "explanation": "Huffman coding iteratively merges the two lowest-frequency character nodes using a min-heap to generate optimal prefix codes."
    },
    {
        "difficulty": "Medium",
        "question": "What does Master Theorem provide a closed-form solution for?",
        "options": ["Solving recurrence relations of divide-and-conquer algorithms like T(n) = a*T(n/b) + f(n)", "Calculating graph chromatic numbers", "Determining network flow bottlenecks", "Solving NP-complete problems"],
        "answer": "Solving recurrence relations of divide-and-conquer algorithms like T(n) = a*T(n/b) + f(n)",
        "explanation": "Master Theorem provides asymptotic bounds for recurrences that divide inputs into equal subproblems."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of the 0/1 Knapsack dynamic programming solution with N items and capacity W?",
        "options": ["O(N)", "O(W)", "O(N * W)", "O(2^N)"],
        "answer": "O(N * W)",
        "explanation": "The 2D DP table has dimensions (N+1) x (W+1), filled in pseudo-polynomial time O(N * W)."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of the Fractional Knapsack problem?",
        "options": ["O(N log N) using Greedy method based on value-to-weight ratio", "O(N * W) using DP", "O(2^N) using Backtracking", "O(N^2) using Brute Force"],
        "answer": "O(N log N) using Greedy method based on value-to-weight ratio",
        "explanation": "Fractional knapsack sorts items by value/weight in O(N log N) and takes whole or fractional items greedily."
    },
    {
        "difficulty": "Medium",
        "question": "What is Topological Sorting applied to?",
        "options": ["Any cyclic graph", "Directed Acyclic Graphs (DAGs)", "Undirected complete graphs", "Binary Search Trees only"],
        "answer": "Directed Acyclic Graphs (DAGs)",
        "explanation": "Topological sort produces a linear ordering of vertices such that for every directed edge u -> v, u comes before v in a DAG."
    },
    {
        "difficulty": "Medium",
        "question": "Which algorithm is used for pattern searching in a text in linear time O(N + M)?",
        "options": ["Knuth-Morris-Pratt (KMP) Algorithm", "Selection Sort", "Kruskal's Algorithm", "Bellman-Ford Algorithm"],
        "answer": "Knuth-Morris-Pratt (KMP) Algorithm",
        "explanation": "KMP uses a preprocessing Longest Prefix Suffix (LPS) array to skip redundant comparisons in O(N + M) time."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of finding the Longest Common Subsequence (LCS) of two strings of lengths M and N using DP?",
        "options": ["O(M + N)", "O(M * N)", "O(2^(M+N))", "O(log(M * N))"],
        "answer": "O(M * N)",
        "explanation": "Building the dynamic programming matrix of size (M+1) x (N+1) takes O(M * N) time."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of Quickselect for finding the k-th smallest element on average?",
        "options": ["O(1)", "O(N)", "O(N log N)", "O(N^2)"],
        "answer": "O(N)",
        "explanation": "Quickselect only recurses into one half of the partition, yielding T(N) = N + N/2 + N/4... = O(N) average time."
    },
    {
        "difficulty": "Medium",
        "question": "In the N-Queens problem, which algorithmic approach is standard for placing non-attacking queens?",
        "options": ["Greedy Algorithm", "Backtracking", "Divide and Conquer", "Linear Programming"],
        "answer": "Backtracking",
        "explanation": "Backtracking places queens row-by-row and abandons invalid board states when conflicts occur."
    },
    {
        "difficulty": "Medium",
        "question": "What is the time complexity of checking if a graph is Bipartite using 2-Coloring via BFS?",
        "options": ["O(V + E)", "O(V * E)", "O(V^2)", "O(E log V)"],
        "answer": "O(V + E)",
        "explanation": "Traversing the graph with BFS and assigning alternating colors runs in standard linear graph time O(V + E)."
    },
    {
        "difficulty": "Medium",
        "question": "What is the worst-case number of comparisons in worst-case optimal comparison-based sorting of N items?",
        "options": ["O(N)", "Omega(N log N)", "O(N^2)", "O(log N)"],
        "answer": "Omega(N log N)",
        "explanation": "Information-theoretic lower bound states that decision trees require at least log2(N!) = Ω(N log N) comparisons."
    },
    {
        "difficulty": "Medium",
        "question": "Which algorithm is used to find Strongly Connected Components (SCC) in a directed graph using two DFS passes?",
        "options": ["Kosaraju's Algorithm", "Prim's Algorithm", "Dijkstra's Algorithm", "Ford-Fulkerson Algorithm"],
        "answer": "Kosaraju's Algorithm",
        "explanation": "Kosaraju's algorithm performs one DFS on original graph to get finishing times, then a second DFS on the transposed graph."
    },

    # Hard (10)
    {
        "difficulty": "Hard",
        "question": "What is the class NP in computational complexity theory defined as?",
        "options": ["Problems that cannot be solved by any computer", "Decision problems whose solutions can be verified in polynomial time by a deterministic Turing machine", "Problems solvable in non-linear polynomial time only", "Problems that require infinite memory"],
        "answer": "Decision problems whose solutions can be verified in polynomial time by a deterministic Turing machine",
        "explanation": "NP (Nondeterministic Polynomial time) contains decision problems where a candidate certificate/witness is checkable in polynomial time."
    },
    {
        "difficulty": "Hard",
        "question": "What constitutes an NP-Complete problem?",
        "options": ["A problem that is in NP and to which every problem in NP can be reduced in polynomial time (NP-Hard)", "A problem that has an O(N) solution", "A problem that is strictly outside of NP", "An unsolvable undecidable problem"],
        "answer": "A problem that is in NP and to which every problem in NP can be reduced in polynomial time (NP-Hard)",
        "explanation": "A problem X is NP-Complete if X ∈ NP and for all Y ∈ NP, Y ≤p X (it is at least as hard as any problem in NP)."
    },
    {
        "difficulty": "Hard",
        "question": "What is the time complexity of the Ford-Fulkerson method with Edmonds-Karp implementation for Maximum Flow?",
        "options": ["O(V * E^2)", "O(V^2 * E)", "O(E log V)", "O(V^3)"],
        "answer": "O(V * E^2)",
        "explanation": "Edmonds-Karp uses BFS to find augmenting paths, bounding the number of augmentations to O(V * E), yielding O(V * E^2)."
    },
    {
        "difficulty": "Hard",
        "question": "What is the time complexity of the A* Search algorithm with an admissible and consistent heuristic in terms of explored state space?",
        "options": ["Always O(1)", "Guaranteed to find the optimal path while expanding fewer or equal nodes than any other optimal search with same heuristic", "O(N^3)", "O(V!)"],
        "answer": "Guaranteed to find the optimal path while expanding fewer or equal nodes than any other optimal search with same heuristic",
        "explanation": "With an admissible and consistent heuristic, A* is optimally efficient and guarantees finding shortest path without reopening nodes."
    },
    {
        "difficulty": "Hard",
        "question": "What is the time complexity of the Fast Fourier Transform (FFT) for multiplying two degree-N polynomials?",
        "options": ["O(N^2)", "O(N log N)", "O(N)", "O(log N)"],
        "answer": "O(N log N)",
        "explanation": "FFT converts polynomials from coefficient to point-value form in O(N log N), multiplies in O(N), and inverts in O(N log N)."
    },
    {
        "difficulty": "Hard",
        "question": "What is the time complexity of Tarjan's Bridge-Finding Algorithm in an undirected graph?",
        "options": ["O(V + E)", "O(V^2)", "O(V * E)", "O(E log V)"],
        "answer": "O(V + E)",
        "explanation": "Tarjan's algorithm uses DFS discovery and low-link values in a single pass to identify all bridge edges in linear O(V + E) time."
    },
    {
        "difficulty": "Hard",
        "question": "What is the Cook-Levin Theorem?",
        "options": ["Proves that the Boolean Satisfiability Problem (SAT) is NP-Complete", "Proves that P = NP", "Proves that Sorting requires Ω(N log N)", "Proves that Halting Problem is decidable"],
        "answer": "Proves that the Boolean Satisfiability Problem (SAT) is NP-Complete",
        "explanation": "The Cook-Levin theorem proved that SAT is NP-Complete, establishing the foundation of computational complexity theory."
    },
    {
        "difficulty": "Hard",
        "question": "What is the time complexity of dynamic programming for Matrix Chain Multiplication of N matrices?",
        "options": ["O(N)", "O(N^2)", "O(N^3)", "O(2^N)"],
        "answer": "O(N^3)",
        "explanation": "Matrix Chain Multiplication considers subchain lengths from 2 to N and splits k from i to j, resulting in O(N^3) time."
    },
    {
        "difficulty": "Hard",
        "question": "What does the Robin Karp string matching algorithm use for fast sub-string filtering?",
        "options": ["Rolling Hash function", "Suffix Automaton", "Binary Search", "Levenshtein Distance"],
        "answer": "Rolling Hash function",
        "explanation": "Rabin-Karp calculates rolling hash values of text windows in O(1) time per window to quickly filter non-matches."
    },
    {
        "difficulty": "Hard",
        "question": "What is the amortized cost of incrementing an N-bit binary counter starting from 0?",
        "options": ["O(N)", "O(1) per increment", "O(log N)", "O(N^2)"],
        "answer": "O(1) per increment",
        "explanation": "Using aggregate analysis, bit 0 flips N times, bit 1 flips N/2, bit 2 flips N/4... total flips < 2N, so amortized cost is O(1)."
    }
]
