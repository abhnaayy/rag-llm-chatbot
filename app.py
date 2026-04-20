import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", layout="centered")

st.title("🤖 RAG Chatbot")

# Clear button (optional)
if st.button("Clear Chat"):
    st.session_state.messages = []

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
query = st.chat_input("Ask a question...")

if query:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    # Call API
    try:
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"query": query}
            )

        if response.status_code == 200:
            answer = response.json()["answer"]
        else:
            answer = f"Error: {response.text}"

    except Exception as e:
        answer = f"Connection error: {e}"

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)