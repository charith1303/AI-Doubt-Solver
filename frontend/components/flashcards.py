import streamlit as st

from backend.flashcards import generate_flashcards


def show_flashcards():

    st.title("🧠 AI Flashcards")

    st.markdown("---")

    if "flashcards" not in st.session_state:
        st.session_state.flashcards = []

    if "card_index" not in st.session_state:
        st.session_state.card_index = 0

    if "show_answer" not in st.session_state:
        st.session_state.show_answer = False

    if st.button("🚀 Generate Flashcards", use_container_width=True):

        with st.spinner("Generating Flashcards..."):

            st.session_state.flashcards = generate_flashcards()

            st.session_state.card_index = 0

            st.session_state.show_answer = False

    if len(st.session_state.flashcards) > 0:

        card = st.session_state.flashcards[
            st.session_state.card_index
        ]

        st.subheader(
            f"Card {st.session_state.card_index+1} / {len(st.session_state.flashcards)}"
        )

        if st.session_state.show_answer:

            st.success(card["back"])

        else:

            st.info(card["front"])

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button("⬅ Previous"):

                if st.session_state.card_index > 0:

                    st.session_state.card_index -= 1

                    st.session_state.show_answer = False

                    st.rerun()

        with col2:

            if st.button("🔄 Flip"):

                st.session_state.show_answer = (
                    not st.session_state.show_answer
                )

                st.rerun()

        with col3:

            if st.button("Next ➡"):

                if st.session_state.card_index < len(st.session_state.flashcards)-1:

                    st.session_state.card_index += 1

                    st.session_state.show_answer = False

                    st.rerun()