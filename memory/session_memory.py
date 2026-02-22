import streamlit as st

MAX_HISTORY = 10  # Prevent token overflow

def initialize_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def add_user_message(message):
    st.session_state.chat_history.append({
        "role": "user",
        "content": message
    })
    trim_history()

def add_assistant_message(message):
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": message
    })
    trim_history()

def get_chat_history():
    return st.session_state.chat_history

def clear_memory():
    st.session_state.chat_history = []

def trim_history():
    if len(st.session_state.chat_history) > MAX_HISTORY:
        st.session_state.chat_history = st.session_state.chat_history[-MAX_HISTORY:]