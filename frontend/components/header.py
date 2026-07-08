import streamlit as st


def show_header():

    col1, col2 = st.columns([1, 8])

    with col1:
        st.markdown("# 🌟")

    with col2:
        st.title("Astra")
        st.caption("Your Personal AI Learning Assistant")

    st.divider()