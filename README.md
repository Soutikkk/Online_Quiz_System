# 🎓 Online CSE Quiz System

A web-based **Computer Science Engineering Quiz System** built with **Python and Streamlit**. The application provides a large curated question bank covering major CSE domains and allows users to create customized quizzes based on category, difficulty, and number of questions.

---

## 📌 Features

* 🎯 **500 Curated CSE Questions**
* 📚 **12 Computer Science Categories**
* ⚙️ Custom quiz configuration
* 🎚️ Difficulty filtering — Easy, Medium, Hard
* 🔢 Choose between 10, 20, 30, 50, or 100 questions
* 🎲 Quick Random Quiz mode
* 🧭 Interactive question navigation
* 📊 Question progress indicator
* 💾 Automatically saves selected answers during the quiz
* ✅ Automatic score calculation
* 📈 Percentage-based performance evaluation
* 📝 Answer review with explanations
* 🎨 Responsive and modern Streamlit interface
* 🔍 Validated question dataset with duplicate and data-integrity checks

---

## 📚 Question Categories

The question bank contains **500 questions** distributed across the following topics:

| Category                                          | Questions |
| ------------------------------------------------- | --------: |
| Programming Fundamentals                          |        50 |
| Python Programming                                |        50 |
| Data Structures                                   |        50 |
| Algorithms                                        |        50 |
| DBMS                                              |        50 |
| Operating Systems                                 |        50 |
| Computer Networks                                 |        50 |
| Computer Organization & Architecture              |        40 |
| Software Engineering                              |        30 |
| Web Technologies                                  |        30 |
| Artificial Intelligence & Machine Learning Basics |        25 |
| Cyber Security                                    |        25 |
| **Total**                                         |   **500** |

---

## 🛠️ Technology Stack

### Frontend / UI

* **Streamlit**
* HTML
* CSS

### Backend / Logic

* **Python**
* JSON

### Data Processing

* Python data structures
* JSON-based question storage
* Random question selection

---

## 📂 Project Structure

```text
Online_Quiz_System/
│
├── app.py
├── build_questions.py
├── questions.json
├── requirements.txt
├── .gitignore
│
└── data_builder/
    ├── cat1_prog_fund.py
    ├── cat2_python.py
    ├── cat3_ds.py
    ├── cat4_algo.py
    ├── cat5_dbms.py
    ├── cat6_os.py
    ├── cat7_cn.py
    ├── cat8_coa.py
    ├── cat9_se.py
    ├── cat10_web.py
    ├── cat11_ai_ml.py
    └── cat12_cyber.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project directory:

```bash
cd Online_Quiz_System
```

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The project currently requires:

```text
streamlit>=1.30.0
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

After starting the application, Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 🧠 How the Application Works

The application follows a simple quiz workflow:

```text
                ┌─────────────────┐
                │   Start App     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Load Questions  │
                │   questions.json│
                └────────┬────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Configure Quiz       │
              │ • Category           │
              │ • Difficulty         │
              │ • Number of Questions│
              └──────────┬───────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Random Selection│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Take Quiz       │
                │                 │
                │ Previous / Next │
                │ Question Palette│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Submit Quiz     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Calculate Score │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Results & Review│
                │ + Explanations  │
                └─────────────────┘
```

---

# ⚙️ Quiz Configuration

Users can customize their quiz using three parameters.

### Category

Users can select:

* All Categories
* Programming Fundamentals
* Python Programming
* Data Structures
* Algorithms
* DBMS
* Operating Systems
* Computer Networks
* Computer Organization & Architecture
* Software Engineering
* Web Technologies
* AI & ML
* Cyber Security

### Difficulty

The available difficulty levels are:

* Easy
* Medium
* Hard
* All Difficulties

### Number of Questions

Users can select:

```text
10
20
30
50
100
```

---

# 📝 Quiz Interface

During the quiz, users can:

* View the current question number
* See quiz progress
* View the question category
* View question difficulty
* Select an answer
* Move to the previous question
* Move to the next question
* Jump directly to any question
* Submit the quiz

The question palette also indicates which questions have already been answered.

---

# 📊 Scoring System

