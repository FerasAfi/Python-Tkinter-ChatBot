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
   git clone https://github.com/yourusername/tkinter-chatbot.git
   cd tkinter-chatbot

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
   
   GEMINI_API_KEY=your_api_key_here
   DB_HOST=your_mysql_host
   DB_USER=your_username
   DB_PASSWORD=your_password
5. **Run the Application**:
   ```bash
   python main.py

