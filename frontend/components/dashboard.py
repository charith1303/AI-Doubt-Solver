import streamlit as st

from backend.dashboard import get_dashboard_stats


def show_dashboard():

    stats = get_dashboard_stats()

    st.title("📊 Astra Dashboard")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📄 PDFs Uploaded",
            stats["pdfs"]
        )

    with col2:

        st.metric(
            "💬 Questions",
            stats["questions"]
        )

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:

        st.metric(
            "🧠 Flashcards",
            stats["flashcards"]
        )

    with col4:

        st.metric(
            "📚 Latest PDF",
            stats["latest_pdf"]
        )

    st.markdown("---")

    st.success(
        "🎉 Astra is ready to help you study!"
    )