After submitting the quiz, the application calculates:

* ✅ Correct answers
* ❌ Incorrect answers
* ⚪ Unanswered questions
* 📈 Overall percentage

The percentage is calculated using:

```text
Percentage = (Correct Answers / Total Questions) × 100
```

The application then classifies the result into performance tiers.

|      Score | Performance          |
| ---------: | -------------------- |
| 90% – 100% | 🏆 Excellent         |
|  75% – 89% | 🌟 Very Good         |
|  50% – 74% | 👍 Good              |
|  Below 50% | 📚 Needs Improvement |

---

# 🗂️ Question Dataset

The questions are maintained in individual Python files inside the `data_builder` directory.

For example:

```text
data_builder/
├── cat1_prog_fund.py
├── cat2_python.py
├── cat3_ds.py
...
└── cat12_cyber.py
```

The `build_questions.py` script combines these question sets into:

```text
questions.json
```

---

# 🔎 Dataset Validation

The project includes a dedicated validation system in `build_questions.py`.

Before generating `questions.json`, the script checks:

* Correct number of questions per category
* Total question count
* Duplicate questions
* Valid difficulty levels
* Exactly four options per question
* Unique answer options
* Correct answer exists in the options
* Explanation is provided for every question

The project expects exactly:

```text
500 questions
```

---

# 🔄 Rebuild the Question Dataset

If questions are added or modified inside the `data_builder` directory, regenerate the master dataset using:

```bash
python build_questions.py
```

The script validates all questions and generates:

```text
questions.json
```

If validation fails, the script displays the corresponding error instead of generating an invalid dataset.

---

# 📁 Data Format

Each question follows a structure similar to:

```json
{
  "id": 1,
  "category": "Python Programming",
  "difficulty": "Easy",
  "question": "Which keyword is used to define a function in Python?",
  "options": [
    "function",
    "def",
    "define",
    "fun"
  ],
  "answer": "def",
  "explanation": "The def keyword is used to define a function in Python."
}
```

---

# 🎨 User Interface

The application uses custom CSS styling to provide:

* Gradient hero section
* Question cards
* Difficulty badges
* Category badges
* Progress indicators
* Result cards
* Correct/incorrect review styling
* Responsive multi-column layout

---

# 🔐 Data & Privacy

The application currently operates using a local JSON question bank.

No user account or external database is required.

Quiz answers are maintained using **Streamlit session state** during the active quiz session.

---

# 📦 Deployment

The application can be deployed to platforms that support Streamlit applications.

For example, the project can be deployed using **Streamlit Community Cloud** by connecting the GitHub repository and selecting:

```text
app.py
```

as the application entry point.

---

# 💡 Future Improvements

Possible future enhancements include:

* 👤 User authentication
* 🏆 Leaderboard system
* 📊 Persistent quiz history
* 📈 Personal performance analytics
* ⏱️ Timed quizzes
* 🌙 Dark mode
* 🔖 Bookmark questions
* ❤️ Favorite questions
* 🔍 Search questions
* 🧠 Adaptive difficulty
* 🤖 AI-generated questions
* 💬 AI explanations
* 🗄️ Database integration
* 📱 Improved mobile interface
* 📥 Export quiz results as PDF
* 🌐 Multi-user online quiz rooms

---

# 🎯 Use Cases

This project can be used for:

* CSE exam preparation
* Technical interview preparation
* Programming practice
* College laboratory projects
* Self-assessment
* Online classroom quizzes
* Competitive programming fundamentals
* Technical aptitude preparation

---

# 👨‍💻 Project

**Project Name:** Online Quiz System

**Built With:** Python + Streamlit

**Question Bank:** 500 CSE Questions

**Application Type:** Web-Based Quiz Application

---

## ⭐ Contributing

Contributions are welcome.

To contribute:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Online_Quiz_System
pip install -r requirements.txt
```

Create a new branch:

```bash
git checkout -b feature/your-feature
```

Make your changes, test the application, and submit a pull request.

---

## 📄 License

This project is intended for educational and academic purposes.

If you plan to distribute or commercially use the project, add an appropriate open-source license such as MIT License and update this section accordingly.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
