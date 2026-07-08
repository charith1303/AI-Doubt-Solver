import streamlit as st


def show_welcome():

    if len(st.session_state.get("messages", [])) == 0:

        st.markdown("## 👋 Welcome to Astra")

        st.write(
            "I'm your AI study companion."
        )

        st.write(
            "Ask me anything and I'll explain it in the simplest possible way."
        )

        st.info(
            "💡 Try asking:\n\n"
            "- Explain Artificial Intelligence\n"
            "- Teach me Newton's Laws\n"
            "- Explain Python loops\n"
            "- What is Photosynthesis?"
        )

        st.divider()