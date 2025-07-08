#!/usr/bin/env python3
"""
Installation helper script for PDF Q&A Assistant
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Requirements installed successfully!")
            return True
        else:
            print(f"❌ Installation failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Installation error: {e}")
        return False

def main():
    print("🔧 PDF Q&A Assistant - Installation Helper")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found. Make sure you're in the deploy directory.")
        return
    
    if install_requirements():
        print("\n🎉 Installation complete!")
        print("You can now run: python deploy.py")
    else:
        print("\n❌ Installation failed. Please check the error messages above.")

if __name__ == "__main__":
    main() 