import streamlit as st
import streamlit.components.v1 as components

from backend.diagram import generate_diagram


def show_diagram():

    st.title("📊 AI Diagram Generator")

    st.markdown("---")

    question = st.text_input(
        "Enter a concept",
        placeholder="Example: Explain Machine Learning"
    )

    if st.button("🚀 Generate Diagram", use_container_width=True):

        if question.strip() == "":

            st.warning("Please enter a topic.")

            return

        with st.spinner("Generating Mermaid Diagram..."):

            mermaid_code = generate_diagram(question)

        st.subheader("Generated Mermaid Code")

        st.code(mermaid_code, language="text")

        html = f"""
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>

        <script>
            mermaid.initialize({{ startOnLoad: true }});
        </script>

        <div class="mermaid">
        {mermaid_code}
        </div>
        """

        st.subheader("Diagram Preview")

        components.html(
            html,
            height=500,
            scrolling=True
        )