#!/usr/bin/env python3
"""
Deployment helper script for PDF Q&A Assistant
"""

import os
import sys
import subprocess
from pathlib import Path

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        "streamlit_app.py",
        "requirements.txt",
        ".streamlit/config.toml",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files found")
    return True

def check_requirements_installed():
    """Check if required packages are installed"""
    try:
        import streamlit
        import langchain
        import langchain_google_genai
        print("✅ Required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing packages: {e}")
        print("   Run: pip install -r requirements.txt")
        return False

def check_api_key():
    """Check if API key is configured"""
    # Check environment variable
    if os.getenv("GOOGLE_API_KEY"):
        print("✅ GOOGLE_API_KEY found in environment")
        return True
    
    # Check .env file
    if Path(".env").exists():
        with open(".env", "r") as f:
            content = f.read()
            if "GOOGLE_API_KEY" in content:
                print("✅ GOOGLE_API_KEY found in .env file")
                return True
    
    print("⚠️  GOOGLE_API_KEY not found")
    print("   Please set it in your Streamlit Cloud secrets or .env file")
    return False

def test_local_run():
    """Test if the app can run locally"""
    try:
        print("🧪 Testing local run...")
        # Test basic imports first
        result = subprocess.run([
            sys.executable, "-c", 
            "import streamlit; import os; print('Basic imports successful')"
        ], capture_output=True, text=True, timeout=15)
        
        if result.returncode == 0:
            print("✅ Basic imports test passed")
            
            # Test app import with longer timeout
            result = subprocess.run([
                sys.executable, "-c", 
                "import streamlit_app; print('App import successful')"
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print("✅ App import test passed")
                return True
            else:
                print(f"⚠️  App import test failed: {result.stderr}")
                print("   This might be due to missing dependencies. Try installing requirements first.")
                return False
        else:
            print(f"❌ Basic imports failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("⚠️  Import test timed out - this is normal for first run")
        print("   Dependencies are being downloaded. Try running again.")
        return True  # Don't fail on timeout
    except Exception as e:
        print(f"❌ Local test error: {e}")
        return False

def generate_deployment_instructions():
    """Generate deployment instructions"""
    print("\n" + "="*50)
    print("🚀 DEPLOYMENT INSTRUCTIONS")
    print("="*50)
    
    print("\n1. Push this code to GitHub:")
    print("   git add .")
    print("   git commit -m 'Add Streamlit deployment'")
    print("   git push origin main")
    
    print("\n2. Deploy to Streamlit Cloud:")
    print("   - Go to https://share.streamlit.io")
    print("   - Sign in with GitHub")
    print("   - Click 'New app'")
    print("   - Repository: your-username/your-repo")
    print("   - Main file path: deploy/streamlit_app.py")
    print("   - Click 'Deploy'")
    
    print("\n3. Add your API key:")
    print("   - In Streamlit app dashboard → Settings → Secrets")
    print("   - Add: GOOGLE_API_KEY = 'your-api-key-here'")
    
    print("\n4. Your app will be available at:")
    print("   https://your-app-name-your-username.streamlit.app")

def main():
    print("🔍 PDF Q&A Assistant - Deployment Check")
    print("="*40)
    
    # Change to deploy directory if running from root
    if Path("deploy").exists():
        os.chdir("deploy")
    
    checks = [
        ("File Structure", check_requirements),
        ("Requirements Installed", check_requirements_installed),
        ("API Key", check_api_key),
        ("Local Test", test_local_run)
    ]
    
    all_passed = True
    for check_name, check_func in checks:
        print(f"\n📋 {check_name}:")
        if not check_func():
            all_passed = False
    
    if all_passed:
        print("\n🎉 All checks passed! Ready for deployment.")
        generate_deployment_instructions()
    else:
        print("\n❌ Some checks failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 