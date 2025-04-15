# 🤖 AI-Powered Chat Assistant Made With Tkinter

A **full-featured Python tkinter application** that combines secure user authentication with advanced AI chat capabilities. Built with Tkinter/CustomTkinter for a modern interface, integrated with Gemini AI for intelligent responses, and packed with productivity tools for content management.

## ✨ Key Features

### 🔒 Secure Authentication System
- User registration with username/password
- Password reset functionality
- Secure login flow with validation

### 💬 Intelligent Chat Management
- Create and organize multiple chat sessions
- Delete chats with confirmation
- Persistent chat history storage

### 🎙️ Multimodal Interaction
- Voice-to-text transcription
- Traditional text input

### 📄 Content Export Tools
- Export full chat transcripts to PDF
- Save conversations locally
- Printable formatted outputs

### 🎥 YouTube Integration
- Paste any YouTube link for automatic processing
- AI-generated video summaries

### 🧠 AI Capabilities
- Powered by Google's Gemini AI
- Context-aware conversations
- Customizable response styles

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `tkinter` | Base GUI |
| `customtkinter` | Modern UI components |
| `Pillow` (PIL) | Image processing |
| `mysql-connector-python` | Database connectivity |
| `google-generativeai` | Gemini AI integration |
| `speechrecognition` | Voice input processing |
| `youtube-transcript-api` | YouTube captions fetching |
| Local `Methods/` modules | Core application functionality |

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Python-Tkinter-ChatBot
   cd Python-Tkinter-ChatBot

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows

3. **Install Required Packages**:
      ```bash
   pip install tkinter customtkinter Pillow mysql-connector-python
   python-dotenv google-generativeai speechrecognition youtube-transcript-api
   pyttsx3 pypdf2
4. **Configure Environment**:
   ```ini
   Create .env file with:
   
   API_KEY = your_api_key_here
   DATA_BASE_NAME = your_db_name
   DATA_BASE_USER="root" = your_username
   DATA_BASE_PASSWORDD = your_password

      SEED_MESSAGE = "You are a personal assistant named Jarvis. Your main goal is to help the user with their tasks. You have a professional and straightforward       personality. From now on, every response you give must be formatted as a plain Python dictionary (without any Python code tags). If the user's message contains a YouTube URL, respond with:  {2: 'hello'} Otherwise, respond with: {1: 'your response here'} Do not say 'I understand' or comment on these instructions. Begin playing your character immediately and follow these formatting rules strictly in all future messages."

5. **Run the Application**:
   ```bash
   python main.py

