import streamlit as st
from memory.session_memory import (
    initialize_memory,
    add_user_message,
    add_assistant_message,
    get_chat_history,
    clear_memory
)
from services.gemini_service import GeminiService

st.set_page_config(
    page_title="Smart IT Career Assistant",
    page_icon="💼",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("⚙ Settings")

    if st.button("Clear Chat"):
        clear_memory()
        st.rerun()

    st.markdown("---")
    st.subheader("Supported Topics")
    st.markdown("""
    • Data Science  
    • AI / ML  
    • Software Development  
    • Cloud & DevOps  
    • Interview Preparation  
    • Resume Building  
    """)

# Main
st.title("💼 Smart IT Career Assistant")
st.markdown(
    "Ask me about tech roles, skills, certifications, salary insights, or career roadmaps."
)

initialize_memory()
service = GeminiService()

# Display chat history
for message in get_chat_history():
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask about tech careers, skills, roadmaps...")

if user_input:
    add_user_message(user_input)

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing career path..."):
            response = service.generate_response(get_chat_history())
            st.markdown(response)

    add_assistant_message(response)