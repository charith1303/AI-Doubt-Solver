import json
import os
import streamlit as st


HISTORY_FILE = "data/chat_history.json"


def load_history():
    """
    Loads chat history from JSON file.
    """

    if not os.path.exists(HISTORY_FILE):

        return []

    try:

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:

            return json.load(file)

    except Exception:

        return []


def save_history(messages):
    """
    Saves chat history to JSON file.
    """

    os.makedirs("data", exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            messages,
            file,
            indent=4,
            ensure_ascii=False
        )


def initialize_chat():
    """
    Loads previous chat history.
    """

    if "messages" not in st.session_state:

        st.session_state["messages"] = load_history()


def add_user_message(message):
    """
    Adds user message.
    """

    st.session_state["messages"].append(
        {
            "role": "user",
            "content": message
        }
    )

    save_history(st.session_state["messages"])


def add_ai_message(message, sources=None):
    """
    Adds AI message.
    """

    if sources is None:

        sources = []

    st.session_state["messages"].append(
        {
            "role": "assistant",
            "content": message,
            "sources": sources
        }
    )

    save_history(st.session_state["messages"])


def get_chat_history():

    history = ""

    for msg in st.session_state["messages"]:

        history += f"{msg['role']}: {msg['content']}\n"

    return history


def clear_chat():
    """
    Clears both session and saved history.
    """

    st.session_state["messages"] = []

    save_history([])