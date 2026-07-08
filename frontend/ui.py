import streamlit as st

from frontend.components.sidebar import show_sidebar
from frontend.components.chat import show_chat
from frontend.components.summary import show_summary
from frontend.components.quiz import show_quiz
from frontend.components.flashcards import show_flashcards
from frontend.components.translator import show_translator
from frontend.components.diagram import show_diagram
from frontend.components.related_topics import show_related_topics


def show_ui():

    # ----------------------------------------
    # Sidebar
    # ----------------------------------------

    show_sidebar()

    # ----------------------------------------
    # Default Page
    # ----------------------------------------

    if "page" not in st.session_state:

        st.session_state.page = "chat"

    # ----------------------------------------
    # Routing
    # ----------------------------------------

    if st.session_state.page == "chat":

        show_chat()

    elif st.session_state.page == "summary":

        show_summary()

    elif st.session_state.page == "quiz":

        show_quiz()

    elif st.session_state.page == "flashcards":

        show_flashcards()

    elif st.session_state.page == "translator":

        show_translator()

    elif st.session_state.page == "diagram":

        show_diagram()

    elif st.session_state.page == "related_topics":

        show_related_topics()