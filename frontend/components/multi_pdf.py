import streamlit as st

from backend.multi_pdf import get_uploaded_pdfs


def show_multi_pdf():

    st.title("📚 Multi PDF Manager")

    st.markdown("---")

    st.write(
        "Manage all uploaded study materials."
    )

    pdfs = get_uploaded_pdfs()

    if len(pdfs) == 0:

        st.info("No PDFs uploaded yet.")

        return

    st.success(f"{len(pdfs)} PDF(s) available")

    st.markdown("---")

    for i, pdf in enumerate(pdfs):

        st.write(f"📄 {i+1}. {pdf}")