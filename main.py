from dotenv import load_dotenv
from templates.streamlit_template import streamlit_app
import streamlit as st

def main():
    load_dotenv()

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    streamlit_app()


if __name__ == '__main__':
    main()
