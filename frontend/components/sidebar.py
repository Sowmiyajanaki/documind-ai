import streamlit as st
from utils.api import health, upload, get_documents


def render_sidebar():
    """
    Render the application sidebar.
    Returns the selected document.
    """

    with st.sidebar:

        # ==========================================
        # Documents
        # ==========================================

        st.title("📂 Documents")

        with st.container(border=True):

            st.markdown("**📤 Upload PDF**")
            st.caption("Upload a PDF document")

            uploaded_pdf = st.file_uploader(
                "Choose PDF",
                type=["pdf"],
                key="pdf_upload",
                label_visibility="collapsed"
            )

            if uploaded_pdf:

                st.success(f"📄 {uploaded_pdf.name}")

                if st.button(
                    "🚀 Process",
                    use_container_width=True
                ):

                    with st.spinner("Processing..."):

                        try:

                            result = upload(uploaded_pdf)

                            st.success("✅ Done")

                            st.session_state["selected_document"] = result["document"]

                            st.rerun()

                        except Exception as e:

                            st.error(str(e))

            else:

                st.caption("📄 PDF • Max 200 MB")

        st.markdown("---")

        # ==========================================
        # Current Document
        # ==========================================

        st.markdown("**📄 Current Document**")

        try:
            documents = get_documents()
        except Exception:
            documents = []

        if not documents:

            st.warning("No processed documents found.")
            document = None

        else:

            current_document = st.session_state.get(
                "selected_document",
                documents[0]
            )

            if current_document not in documents:
                current_document = documents[0]

            document = st.selectbox(
                "Choose Document",
                documents,
                index=documents.index(current_document)
            )

            st.session_state["selected_document"] = document

        st.markdown("---")

        # ==========================================
        # System
        # ==========================================

        st.markdown("**⚙️ System**")

        col1, col2 = st.columns([1, 6])

        with col1:
            st.write("🤖")
        with col2:
            st.caption("Model: Llama 3.3 70B")

        col1, col2 = st.columns([1, 6])

        with col1:
            st.write("🧠")
        with col2:
            st.caption("Embedding: MiniLM-L6-v2")

        col1, col2 = st.columns([1, 6])

        with col1:
            st.write("🟢" if health() else "🔴")
        with col2:
            st.caption(
                "Backend: Connected" if health()
                else "Backend: Offline"
            )

        st.markdown("---")

        st.caption("DocuMind AI v2.0")

    return document