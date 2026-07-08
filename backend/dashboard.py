import streamlit as st


def get_dashboard_stats():

    return {

        "pdfs": len(
            st.session_state.get(
                "uploaded_pdfs",
                []
            )
        ),

        "questions": len(
            st.session_state.get(
                "messages",
                []
            )
        ),

        "flashcards": len(
            st.session_state.get(
                "flashcards",
                []
            )
        ),

        "latest_pdf": st.session_state.get(
            "uploaded_pdf",
            "None"
        )

    }