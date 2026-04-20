import streamlit as st
from src.rag import ask_question

st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title("🤖 RAG Chatbot")

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box
query = st.chat_input("Ask a question...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = ask_question(query)
            except Exception as e:
                answer = f"Error: {e}"

            st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})