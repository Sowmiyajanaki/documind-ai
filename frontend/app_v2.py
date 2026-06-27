import streamlit as st
import requests

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "http://127.0.0.1:8000/chat"

# ==========================================================
# SESSION STATE
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document" not in st.session_state:
    st.session_state.document = "NIST.pdf"

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("📂 Documents")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    st.divider()

    st.subheader("Current Document")

    st.selectbox(
        "",
        [
            "NIST.pdf"
        ],
        key="document"
    )

    st.divider()

    st.subheader("System")

    st.write("🤖 **Model**")
    st.caption("Llama 3.3 70B")

    st.write("🧠 **Embeddings**")
    st.caption("MiniLM-L6-v2")

    st.write("🗄 **Vector DB**")
    st.caption("FAISS")

    st.success("🟢 Ready")

# ==========================================================
# HEADER
# ==========================================================

left, right = st.columns([5,1])

with left:

    st.title("🤖 DocuMind AI")

    st.caption(
        "AI-Powered Document Intelligence Platform"
    )

with right:

    st.success("Connected")

st.divider()

# ==========================================================
# DASHBOARD
# ==========================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric("Documents", "1")
c2.metric("Chunks", "104")
c3.metric("Model", "Llama 3.3")
c4.metric("Status", "Ready")

st.divider()

# ==========================================================
# CHAT HISTORY
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ==========================================================
# CHAT INPUT
# ==========================================================

question = st.chat_input(
    "Ask anything about your document..."
)

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question":question
                    }
                )

                data = response.json()

                answer = data["answer"]

                st.markdown(answer)

                if "sources" in data:

                    with st.expander("📄 Sources"):

                        for source in data["sources"]:

                            st.write(
                                f"Page {source['page']} — {source['source']}"
                            )

                st.session_state.messages.append(
                    {
                        "role":"assistant",
                        "content":answer
                    }
                )

            except Exception:

                st.error("Cannot connect to FastAPI server.")