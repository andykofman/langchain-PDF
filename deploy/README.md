# PDF Q&A Assistant - Streamlit Deployment

This directory contains the optimized version of the PDF Q&A Assistant for Streamlit Cloud deployment.

## 🚀 Quick Deployment

### 1. Prerequisites
- A Google AI API key (Gemini)
- A GitHub account
- A Streamlit Cloud account

### 2. Setup Steps

1. **Fork/Clone this repository** to your GitHub account

2. **Get your Google AI API Key:**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key

3. **Deploy to Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.https://langchain-pdf-reader.streamlit.app/.io)
   - Sign in with GitHub
   - Click "New app"
   - Set repository to your forked repo
   - Set main file path to: `deploy/streamlit_app.py`
   - Click "Deploy"

4. **Add your API Key:**
   - In your Streamlit app dashboard, go to "Settings" → "Secrets"
   - Add your API key:
   ```toml
   GOOGLE_API_KEY = "your-api-key-here"
   ```

### 3. File Structure
```
deploy/
├── streamlit_app.py      # Main application
├── requirements.txt      # Dependencies
├── .streamlit/
│   └── config.toml      # Streamlit configuration
└── README.md            # This file
```

### 4. Features
- ✅ PDF text extraction
- ✅ Semantic search with embeddings
- ✅ Conversational Q&A with Gemini
- ✅ Chat interface with history
- ✅ Source document references
- ✅ Error handling and rate limiting
- ✅ Responsive design

### 5. Troubleshooting

**Common Issues:**
- **API Key Error:** Make sure your `GOOGLE_API_KEY` is set in Streamlit secrets
- **Rate Limiting:** The free tier has limits. Consider upgrading for production use
- **Large PDFs:** Very large PDFs may timeout. Consider splitting into smaller files

**Performance Tips:**
- Use PDFs under 50 pages for best performance
- The app processes text in chunks for efficiency
- Chat history is maintained during the session

### 6. Local Development

To run locally:
```bash
cd deploy

# Install dependencies
python install.py
# OR manually: pip install -r requirements.txt

# Test deployment
python deploy.py

# Run the app
streamlit run streamlit_app.py
```

Make sure to create a `.env` file with your `GOOGLE_API_KEY`. 