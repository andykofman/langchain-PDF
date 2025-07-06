from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from pydantic import SecretStr
import re

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")
    
    # upload file
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    
    # extract the text
    if pdf is not None:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()
        
      # split into chunks
      text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
      )
      chunks = text_splitter.split_text(text)
      
      # Create embeddings using Gemini API
      api_key = os.getenv("GOOGLE_API_KEY")
      if api_key:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=SecretStr(api_key))
      else:
        st.error("GOOGLE_API_KEY not found in environment variables")
        return
      
      # Create FAISS vector store
      knowledge_base = FAISS.from_texts(chunks, embeddings)
      
      # Create conversational chain
      llm = GoogleGenerativeAI(model="gemini-pro")
      chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=knowledge_base.as_retriever()
      )
      
      # Show chat interface
      user_question = st.text_input("Ask a question about your PDF:")
      
      if user_question:
        response = chain.run(user_question)
        st.write(response)

if __name__ == "__main__":
    main()
