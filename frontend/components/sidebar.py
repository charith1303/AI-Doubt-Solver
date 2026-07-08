import os
import streamlit as st

from backend.history import clear_chat
from backend.pdf_loader import extract_text_from_pdf
from backend.text_chunker import split_text
from backend.vectorstore import add_chunks


def show_sidebar():

    with st.sidebar:

        # ------------------------------------
        # Session State
        # ------------------------------------

        if "pdf_text" not in st.session_state:
            st.session_state.pdf_text = ""

        if "uploaded_pdf" not in st.session_state:
            st.session_state.uploaded_pdf = None

        if "uploaded_pdfs" not in st.session_state:
            st.session_state.uploaded_pdfs = []

        if "pdf_chunks" not in st.session_state:
            st.session_state.pdf_chunks = []

        if "page" not in st.session_state:
            st.session_state.page = "chat"

        # ------------------------------------
        # Sidebar Header
        # ------------------------------------

        st.title("🌟 Astra")

        st.markdown("---")

        # ------------------------------------
        # Navigation
        # ------------------------------------

        if st.button("💬 Chat", use_container_width=True):
            st.session_state.page = "chat"
            st.rerun()

        if st.button("🆕 New Chat", use_container_width=True):
            clear_chat()
            st.session_state.page = "chat"
            st.rerun()

        # ------------------------------------
        # Upload Notes
        # ------------------------------------

        uploaded_files = st.file_uploader(
            "📄 Upload Notes",
            type=["pdf"],
            accept_multiple_files=True
        )

        if uploaded_files:

            os.makedirs("uploads/pdfs", exist_ok=True)

            for uploaded_file in uploaded_files:

                if uploaded_file.name not in st.session_state.uploaded_pdfs:

                    save_path = os.path.join(
                        "uploads",
                        "pdfs",
                        uploaded_file.name
                    )

                    with open(save_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    pdf_text = extract_text_from_pdf(save_path)

                    chunks = split_text(pdf_text)

                    if len(chunks) > 0:
                        add_chunks(chunks)

                    st.session_state.uploaded_pdfs.append(uploaded_file.name)

                    st.session_state.uploaded_pdf = uploaded_file.name
                    st.session_state.pdf_text = pdf_text
                    st.session_state.pdf_chunks = chunks

            st.success("🧠 Astra has learned all uploaded PDFs!")

        # ------------------------------------
        # PDF Statistics
        # ------------------------------------

        if len(st.session_state.uploaded_pdfs) > 0:

            st.info(f"""
### 📄 PDF Statistics

**Total PDFs:** {len(st.session_state.uploaded_pdfs)}

**Latest PDF:** {st.session_state.uploaded_pdf}

**Words:** {len(st.session_state.pdf_text.split())}

**Characters:** {len(st.session_state.pdf_text)}

**Chunks:** {len(st.session_state.pdf_chunks)}
""")

            with st.expander("📖 Preview Latest PDF"):

                st.text(st.session_state.pdf_text[:1000])

        # ------------------------------------
        # AI Features
        # ------------------------------------

        if st.button("📝 Practice Quiz", use_container_width=True):
            st.session_state.page = "quiz"
            st.rerun()

        if st.button("📄 AI Summary", use_container_width=True):
            st.session_state.page = "summary"
            st.rerun()

        if st.button("📊 AI Diagram", use_container_width=True):
            st.session_state.page = "diagram"
            st.rerun()

        if st.button("📚 Related Topics", use_container_width=True):
            st.session_state.page = "related_topics"
            st.rerun()

        if st.button("🧠 Flashcards", use_container_width=True):
            st.session_state.page = "flashcards"
            st.rerun()

        if st.button("🌍 AI Translator", use_container_width=True):
            st.session_state.page = "translator"
            st.rerun()

        if st.button("📚 Multi PDF", use_container_width=True):
            st.session_state.page = "multi_pdf"
            st.rerun()

        if st.button("📊 Dashboard", use_container_width=True):
            st.session_state.page = "dashboard"
            st.rerun()

        # ------------------------------------
        # Future Features
        # ------------------------------------

        st.button("🕘 Chat History", use_container_width=True)

        st.button("⚙️ Settings", use_container_width=True)

        st.markdown("---")

        st.info(
            "Astra is your personal AI learning assistant."
        )