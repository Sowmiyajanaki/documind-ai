import streamlit as st
from utils.api import dashboard


def render_dashboard(selected_document):

    data = dashboard()

    st.markdown("""
    <style>

    .metric-card{
        background:#ffffff;
        border:1px solid #e5e7eb;
        border-radius:12px;
        padding:18px;
        text-align:center;
        height:120px;
    }

    .metric-title{
        color:#6b7280;
        font-size:15px;
        font-weight:600;
        margin-bottom:12px;
    }

    .metric-value{
        color:#111827;
        font-size:24px;
        font-weight:700;
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📄 Documents</div>
            <div class="metric-value">{data['documents']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📚 Current Document</div>
            <div class="metric-value" style="font-size:18px;">
                {selected_document}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🤖 Model</div>
            <div class="metric-value" style="font-size:18px;">
                {data['model']}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🟢 Status</div>
            <div class="metric-value">
                {data['status']}
            </div>
        </div>
        """, unsafe_allow_html=True)