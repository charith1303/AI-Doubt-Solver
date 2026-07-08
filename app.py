import os
import streamlit as st

from frontend.ui import show_ui

print("=" * 60)
print("RUNNING APP.PY")
print("Location:", os.path.abspath(__file__))
print("=" * 60)

st.set_page_config(
    page_title="AI Doubt Solver",
    page_icon="🎓",
    layout="wide"
)


def load_css():

    css_path = "frontend/styles/theme.css"

    print("Current Folder:", os.getcwd())
    print("CSS Exists:", os.path.exists(css_path))

    with open(css_path, "r", encoding="utf-8") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

show_ui()