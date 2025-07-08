# 📚 Langchain PDF Q&A App

An AI application that allows you to upload PDF documents and ask questions about their content using Google's Gemini AI and FAISS vector database.

---

![Workflow](Ask_Book_Questions_Workflow.jpg)

---

## Live Deployment
[Streamlit Live](https://langchain-pdf-reader.streamlit.app/)
## 🛡️ Monitoring & Educational Logging

This project includes a `monitor.py` module that provides comprehensive, educational logging of all major pipeline steps:
- PDF upload
- Text extraction
- Text chunking
- Embedding creation
- Vector store creation
- Chain creation
- User question received
- Query embedding
- Semantic search
- Knowledge base search
- Ranked results
- LLM response
- Error handling

All logs will be written to `monitor.log` with clear explanations, making it easy for new learners to understand what happens under the hood in a modern LLM-powered RAG system.

## 🌟 Features

- **PDF Document Processing**: Upload and extract text from PDF files
- **Intelligent Text Chunking**: Smart text splitting for optimal context retrieval
- **Vector Embeddings**: Uses Google's Gemini embeddings for semantic understanding
- **FAISS Vector Database**: Fast and efficient similarity search
- **Conversational AI**: Interactive Q&A with conversation memory
- **Streamlit UI**: Clean and intuitive web interface
- **Error Handling**: Graceful handling of API rate limits and errors
- **Chat History**: Maintains conversation context across questions

## 🏗️ Architecture

The application follows a modern RAG (Retrieval-Augmented Generation) architecture:

```
PDF Upload → Text Extraction → Text Chunking → Vector Embeddings → FAISS Storage → Query Processing → AI Response
```

### Core Components:

1. **PDF Processor**: Extracts text from uploaded PDF documents
2. **Text Splitter**: Divides text into manageable chunks with overlap
3. **Embedding Engine**: Converts text chunks to vector representations using Gemini
4. **Vector Store**: FAISS database for efficient similarity search
5. **Conversational Chain**: LangChain's ConversationalRetrievalChain for Q&A
6. **Web Interface**: Streamlit-based user interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Internet connection for API calls

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Langchain-PDF-App
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   Open your browser and go to `http://localhost:8501`

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit>=1.28.0
langchain>=0.1.0
langchain-google-genai>=2.1.0
langchain-community>=0.0.10
faiss-cpu>=1.7.4
PyPDF2>=3.0.0
python-dotenv>=1.0.0
pydantic>=2.0.0
google-generativeai>=0.3.0
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google Gemini API key | Yes |

### Model Configuration

The app uses the following models:
- **Embeddings**: `models/embedding-001` (Gemini embedding model)
- **LLM**: `gemini-1.5-flash` (Gemini Flash for faster responses)

### Text Chunking Parameters

```python
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,      # Characters per chunk
    chunk_overlap=200,    # Overlap between chunks
    length_function=len
)
```

## 💡 Usage

### Basic Workflow

1. **Upload PDF**: Use the file uploader to select your PDF document
2. **Wait for Processing**: The app will extract text and create embeddings
3. **Ask Questions**: Type your questions in the text input field
4. **View Responses**: Get AI-generated answers based on your PDF content
5. **Continue Conversation**: Ask follow-up questions with context awareness

### Example Questions

- "What is the main topic of this document?"
- "Summarize the key points from chapter 3"
- "What are the conclusions mentioned in the paper?"
- "Explain the methodology used in this research"

## 🔍 How It Works

### 1. Document Processing
- PDF text extraction using PyPDF2
- Text cleaning and preprocessing
- Intelligent chunking with overlap for context preservation

### 2. Vector Embeddings
- Each text chunk is converted to a high-dimensional vector
- Uses Google's Gemini embedding model for semantic understanding
- Vectors capture meaning, not just keywords

### 3. Similarity Search
- FAISS vector database stores all embeddings
- When you ask a question, it's also converted to a vector
- FAISS finds the most similar text chunks to your question

### 4. AI Response Generation
- Relevant text chunks are retrieved from FAISS
- Gemini AI generates a contextual answer using the retrieved information
- Conversation history is maintained for context

## 🛠️ Technical Details

### Dependencies Breakdown

- **Streamlit**: Web application framework
- **LangChain**: LLM orchestration and chains
- **FAISS**: Vector similarity search (Facebook AI Similarity Search)
- **PyPDF2**: PDF text extraction
- **Google Generative AI**: Gemini embeddings and text generation
- **Pydantic**: Data validation and settings management

### Performance Considerations

- **Chunk Size**: 1000 characters with 200 character overlap
- **Vector Dimensions**: Determined by Gemini embedding model
- **Search Efficiency**: FAISS provides sub-linear search complexity
- **Memory Usage**: Vectors are stored in memory for fast access

## 🚨 Error Handling

The application includes comprehensive error handling for:

- **API Rate Limits**: Graceful handling of quota exceeded errors
- **Missing API Keys**: Clear error messages for configuration issues
- **PDF Processing Errors**: Validation of uploaded files
- **Network Issues**: Retry logic for API calls

## 🔒 Security Considerations

- API keys are stored in environment variables
- No sensitive data is logged or stored
- Temporary file processing (no permanent storage)
- Secure API communication with Google services

## 📊 Limitations

- **API Rate Limits**: Free tier has daily and per-minute limits
- **File Size**: Large PDFs may take longer to process
- **Text Quality**: OCR-dependent PDFs may have lower accuracy
- **Language Support**: Primarily optimized for English text

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Cloud Deployment Options

1. **Streamlit Cloud**
   - Connect your GitHub repository
   - Set environment variables in Streamlit Cloud dashboard
   - Automatic deployment on push

2. **Current Live Streamlit**
   - [Streamlit] (https://langchain-pdf-reader.streamlit.app/)
     
3. **Local Deployment**
   - cd \Langchain PDF App
   - run ---> streamlit run app.py
     
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Check [AO](https://www.youtube.com/@alejandro_ao) 
