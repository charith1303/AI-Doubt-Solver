import streamlit as st


def get_uploaded_pdfs():
    """
    Returns the list of uploaded PDFs.
    """

    if "uploaded_pdfs" not in st.session_state:
        st.session_state.uploaded_pdfs = []

    return st.session_state.uploaded_pdfs