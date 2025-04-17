from html_template import bot_template, user_template, css
import streamlit as st
from utils import get_text, get_chunks, create_vectorstore, conversation_chain

def streamlit_app():
    st.set_page_config(page_title="Pretrained Support ChatBot")

    st.write(css, unsafe_allow_html=True)

    st.header("Ask anything to the Pretrained Support ChatBot")
    user_input = st.text_input("Ask your question here:")
    if st.button("New Chat"):
        st.session_state.chat_history = []

    st.session_state.conversation = None
    st.session_state.chat_history = None

    with st.spinner("Loading..."):
        text = get_text()
        chunks = get_chunks(text)
        vectorstore = create_vectorstore(chunks)
        print("Ready to chat!")

    if vectorstore:
        st.session_state.conversation = conversation_chain(vectorstore)


    if user_input:

        #'st.session_state.conversation' can fail in allocating the question correctly,
        #still figuring out how to make it more consistent

        response = st.session_state.conversation({"question": user_input})

        #for debug purposes
        print("Question", response.get("question", ""))
        print("Response:", response)
        print("Chat History:", response.get("chat_history", []))

        st.session_state.chat_history = st.session_state.conversation({"question": user_input})["chat_history"]

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
