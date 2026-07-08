import streamlit as st

from backend.related_topics import generate_related_topics


def show_related_topics():

    st.title("📚 AI Related Topics")

    st.markdown("---")

    topic = st.text_input(
        "Enter a Topic",
        placeholder="Example: Machine Learning"
    )

    if st.button("🚀 Generate Related Topics", use_container_width=True):

        if topic.strip() == "":

            st.warning("Please enter a topic.")

            return

        with st.spinner("Finding related topics..."):

            topics = generate_related_topics(topic)

        st.markdown("## 📖 Suggested Topics")

        if len(topics) == 0:

            st.error("No related topics found.")

        else:

            for index, item in enumerate(topics, start=1):

                st.write(f"{index}. {item}")