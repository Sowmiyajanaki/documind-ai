import streamlit as st

from utils.api import chat


def render_chat(document):
    """
    Render the chat interface.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    question = st.chat_input(
        "Ask anything about your document..."
    )

    if question:

        # User message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Assistant message
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                try:

                    response = chat(
                        question,
                        document
                    )

                    answer = response["answer"]

                    st.markdown(answer)

                    # Store assistant reply
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                    # Show sources
                    if response["sources"]:

                        with st.expander("📄 Sources"):

                            for source in response["sources"]:

                                st.write(
                                    f"**Page:** {source['page']} | **File:** {source['source']}"
                                )

                except Exception as e:

                    st.error(str(e))