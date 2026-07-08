import streamlit as st

from backend.translator import translate_text


def show_translator():

    st.title("🌍 AI Translator")

    st.markdown("---")

    st.write(
        "Translate your notes or AI responses into another language."
    )

    languages = [
        "Hindi",
        "Telugu",
        "Tamil",
        "Kannada",
        "Malayalam",
        "English",
        "French",
        "German",
        "Spanish"
    ]

    language = st.selectbox(
        "Choose Language",
        languages
    )

    default_text = st.session_state.get("pdf_text", "")

    text = st.text_area(
        "Text to Translate",
        value=default_text,
        height=250
    )

    if st.button(
        "🌍 Translate",
        use_container_width=True
    ):

        with st.spinner("Translating..."):

            translated = translate_text(
                text,
                language
            )

        st.markdown("---")

        st.subheader("Translated Text")

        st.write(translated)