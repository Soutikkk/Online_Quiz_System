import streamlit as st
import json
import random
import os

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="CSE Quiz System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    /* Main container and font styling */
    .main {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Header hero styling */
    .hero-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
    }
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 300;
    }

    /* Question card */
    .question-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .question-badge {
        display: inline-block;
        padding: 0.25rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    .badge-category {
        background-color: #e0e7ff;
        color: #3730a3;
    }
    .badge-easy {
        background-color: #dcfce7;
        color: #166534;
    }
    .badge-medium {
        background-color: #fef9c3;
        color: #854d0e;
    }
    .badge-hard {
        background-color: #fee2e2;
        color: #991b1b;
    }

    /* Review Card Styling */
    .review-card {
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.2rem;
        border-left: 6px solid #cbd5e1;
        background-color: #f8fafc;
    }
    .review-card.correct {
        border-left-color: #22c55e;
        background-color: #f0fdf4;
    }
    .review-card.wrong {
        border-left-color: #ef4444;
        background-color: #fef2f2;
    }
    
    /* Result Tier Box */
    .tier-box {
        text-align: center;
        padding: 2rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        font-weight: bold;
    }
    .tier-excellent {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
    }
    .tier-very-good {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
    }
    .tier-good {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
    }
    .tier-needs-improvement {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_questions():
    """Load and cache questions from questions.json file."""
    file_path = os.path.join(os.path.dirname(__file__), "questions.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def init_session_state():
    """Initialize state variables if not already present."""
    if "page" not in st.session_state:
        st.session_state.page = "HOME"
    if "quiz_questions" not in st.session_state:
        st.session_state.quiz_questions = []
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}  # {question_index: selected_option_str}
    if "quiz_config" not in st.session_state:
        st.session_state.quiz_config = {}


def start_quiz(questions_pool, num_q, category, difficulty):
    """Filters pool and starts a new quiz session."""
    filtered = questions_pool
    if category != "All Categories":
        filtered = [q for q in filtered if q["category"] == category]
    if difficulty != "All Difficulties":
        filtered = [q for q in filtered if q["difficulty"] == difficulty]
    
    if not filtered:
        st.error("No questions found matching your filter criteria. Please adjust your selections.")
        return

    sample_size = min(num_q, len(filtered))
    selected = random.sample(filtered, sample_size)

    st.session_state.quiz_questions = selected
    st.session_state.current_index = 0
    st.session_state.user_answers = {}
    st.session_state.quiz_config = {
        "category": category,
        "difficulty": difficulty,
        "total_requested": num_q,
        "total_actual": sample_size
    }
    st.session_state.page = "QUIZ"
    st.rerun()


# ==========================================
# PAGE 1: HOME PAGE
# ==========================================
def render_home(all_questions):
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🎓 CSE Quiz System</div>
        <div class="hero-subtitle">Test your Computer Science Engineering knowledge with 500+ Curated Questions</div>
    </div>
    """, unsafe_allow_html=True)

    # Categories and stats
    categories = sorted(list(set(q["category"] for q in all_questions)))
    difficulties = ["All Difficulties", "Easy", "Medium", "Hard"]

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.subheader("⚙️ Configure Your Quiz")
        
        selected_category = st.selectbox(
            "Select Category",
            ["All Categories"] + categories,
            index=0,
            help="Choose a specific CSE domain or practice across all topics."
        )

        selected_difficulty = st.selectbox(
            "Select Difficulty",
            difficulties,
            index=0,
            help="Filter questions by difficulty tier."
        )

        num_questions = st.select_slider(
            "Number of Questions",
            options=[10, 20, 30, 50, 100],
            value=20,
            help="Select how many questions you want in your quiz."
        )

        st.markdown("<br>", unsafe_allow_html=True)
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("🚀 Start Custom Quiz", use_container_width=True, type="primary"):
                start_quiz(all_questions, num_questions, selected_category, selected_difficulty)
        
        with btn_col2:
            if st.button("🎲 Quick Random Quiz (20 Qs)", use_container_width=True):
                start_quiz(all_questions, 20, "All Categories", "All Difficulties")

    with col2:
        st.subheader("📊 Question Bank Overview")
        st.info(f"Total Available Questions: **{len(all_questions)}** across **{len(categories)}** Core CSE Topics.")

        # Show topics breakdown in an expander
        with st.expander("📚 View Topic Breakdown (500 Questions)", expanded=True):
            cat_counts = {}
            for q in all_questions:
                cat_counts[q["category"]] = cat_counts.get(q["category"], 0) + 1
            
            for cat, count in cat_counts.items():
                st.write(f"• **{cat}**: `{count} questions`")


# ==========================================
# PAGE 2: QUIZ PAGE
# ==========================================
def render_quiz():
    questions = st.session_state.quiz_questions
    idx = st.session_state.current_index
    total = len(questions)

    if total == 0:
        st.session_state.page = "HOME"
        st.rerun()
        return

    q = questions[idx]

    # Top Header & Progress
    progress_val = (idx + 1) / total
    st.progress(progress_val)

    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown(f"### Question {idx + 1} of {total}")
    with header_col2:
        diff_class = f"badge-{q['difficulty'].lower()}"
        st.markdown(f"""
        <div style="text-align: right; padding-top: 5px;">
            <span class="question-badge badge-category">{q['category']}</span>
            <span class="question-badge {diff_class}">{q['difficulty']}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Main Quiz Area and Sidebar Palette
    main_col, nav_col = st.columns([3, 1], gap="medium")

    with main_col:
        # Question Display
        st.markdown(f"#### {q['question']}")

        # Retrieve previously saved answer for this question
        current_saved_answer = st.session_state.user_answers.get(idx, None)
        
        # Calculate default index in options list
        options = q["options"]
        default_index = options.index(current_saved_answer) if current_saved_answer in options else None

        selected_option = st.radio(
            "Choose your answer:",
            options=options,
            index=default_index,
            key=f"radio_q_{idx}_{q['id']}",
            label_visibility="collapsed"
        )

        # Save selection into session state
        if selected_option is not None:
            st.session_state.user_answers[idx] = selected_option

        st.markdown("<br>", unsafe_allow_html=True)

        # Navigation Controls
        nav_prev, nav_next, nav_submit = st.columns([1, 1, 1])

        with nav_prev:
            if st.button("⬅️ Previous", disabled=(idx == 0), use_container_width=True):
                st.session_state.current_index -= 1
                st.rerun()

        with nav_next:
            if idx < total - 1:
                if st.button("Next ➡️", use_container_width=True, type="primary"):
                    st.session_state.current_index += 1
                    st.rerun()
            else:
                st.write("")

        with nav_submit:
            if st.button("✅ Submit Quiz", type="primary" if idx == total - 1 else "secondary", use_container_width=True):
                st.session_state.page = "RESULT"
                st.rerun()

    # Sidebar / Palette Quick Navigation
    with nav_col:
        st.markdown("##### 🧭 Question Palette")
        answered_count = len(st.session_state.user_answers)
        st.caption(f"Answered: **{answered_count}/{total}**")
        
        # Grid of questions
        grid_cols = st.columns(4)
        for i in range(total):
            col_target = grid_cols[i % 4]
            is_answered = i in st.session_state.user_answers
            is_current = (i == idx)

            btn_label = f"{i + 1}{' ●' if is_answered else ''}"
            btn_type = "primary" if is_current else ("secondary" if not is_answered else "secondary")
            
            with col_target:
                if st.button(btn_label, key=f"jump_btn_{i}", use_container_width=True):
                    st.session_state.current_index = i
                    st.rerun()


# ==========================================
# PAGE 3: RESULT & REVIEW PAGE
# ==========================================
def render_result():
    questions = st.session_state.quiz_questions
    user_answers = st.session_state.user_answers
    total = len(questions)

    if total == 0:
        st.session_state.page = "HOME"
        st.rerun()
        return

    # Calculate Score
    correct_count = 0
    wrong_count = 0
    unanswered_count = 0

    for i, q in enumerate(questions):
        user_ans = user_answers.get(i, None)
        if user_ans is None:
            unanswered_count += 1
        elif user_ans == q["answer"]:
            correct_count += 1
        else:
            wrong_count += 1

    percentage = (correct_count / total) * 100 if total > 0 else 0

    # Classification
    if percentage >= 90:
        tier_title = "🏆 Excellent!"
        tier_msg = "Outstanding performance! You have an exceptional grasp of Computer Science concepts."
        tier_class = "tier-excellent"
    elif percentage >= 75:
        tier_title = "🌟 Very Good!"
        tier_msg = "Great job! You have a solid understanding across most CSE domains."
        tier_class = "tier-very-good"
    elif percentage >= 50:
        tier_title = "👍 Good"
        tier_msg = "Fair effort! Review the explanations below to strengthen key areas."
        tier_class = "tier-good"
    else:
        tier_title = "📚 Needs Improvement"
        tier_msg = "Keep practicing! Review each answer and explanation to build your knowledge."
        tier_class = "tier-needs-improvement"

    # Display Tier Box
    st.markdown(f"""
    <div class="tier-box {tier_class}">
        <div style="font-size: 2.2rem; margin-bottom: 0.3rem;">{tier_title}</div>
        <div style="font-size: 1.1rem; opacity: 0.95;">{tier_msg}</div>
    </div>
    """, unsafe_allow_html=True)

    # Score Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Questions", total)
    with col2:
        st.metric("Score", f"{correct_count} / {total}")
    with col3:
        st.metric("Percentage", f"{percentage:.1f}%")
    with col4:
        st.metric("Correct", f"✅ {correct_count}")
    with col5:
        st.metric("Wrong / Skipped", f"❌ {wrong_count + unanswered_count}")

    st.markdown("---")

    # Action Buttons (Retake / Return Home)
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("🔄 Retake Quiz", use_container_width=True, type="primary"):
            cfg = st.session_state.quiz_config
            all_q = load_questions()
            start_quiz(all_q, cfg.get("total_requested", 20), cfg.get("category", "All Categories"), cfg.get("difficulty", "All Difficulties"))
    with btn_col2:
        if st.button("🏠 Return to Home", use_container_width=True):
            st.session_state.page = "HOME"
            st.session_state.quiz_questions = []
            st.session_state.user_answers = {}
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📝 Detailed Answer Review")
    st.caption("Review all questions, your answers, correct solutions, and in-depth explanations below.")

    # Filter review options
    review_filter = st.radio(
        "Filter Review:",
        ["All Questions", "Incorrect / Skipped Only", "Correct Only"],
        horizontal=True
    )

    for i, q in enumerate(questions):
        user_ans = user_answers.get(i, None)
        is_correct = (user_ans == q["answer"])
        is_skipped = (user_ans is None)

        if review_filter == "Incorrect / Skipped Only" and is_correct:
            continue
        if review_filter == "Correct Only" and not is_correct:
            continue

        card_class = "correct" if is_correct else "wrong"
        status_badge = "✅ Correct" if is_correct else ("⚠️ Skipped" if is_skipped else "❌ Incorrect")

        with st.container():
            st.markdown(f"""
            <div class="review-card {card_class}">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <strong>Question {i + 1} of {total}</strong>
                    <span><strong>{status_badge}</strong> &nbsp;|&nbsp; <em>{q['category']} ({q['difficulty']})</em></span>
                </div>
                <div style="font-size: 1.05rem; font-weight: 600; margin-bottom: 0.8rem;">
                    {q['question']}
                </div>
                <div style="margin-bottom: 0.4rem;">
                    <strong>Your Answer:</strong> <span style="color: {'#166534' if is_correct else '#991b1b'};">{user_ans if not is_skipped else '<em>Not Attempted</em>'}</span>
                </div>
                <div style="margin-bottom: 0.6rem;">
                    <strong>Correct Answer:</strong> <span style="color: #166534; font-weight: 600;">{q['answer']}</span>
                </div>
                <div style="background: rgba(0,0,0,0.03); padding: 0.7rem 1rem; border-radius: 8px; font-size: 0.95rem;">
                    💡 <strong>Explanation:</strong> {q['explanation']}
                </div>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# MAIN APPLICATION CONTROLLER
# ==========================================
def main():
    init_session_state()
    all_questions = load_questions()

    if st.session_state.page == "HOME":
        render_home(all_questions)
    elif st.session_state.page == "QUIZ":
        render_quiz()
    elif st.session_state.page == "RESULT":
        render_result()


if __name__ == "__main__":
    main()
