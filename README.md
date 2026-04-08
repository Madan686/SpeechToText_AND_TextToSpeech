# 🎙️ Voice Assistant (Speech-to-Text + Text-to-Speech)

A simple Python-based voice assistant that supports:

* Speech-to-Text (STT) → Convert spoken words into text and save them
* Text-to-Speech (TTS) → Convert typed text into speech
* Real-time microphone input
* Automatic transcription saving

---

## 📌 Features

* 🎤 Select microphone from available devices
* 🧠 Convert speech to text using Google Speech Recognition
* 💾 Save transcriptions to a file automatically
* 🔊 Convert text into speech using `pyttsx3` (offline)
* 🛑 Voice command to stop listening (`exit listening mode`)
* 📂 Automatically opens saved file after session

---

## 🛠️ Tech Stack

* Python 3.x
* `SpeechRecognition` (for STT)
* `pyttsx3` (for TTS)
* `pyaudio` (for microphone input)

---

## ⚙️ Installation

### 1. Clone or Download Project

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

### 2. Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

#### ⚠️ If `pyaudio` fails on Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧭 Usage

After running, you will see:

```
Choose an option:
1) Speech-to-Text (STT)
2) Text-to-Speech (TTS)
3) Exit
```

---

### 🔹 Option 1: Speech-to-Text

* Select microphone index
* Speak normally
* Your speech will:

  * be printed on screen
  * be saved to a text file

Say:

```
exit listening mode
```

to stop recording

---

### 🔹 Option 2: Text-to-Speech

* Enter any text
* System will speak it aloud

---

## 📁 Output

* Transcriptions are saved in:

```
C:\Users\Madan\Desktop\Machine_learning2\savedfile.txt
```

---

## ⚠️ Important Notes

* 🌐 Internet is required for Speech Recognition (Google API)
* 🎤 Ensure microphone permissions are enabled
* 🔊 Voice availability depends on your system

---

## 🐛 Common Issues & Fixes

### 1. Microphone not detected

* Check system microphone settings
* Run:

```python
import speech_recognition as sr
print(sr.Microphone.list_microphone_names())
```

---

### 2. `pyaudio` installation error

Use:

```bash
pip install pipwin
pipwin install pyaudio
```

---

### 3. Speech not recognized

* Speak clearly
* Reduce background noise
* Check internet connection

---

### 4. Wrong voice selected

* Voice index depends on system
* Try different index values

---

## 🚀 Future Improvements

* Offline speech recognition (Vosk / Whisper)
* Voice commands (open apps, search, etc.)
* GUI (Tkinter / Web UI)
* AI integration (ChatGPT / RAG system)

---

## 📌 Author

Madan

---

## 📄 License

This project is for educational and personal use.
