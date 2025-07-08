import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from pydantic import SecretStr

# Load environment variables
load_dotenv()

def main():
    st.set_page_config(
        page_title="PDF Q&A Assistant",
        page_icon="📚",
        layout="wide"
    )
    
    st.title("📚 PDF Question & Answer Assistant")
    st.markdown("Upload a PDF and ask questions about its content!")
    
    # Check for API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("⚠️ GOOGLE_API_KEY not found. Please add it to your Streamlit secrets.")
        st.info("To add your API key, go to your Streamlit app settings and add it as a secret.")
        return
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=['pdf'],
        help="Upload a PDF file to analyze"
    )
    
    if uploaded_file is not None:
        try:
            # Extract text from PDF
            with st.spinner("📖 Reading PDF..."):
                pdf_reader = PdfReader(uploaded_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
            
            st.success(f"✅ Successfully read {len(pdf_reader.pages)} pages")
            
            # Split text into chunks
            with st.spinner("✂️ Processing text..."):
                text_splitter = CharacterTextSplitter(
                    separator="\n",
                    chunk_size=1000,
                    chunk_overlap=200,
                    length_function=len
                )
                chunks = text_splitter.split_text(text)
            
            # Create embeddings
            with st.spinner("🧠 Creating embeddings..."):
                embeddings = GoogleGenerativeAIEmbeddings(
                    model="models/embedding-001",
                    google_api_key=SecretStr(api_key)
                )
                knowledge_base = FAISS.from_texts(chunks, embeddings)
            
            # Create conversation chain
            with st.spinner("🔗 Setting up AI assistant..."):
                llm = GoogleGenerativeAI(
                    model="gemini-1.5-flash",
                    google_api_key=SecretStr(api_key)
                )
                chain = ConversationalRetrievalChain.from_llm(
                    llm=llm,
                    retriever=knowledge_base.as_retriever(),
                    return_source_documents=True
                )
            
            st.success("🎉 Ready to answer questions!")
            
            # Initialize chat history
            if "messages" not in st.session_state:
                st.session_state.messages = []
            
            # Display chat messages
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # Chat input
            if prompt := st.chat_input("Ask a question about your PDF..."):
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)
                
                # Get AI response
                with st.chat_message("assistant"):
                    with st.spinner("🤔 Thinking..."):
                        try:
                            response = chain.invoke({
                                "question": prompt,
                                "chat_history": [(msg["content"], "") for msg in st.session_state.messages[:-1]]
                            })
                            
                            answer = response["answer"]
                            
                            # Add assistant response to chat history
                            st.session_state.messages.append({"role": "assistant", "content": answer})
                            st.markdown(answer)
                            
                            # Show sources if available
                            if response.get("source_documents"):
                                with st.expander("📄 View Sources"):
                                    for i, doc in enumerate(response["source_documents"][:3]):
                                        st.markdown(f"**Source {i+1}:**")
                                        st.markdown(doc.page_content[:300] + "...")
                                        
                        except Exception as e:
                            error_msg = f"Sorry, I encountered an error: {str(e)}"
                            st.error(error_msg)
                            st.session_state.messages.append({"role": "assistant", "content": error_msg})
            
            # Clear chat button
            if st.button("🗑️ Clear Chat History"):
                st.session_state.messages = []
                st.rerun()
                
        except Exception as e:
            st.error(f"❌ Error processing PDF: {str(e)}")
            if "quota" in str(e).lower() or "429" in str(e):
                st.warning("Rate limit exceeded. Please try again later.")
    
    else:
        st.info("👆 Please upload a PDF file to get started!")

if __name__ == "__main__":
    main() 