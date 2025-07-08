# 🚀 Deploy to Streamlit Cloud

This project includes a complete deployment module for Streamlit Cloud with minimal requirements.

## Quick Start

1. **Navigate to the deployment directory:**
   ```bash
   cd deploy
   ```

2. **Run the deployment checker:**
   ```bash
   python deploy.py
   ```

3. **Follow the instructions provided by the checker**

## What's Included

The `deploy/` directory contains:

- **`streamlit_app.py`** - Optimized main application
- **`requirements.txt`** - Minimal dependencies with specific versions
- **`.streamlit/config.toml`** - Streamlit configuration
- **`README.md`** - Detailed deployment instructions
- **`deploy.py`** - Deployment validation script
- **`setup.py`** - Package setup (optional)

## Key Optimizations

✅ **Removed monitoring** - Eliminated the `monitor.py` dependency for cleaner deployment  
✅ **Minimal requirements** - Only essential packages with specific versions  
✅ **Better error handling** - Improved user experience with clear error messages  
✅ **Chat interface** - Modern chat UI with message history  
✅ **Source references** - Shows which parts of the PDF were used  
✅ **Rate limit handling** - Graceful handling of API limits  

## Requirements

- Google AI API key (Gemini)
- GitHub account
- Streamlit Cloud account

## Next Steps

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Push your code to GitHub
3. Deploy on [Streamlit Cloud](https://langchain-pdf-reader.streamlit.app/)
4. Add your API key in the Streamlit secrets

For detailed instructions, see `deploy/README.md` 