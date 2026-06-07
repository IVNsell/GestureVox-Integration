# GestureVox Integration

🏆 **INFOMATRIX World 2024 - Platinum (1st Place)**  
Voice-controlled desktop assistant with hand gesture recognition.

> Multi-modal AI assistant: speak commands, control your PC with gestures, and interact through a modern desktop GUI.

**Author:** [Ivan Gaidarov](https://github.com/IVNsell)  
**Competition:** [INFOMATRIX World Finals](https://www.infomatrix.ro/) — Programming category

---

## Overview

GestureVox Integration is a Windows desktop assistant that combines **voice commands** and **camera-based hand gestures** for hands-free computer control. Built for the INFOMATRIX World 2024 championship, the project won **Platinum (1st place)** in the voice assistant + gestures category.

The assistant listens for a wake phrase, recognizes speech, executes system commands, and supports gesture-based control via webcam.

> **Note:** Custom wake-word training is in a **separate repository** (free Porcupine alternative). This project uses a different activation flow.

---

## Features

### 🎤 Voice Control
- Speech recognition with **faster-whisper** (GPU-accelerated)
- Configurable assistant name / wake phrase (`settings.json`)
- Fuzzy command matching for robust recognition
- AI chat integration (LLM via g4f client)
- Text-to-speech responses

### 👋 Gesture Control
- **MediaPipe Hands** - real-time hand tracking via webcam
- Custom gesture training and recognition (`Gesture_crt.py`)
- Swipe gestures for navigation (`OpenCV_plus_ultra.py`)
- Gesture + voice multimodal interaction

### 🖥 System Automation
- Volume & brightness control
- Open/close applications (Steam, Terraria, browsers)
- Music playback & YouTube playlist search
- Weather & time queries
- Battery level alerts
- Window management, Bluetooth, Wi-Fi utilities

### 🎨 Desktop GUI
- Modern UI built with **CustomTkinter**
- Real-time assistant status and feedback

---

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| Speech | faster-whisper, SpeechRecognition, PyAudio |
| Gestures | MediaPipe, OpenCV |
| AI | g4f (LLM client) |
| GUI | CustomTkinter, Pygame |
| Audio | pydub, simpleaudio, HierSpeechpp (TTS) |
| System | pyautogui, pycaw, screen_brightness_control |

**Language:** Python 3.x  
**Platform:** Windows (primary)

---

## Project Structure
