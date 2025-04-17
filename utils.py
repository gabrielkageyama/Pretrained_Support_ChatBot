import os
from PyPDF2 import PdfReader
import streamlit as st
from FAISS_compatibility import CompatibleFAISS
from retriever import get_compatible_retriever
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub

def conversation_chain(vectorstore):
                #you can change this for your API Key or configure your .env with it
    api_token = os.getenv("HUGGINGFACE_API_TOKEN")
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-xxl",
        huggingfacehub_api_token=api_token,
        model_kwargs={"temperature": 0.3,
                      "max_new_tokens": 512},
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = get_compatible_retriever(vectorstore)

    conversation = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
    )
    print(conversation)

    return conversation


def create_vectorstore(chunks):
    try:
        #Recommend using some API service (like OpenAi) to do the embeddings remotely,
        #this task can be really hard on your hardware
        embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl", model_kwargs={"device": "cpu"})

        vectorstore = CompatibleFAISS.from_texts(texts=chunks, embedding=embeddings)

        return vectorstore
    except Exception as e:
        st.error(f"An error occurred while creating the vectorstore: {e}")
        return None


def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)

    return chunks


def get_text():
    try:                                                    # ADD here your training data for the AI
        pdf_path = os.path.join(os.path.dirname(__file__), "training_data", "features_sap_sales_cloud.pdf")
        pdf_reader = PdfReader(pdf_path)
        return ''.join(page.extract_text() for page in pdf_reader.pages)
    except FileNotFoundError:
        st.error("PDF file not found.")
    except Exception as e:
        st.error(f"An error occurred while reading the PDF: {e}")
    return ""
