# Voice LLM Assistant

[Live Demo](https://voice-llm-assistant.onrender.com)

## 📝 Description
Voice LLM Assistant is a voice-enabled chatbot that integrates with Google Generative AI (Gemini 2.0 Pro) using FastAPI as the backend and a simple HTML/CSS/JavaScript frontend. It allows users to interact with an AI assistant using voice input and receive spoken responses, creating a seamless voice-based conversational experience.

## 🚀 Features
- 🎙️ **Voice Recognition:** Converts speech to text using browser-based Web Speech API.
- 💬 **LLM Integration:** Utilizes the Gemini 2.0 Pro model via LangChain's Google Generative AI integration.
- 🔊 **Text-to-Speech:** Delivers AI responses using the browser's Speech Synthesis API.
- 🌐 **FastAPI Backend:** Efficiently handles API requests to the LLM.
- 🛠️ **Bootstrap UI:** Clean and responsive frontend design.
- 🧠 **Streaming Responses:** Provides real-time response streaming from the LLM.

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** FastAPI (Python)
- **AI Model:** Gemini 2.0 Pro via LangChain
- **Hosting:** Render

## 🚦 Getting Started

### Prerequisites
- Python 3.9+
  
### Installation
1. **Clone the repository:**
```bash
git clone <repository-url>
cd voice-llm-assistant
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Setup environment variables:**
Create a `.env` file and add your API keys and configurations.
```plaintext
GOOGLE_API_KEY=your_google_genai_api_key
```

4. **Run the server:**
```bash
uvicorn server:app --host 0.0.0.0 --port 3000
```

5. **Access the app:**
Open `http://localhost:3000` in your browser.

## 🚀 Deployment
1. **Push the code to GitHub.**
2. **Create a Web Service on Render:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn server:app --host 0.0.0.0 --port 10000`
3. **Add environment variables** in the Render dashboard.
4. **Deploy and access the live app!**

## 💡 How to Use
1. Click **Start Listening** to begin voice input.
2. Speak your query to the AI assistant.
3. The AI will respond with both **text** and **speech**.
4. Use **Clear** to reset the conversation.


## 🤝 Contributing
Feel free to fork this project and submit pull requests!

## 📄 License
This project is licensed under the Apache-2.0 License.


