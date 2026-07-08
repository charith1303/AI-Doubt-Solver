import streamlit as st

from backend.quiz_parser import get_sample_quiz


def show_quiz():

    st.title("📝 Practice Quiz")

    st.markdown("---")

    st.write("Practice using AI-generated quizzes.")

    quiz = get_sample_quiz()

    answers = {}

    for i, q in enumerate(quiz):

        st.subheader(f"Question {i+1}")

        st.write(q["question"])

        answers[i] = st.radio(
            "Choose an answer",
            q["options"],
            key=f"quiz_{i}"
        )

        st.markdown("---")

    if st.button("✅ Submit Quiz", use_container_width=True):

        score = 0

        st.header("📊 Results")

        for i, q in enumerate(quiz):

            if answers[i] == q["answer"]:
                score += 1
                st.success(f"✅ Question {i+1}: Correct")
            else:
                st.error(f"❌ Question {i+1}: Incorrect")
                st.info(f"Correct Answer: **{q['answer']}**")

        st.metric(
            "Final Score",
            f"{score}/{len(quiz)}"
        )