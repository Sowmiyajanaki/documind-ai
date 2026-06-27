import streamlit as st

from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
from components.chat import render_chat

# ===========================================
# PAGE CONFIGURATION
# ===========================================

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================================
# GLOBAL CSS
# ===========================================

st.markdown("""
<style>

/* ---------- Main ---------- */

.block-container{
    padding-top:0.8rem;
    padding-bottom:0.8rem;
}

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"] .block-container{
    padding-top:0.4rem !important;
    padding-bottom:0.4rem !important;
    padding-left:0.8rem !important;
    padding-right:0.8rem !important;
}

/* Reduce spacing between widgets */
section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div{
    margin-bottom:0.15rem !important;
}

/* Reduce paragraph/caption spacing */
section[data-testid="stSidebar"] p{
    margin-top:0.15rem !important;
    margin-bottom:0.15rem !important;
}

/* Reduce heading spacing */
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] h5{
    margin-top:0rem !important;
    margin-bottom:0.2rem !important;
}

/* Reduce divider spacing */
section[data-testid="stSidebar"] hr{
    margin-top:0.45rem !important;
    margin-bottom:0.45rem !important;
}

/* Smaller alert/info/success boxes */
section[data-testid="stSidebar"] div[data-testid="stAlert"]{
    padding:0.35rem 0.75rem !important;
    border-radius:8px;
}

/* File uploader spacing */
section[data-testid="stSidebar"] div[data-testid="stFileUploader"]{
    margin-top:-0.15rem;
    margin-bottom:-0.15rem;
}

/* Smaller select box */
section[data-testid="stSidebar"] div[data-baseweb="select"]{
    min-height:36px;
}

/* Rounded buttons */
button{
    border-radius:8px;
}

/* Hide Streamlit branding */
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ===========================================
# HEADER
# ===========================================

left, right = st.columns([5, 1])

with left:
    st.title("🤖 DocuMind AI")
    st.caption("AI-Powered Document Intelligence Platform")

with right:
    st.success("🟢 Connected")

st.divider()

# ===========================================
# SIDEBAR
# ===========================================

try:
    selected_document = render_sidebar()
except Exception as e:
    st.exception(e)
    st.stop()

# ===========================================
# DASHBOARD
# ===========================================

try:
    render_dashboard(selected_document)
except Exception as e:
    st.exception(e)
    st.stop()

st.divider()

# ===========================================
# CHAT
# ===========================================

if selected_document is None:

    st.info("📂 Upload and process a PDF to start chatting.")

else:

    try:
        render_chat(selected_document)
    except Exception as e:
        st.exception(e)
        st.stop()