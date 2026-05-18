from src.langgraphai.ui.loadui import LoadUI
import streamlit as st

def load_langgraph_agentic_app():
    """
    Load Streamlit UI Agentic app

    """

    load_ui = LoadUI()
    print(f"LoadUI")
    user_input = load_ui.load_ui()
    print(f"load_ui")

    if not user_input:
        st.error("Failed to load user input")
        return

    user_input = st.chat_input("Enter you message here")
    print(f"user_input: {user_input}")