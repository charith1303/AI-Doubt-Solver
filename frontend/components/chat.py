import streamlit as st

from backend.chatbot import get_ai_response
from backend.history import (
    initialize_chat,
    add_user_message,
    add_ai_message
)


def show_chat():

    # ------------------------------------
    # Initialize Chat History
    # ------------------------------------

    initialize_chat()

    # ------------------------------------
    # Explanation Level Selector
    # ------------------------------------

    level = st.selectbox(
        "🎓 Explanation Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ],
        index=1
    )

    st.markdown("---")

    # ------------------------------------
    # Display Previous Messages
    # ------------------------------------

    for message in st.session_state["messages"]:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if (
                message["role"] == "assistant"
                and "sources" in message
                and len(message["sources"]) > 0
            ):

                with st.expander("📖 Sources"):

                    for index, source in enumerate(
                        message["sources"],
                        start=1
                    ):

                        st.markdown(f"**Source {index}**")

                        st.info(
                            source[:300] + "..."
                            if len(source) > 300
                            else source
                        )

    # ------------------------------------
    # Chat Input
    # ------------------------------------

    question = st.chat_input("Ask Astra anything...")

    if question:

        # Display User Message

        with st.chat_message("user"):

            st.markdown(question)

        add_user_message(question)

        # ------------------------------------
        # Generate AI Response
        # ------------------------------------

        with st.spinner("🌟 Astra is thinking..."):

            result = get_ai_response(
                question,
                level
            )

        answer = result["answer"]

        sources = result["sources"]

        # ------------------------------------
        # Display AI Response
        # ------------------------------------

        with st.chat_message("assistant"):

            st.markdown(answer)

            if len(sources) > 0:

                with st.expander("📖 Sources"):

                    for index, source in enumerate(
                        sources,
                        start=1
                    ):

                        st.markdown(f"**Source {index}**")

                        st.info(
                            source[:300] + "..."
                            if len(source) > 300
                            else source
                        )

        add_ai_message(
            answer,
            sources=sources
        )