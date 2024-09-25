import streamlit as st
import pdfplumber
import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader

os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxx"

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text


def create_faiss_index(documents):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(documents, embeddings)
    return vector_store


def answer_question(query, index):
    llm = OpenAI(temperature=0.7)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=index.as_retriever())
    answer = qa_chain.run(query)
    return answer


st.title("AI Assistant for Document Search")

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
    else:
        st.error("Unsupported file format!")

    st.write("Document Text Preview:")
    st.text_area(label="Document Text", value=text[:2000], height=300)

    index = create_faiss_index([text])

    query = st.text_input("Enter your query")

    if query:
        answer = answer_question(query, index)
        st.write("Answer:")
        st.write(answer)