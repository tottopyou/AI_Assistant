# AI Assistant for Document Search

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-brightgreen)
![LangChain](https://img.shields.io/badge/LangChain-0.2%2B-orange)
![FAISS](https://img.shields.io/badge/FAISS-1.7%2B-yellow)
![OpenAI](https://img.shields.io/badge/OpenAI-API-blue)

## Overview
This project implements an AI-powered document search assistant using the LangChain framework, OpenAI API, and FAISS (Facebook AI Similarity Search) for indexing. The assistant allows users to upload PDF or text documents and ask questions in natural language, receiving relevant answers based on the content of the uploaded files.

## Purpose
The goal of this project is to showcase how LangChain can be utilized to integrate large language models (LLMs) for intelligent document search and question-answering tasks. By combining FAISS for fast similarity search and OpenAI’s language models for generating responses, this project demonstrates practical applications of NLP in document processing.

## How It Works
1. The user uploads a PDF or text file.
2. The document text is extracted and indexed using FAISS for efficient similarity searching.
3. The user submits a query, which is processed by an OpenAI model to retrieve relevant information from the indexed document.
4. The assistant responds with the most relevant section of the document based on the user's query.

## Technologies Used
- **Python 3.8+**: Core language for the project.
- **Streamlit**: Front-end framework for creating the interactive UI to upload documents and query them.
- **LangChain**: Framework for building the document search and question-answering pipeline.
- **FAISS**: Utilized for vector-based document indexing and similarity search.
- **OpenAI API**: Provides the language models that process user queries and generate intelligent responses.
