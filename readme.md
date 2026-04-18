<h1 align="center">J.A.R.V.I.S - Mark-I</h1>
<p align="center">
  <img src="assets/logo.png" width="200" alt="JARVIS Logo">
</p>
<p align="center">
  <b>Advanced AI Assistant with Voice Activation, Automation, and Computer Vision.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/OS-Windows-blue" alt="OS">
  <img src="https://img.shields.io/badge/Model-Gemini_Live-orange" alt="Model">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

---

## 🌟 Overview
Welcome to **J.A.R.V.I.S** (Just A Rather Very Intelligent System). Designed as a background-first companion, JARVIS provides a hands-free, high-performance interface for your Windows machine. Inspired by the Stark Industries aesthetic, it combines advanced LLM capabilities with local hardware control.

## ✨ Key Features
- 🎙️ **Voice Activation**: Responds instantly to "Hey Jarvis" from the background.
- 👏 **Gesture Wake**: Advanced double-clap detection for silent environments.
- 👻 **Silent Persistence**: Runs invisibly via VBScript—no terminal windows required.
- 👁️ **Visual Intelligence**: Real-time screen analysis using Computer Vision.
- 🛠️ **System Mastery**: Full control over browsers, desktop applications, and settings.
- 🎨 **Premium UI**: Dynamic, responsive Stark-tech inspired visual interface.

## 🛠️ Installation

### 1. Prerequisites
- **Python 3.10+** (Windows 10/11)
- **Microphone** (Hardware access required)
- **Gemini API Key** (v1alpha Support)

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/Alinshan/JARVIS-
cd JARVIS-

# Install core dependencies
pip install -r requirements.txt

# Setup Browser automation
playwright install chromium
```

### 3. API Configuration
Create a `.env` file in the root:
```env
GEMINI_API_KEY=your_google_api_key_here
```

### 4. Enable Startup
Register JARVIS to launch automatically when you turn on your PC:
```bash
python install_startup.py
```

## 🚀 Launch Protocols

| Mode | Command | Description |
| :--- | :--- | :--- |
| **Silent** | `launcher.vbs` | Starts invisibly in background. (Recommended) |
| **Visual** | `python main.py` | Force launch the UI immediately. |

## ⌨️ Tactical Controls
- **[F4]**: Instant Microphone Mute/Unmute.
- **[Shutdown]**: Safely terminates all modules and releases hardware.

---

<p align="center">
  <i>"Systems are online and ready for your command, Sir."</i>
</p>
