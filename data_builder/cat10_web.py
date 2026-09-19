CATEGORY = "Web Technologies"

QUESTIONS = [
    # Easy (12)
    {
        "difficulty": "Easy",
        "question": "What does HTML stand for?",
        "options": ["HyperText Markup Language", "High-level Text Management Language", "Hyperlink Text Marking Logic", "Home Tool Markup Language"],
        "answer": "HyperText Markup Language",
        "explanation": "HTML stands for HyperText Markup Language, the standard markup language for creating web pages."
    },
    {
        "difficulty": "Easy",
        "question": "What does CSS stand for?",
        "options": ["Cascading Style Sheets", "Computer Style System", "Creative Styling Standard", "Coded Sheet Syntax"],
        "answer": "Cascading Style Sheets",
        "explanation": "CSS stands for Cascading Style Sheets, used for styling the layout and presentation of HTML documents."
    },
    {
        "difficulty": "Easy",
        "question": "Which HTML tag is used to create an interactive hyperlink?",
        "options": ["<a>", "<link>", "<href>", "<url>"],
        "answer": "<a>",
        "explanation": "The `<a>` (anchor) tag with the `href` attribute creates hyperlinks to other web pages or locations."
    },
    {
        "difficulty": "Easy",
        "question": "Which HTML element is used to embed client-side JavaScript code?",
        "options": ["<script>", "<javascript>", "<js>", "<code>"],
        "answer": "<script>",
        "explanation": "The `<script>` tag is used to embed or reference executable client-side JavaScript code."
    },
    {
        "difficulty": "Easy",
        "question": "What does DOM stand for in client-side web development?",
        "options": ["Document Object Model", "Data Object Manager", "Digital Optimization Module", "Direct Output Mechanism"],
        "answer": "Document Object Model",
        "explanation": "The Document Object Model (DOM) is a programming interface representing HTML/XML documents as a node tree."
    },
    {
        "difficulty": "Easy",
        "question": "Which HTTP request method is primarily intended to submit data to a server to create/process a resource?",
        "options": ["GET", "POST", "HEAD", "OPTIONS"],
        "answer": "POST",
        "explanation": "POST sends enclosed entity data to the server to create or process resources (e.g. form submissions)."
    },
    {
        "difficulty": "Easy",
        "question": "What HTTP status code indicates a successful request?",
        "options": ["200 OK", "301 Moved Permanently", "404 Not Found", "500 Internal Server Error"],
        "answer": "200 OK",
        "explanation": "HTTP 200 OK standard response indicates that the HTTP request has succeeded."
    },
    {
        "difficulty": "Easy",
        "question": "What HTTP status code represents 'Page Not Found'?",
        "options": ["400", "401", "403", "404"],
        "answer": "404",
        "explanation": "HTTP 404 Not Found indicates that the server cannot find the requested resource URL."
    },
    {
        "difficulty": "Easy",
        "question": "What does JSON stand for?",
        "options": ["JavaScript Object Notation", "Java System Online Network", "JavaScript Output Node", "Joint Standard Object Name"],
        "answer": "JavaScript Object Notation",
        "explanation": "JSON (JavaScript Object Notation) is a lightweight, language-independent data-interchange text format."
    },
    {
        "difficulty": "Easy",
        "question": "What CSS property is used to change the text color of an HTML element?",
        "options": ["color", "text-color", "font-color", "foreground"],
        "answer": "color",
        "explanation": "The `color` property in CSS sets the foreground color of text elements."
    },
    {
        "difficulty": "Easy",
        "question": "Which HTTP status code represents a generic internal server error?",
        "options": ["200", "302", "404", "500"],
        "answer": "500",
        "explanation": "HTTP 500 Internal Server Error indicates an unexpected condition on the server that prevented fulfilling the request."
    },
    {
        "difficulty": "Easy",
        "question": "Which CSS property is used to create space around elements outside of any defined borders?",
        "options": ["margin", "padding", "border-spacing", "outline"],
        "answer": "margin",
        "explanation": "In the CSS box model, `margin` clears an area outside the border, while `padding` creates space inside the border."
    },

    # Medium (12)
    {
        "difficulty": "Medium",
        "question": "What is the CSS Box Model composed of from inside to outside?",
        "options": ["Content -> Padding -> Border -> Margin", "Content -> Margin -> Border -> Padding", "Padding -> Content -> Border -> Margin", "Margin -> Border -> Padding -> Content"],
        "answer": "Content -> Padding -> Border -> Margin",
        "explanation": "The standard CSS box model wraps around every HTML element: Content, surrounded by Padding, then Border, then outer Margin."
    },
    {
        "difficulty": "Medium",
        "question": "What is Cross-Origin Resource Sharing (CORS)?",
        "options": ["An HTTP-header based security mechanism that allows a server to indicate any origins other than its own from which a browser should permit loading resources", "A technique for sharing CSS files across websites", "A database replication protocol", "A method to bypass SSL certificates"],
        "answer": "An HTTP-header based security mechanism that allows a server to indicate any origins other than its own from which a browser should permit loading resources",
        "explanation": "CORS uses HTTP response headers (like Access-Control-Allow-Origin) to tell browsers whether cross-domain AJAX requests are authorized."
    },
    {
        "difficulty": "Medium",
        "question": "What does the `localStorage` object in HTML5 Web Storage API provide?",
        "options": ["Client-side key-value storage with no expiration date that persists across browser sessions", "Session-only storage that clears when the tab is closed", "Server-side SQL storage", "Encrypted cookie storage with HTTP-only flag"],
        "answer": "Client-side key-value storage with no expiration date that persists across browser sessions",
        "explanation": "`localStorage` stores persistent key-value pairs (up to ~5MB) in the browser that survive browser restarts."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between `cookies`, `sessionStorage`, and `localStorage`?",
        "options": ["Cookies are sent automatically with every HTTP request (~4KB); sessionStorage expires when the tab closes; localStorage persists indefinitely without auto-sending to server", "Cookies can store up to 50MB of data", "sessionStorage persists across computer reboots", "localStorage is sent in HTTP request headers automatically"],
        "answer": "Cookies are sent automatically with every HTTP request (~4KB); sessionStorage expires when the tab closes; localStorage persists indefinitely without auto-sending to server",
        "explanation": "Cookies travel in HTTP request headers for server sessions, whereas web storage (`sessionStorage`/`localStorage`) remains purely client-side."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between Synchronous and Asynchronous JavaScript execution (Event Loop)?",
        "options": ["Synchronous blocks the single main thread; Asynchronous delegates tasks (timers, fetch) to browser Web APIs and executes callbacks via Event Loop queues without blocking", "Asynchronous creates native CPU hardware threads for every function", "Synchronous JavaScript runs faster in all cases", "JavaScript is inherently multi-threaded with parallel locks"],
        "answer": "Synchronous blocks the single main thread; Asynchronous delegates tasks (timers, fetch) to browser Web APIs and executes callbacks via Event Loop queues without blocking",
        "explanation": "JavaScript runs on a single-threaded event loop, offloading I/O and timers to browser Web APIs and queuing callbacks on microtask/macrotask queues."
    },
    {
        "difficulty": "Medium",
        "question": "What is REST (Representational State Transfer) architecture?",
        "options": ["A stateless, resource-oriented architectural style for web APIs using standard HTTP verbs (GET, POST, PUT, DELETE) and standard media types", "A binary RPC protocol over UDP", "A protocol requiring XML-RPC schemas exclusively", "A stateful session protocol"],
        "answer": "A stateless, resource-oriented architectural style for web APIs using standard HTTP verbs (GET, POST, PUT, DELETE) and standard media types",
        "explanation": "REST leverages HTTP methods on URI-identified resources, stateless client-server communication, and uniform representations (JSON/XML)."
    },
    {
        "difficulty": "Medium",
        "question": "What does the `box-sizing: border-box;` CSS declaration do?",
        "options": ["Includes padding and border within the element's total declared width and height", "Removes borders from boxes", "Adds external margins to width", "Forces boxes to display as flex containers"],
        "answer": "Includes padding and border within the element's total declared width and height",
        "explanation": "`border-box` simplifies responsive design by calculating width and height inclusive of content, padding, and border."
    },
    {
        "difficulty": "Medium",
        "question": "What is WebSocket protocol (RFC 6455)?",
        "options": ["A full-duplex, persistent two-way communication channel over a single TCP connection initiated via an HTTP Upgrade handshake", "A protocol for sending emails from web pages", "A server-side file compression standard", "A replacement for DNS"],
        "answer": "A full-duplex, persistent two-way communication channel over a single TCP connection initiated via an HTTP Upgrade handshake",
        "explanation": "WebSockets provide low-latency, bi-directional real-time communication between browser and server without repeated HTTP polling."
    },
    {
        "difficulty": "Medium",
        "question": "What is the purpose of JWT (JSON Web Token)?",
        "options": ["A compact, URL-safe means of securely representing signed claims between two parties for stateless authentication and authorization", "A tool for minifying JavaScript files", "A database index format", "A CSS preprocessor"],
        "answer": "A compact, URL-safe means of securely representing signed claims between two parties for stateless authentication and authorization",
        "explanation": "JWT consists of Header.Payload.Signature and provides tamper-proof stateless verification of user identity."
    },
    {
        "difficulty": "Medium",
        "question": "What is the difference between `PUT` and `PATCH` HTTP methods?",
        "options": ["`PUT` replaces the entire target resource representation; `PATCH` applies partial modifications to a resource", "`PUT` is read-only; `PATCH` is write-only", "`PATCH` is idempotent; `PUT` is not", "There is no difference"],
        "answer": "`PUT` replaces the entire target resource representation; `PATCH` applies partial modifications to a resource",
        "explanation": "PUT replaces the resource completely (idempotent); PATCH updates only specified fields of the target resource."
    },
    {
        "difficulty": "Medium",
        "question": "What is Event Bubbling in JavaScript DOM event propagation?",
        "options": ["The phase where an event triggers on the deepest target element and bubbles upwards through its ancestor nodes in the DOM hierarchy", "When multiple events crash the browser", "When events are captured from window downwards", "When memory leaks create orphan DOM nodes"],
        "answer": "The phase where an event triggers on the deepest target element and bubbles upwards through its ancestor nodes in the DOM hierarchy",
        "explanation": "Event propagation consists of Capturing (downwards), Target, and Bubbling (upwards from target to `window`)."
    },
    {
        "difficulty": "Medium",
        "question": "What is a Progressive Web App (PWA)?",
        "options": ["A web application that uses modern web APIs (Service Workers, Manifest) to deliver app-like experiences including offline capability and push notifications", "A website written exclusively in WebAssembly", "A desktop app wrapped in Electron", "A website that only runs on Google Chrome"],
        "answer": "A web application that uses modern web APIs (Service Workers, Manifest) to deliver app-like experiences including offline capability and push notifications",
        "explanation": "PWAs use Service Workers to cache assets for offline use and Web App Manifests for installability on mobile/desktop devices."
    },

    # Hard (6)
    {
        "difficulty": "Hard",
        "question": "What is the difference between the JavaScript Microtask Queue (Promises) and Macrotask / Task Queue (setTimeout)?",
        "options": ["Microtasks (Promise reactions, queueMicrotask, MutationObserver) have higher priority and are completely drained after every task before the next macrotask runs or rendering occurs", "Macrotasks execute before microtasks", "Both queues execute in parallel on separate threads", "Microtasks are managed by the operating system kernel"],
        "answer": "Microtasks (Promise reactions, queueMicrotask, MutationObserver) have higher priority and are completely drained after every task before the next macrotask runs or rendering occurs",
        "explanation": "The event loop processes one macrotask, then drains all microtasks until empty, before performing UI layout and paint."
    },
    {
        "difficulty": "Hard",
        "question": "What is Server-Side Rendering (SSR) vs Static Site Generation (SSG) in modern web frameworks?",
        "options": ["SSR renders HTML on each individual request dynamically at runtime; SSG pre-renders full HTML pages at build time ahead of requests", "SSG requires continuous database queries on every click", "SSR cannot use JavaScript on the client", "SSG is only used for video streaming"],
        "answer": "SSR renders HTML on each individual request dynamically at runtime; SSG pre-renders full HTML pages at build time ahead of requests",
        "explanation": "SSR generates dynamic HTML per user request on the server; SSG generates static HTML files during build time for fast CDN distribution."
    },
    {
        "difficulty": "Hard",
        "question": "What is Critical Rendering Path (CRP) optimization in web performance?",
        "options": ["Minimizing the sequence of steps (DOM -> CSSOM -> Render Tree -> Layout -> Paint) required for the browser to render the initial viewport pixels", "Optimizing server SQL join queries", "Compiling JavaScript to machine assembly", "Minifying database schemas"],
        "answer": "Minimizing the sequence of steps (DOM -> CSSOM -> Render Tree -> Layout -> Paint) required for the browser to render the initial viewport pixels",
        "explanation": "Optimizing CRP reduces render-blocking CSS and JS to deliver fast First Contentful Paint (FCP) and Largest Contentful Paint (LCP)."
    },
    {
        "difficulty": "Hard",
        "question": "What is WebAssembly (Wasm)?",
        "options": ["A binary instruction format for a stack-based virtual machine enabling near-native execution speed for code compiled from C/C++/Rust inside web browsers", "A new JavaScript syntax standard", "An assembly language for motherboard BIOS", "A CSS styling framework"],
        "answer": "A binary instruction format for a stack-based virtual machine enabling near-native execution speed for code compiled from C/C++/Rust inside web browsers",
        "explanation": "Wasm allows performant compiled languages (C++, Rust, Go) to run alongside JavaScript inside the browser's secure sandbox."
    },
    {
        "difficulty": "Hard",
        "question": "What is Content Security Policy (CSP)?",
        "options": ["An HTTP header standard that restricts the origins and resources (scripts, images, styles, iframes) a browser is allowed to load to mitigate Cross-Site Scripting (XSS)", "A copyright management standard", "A license file for open source websites", "A firewall that blocks port 80"],
        "answer": "An HTTP header standard that restricts the origins and resources (scripts, images, styles, iframes) a browser is allowed to load to mitigate Cross-Site Scripting (XSS)",
        "explanation": "CSP prevents code injection attacks (XSS, data injection) by specifying whitelisted domains for executable scripts and other assets."
    },
    {
        "difficulty": "Hard",
        "question": "What is Hydration in modern reactive frontend frameworks (React/Vue)?",
        "options": ["The client-side process where framework JavaScript attaches event listeners and reactive state to pre-rendered server-generated HTML DOM nodes", "Allocating RAM memory buffers for images", "Clearing browser cache memory", "Compressing SVG vectors"],
        "answer": "The client-side process where framework JavaScript attaches event listeners and reactive state to pre-rendered server-generated HTML DOM nodes",
        "explanation": "Hydration transforms static server-rendered HTML into an interactive client-side Single Page Application (SPA) by binding JavaScript event listeners."
    }
]
