import streamlit as st

from backend.summary_generator import generate_summary


def show_summary():

    st.title("📄 AI Study Summary")

    st.markdown("---")

    st.write(
        "Generate a concise summary from your uploaded notes."
    )

    summary_type = st.selectbox(
        "Summary Type",
        [
            "Short",
            "Detailed",
            "Exam Revision"
        ]
    )

    if st.button(
        "🚀 Generate Summary",
        use_container_width=True
    ):

        with st.spinner("Generating Summary..."):

            summary = generate_summary(summary_type)

        st.markdown("---")

        st.subheader("📚 Summary")

        st.markdown(summary)