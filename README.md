# 🚀 Smart IT Career Assistant  
### Real-Time AI Career Chatbot using Google Gemini API

Smart IT Career Assistant is a domain-specific AI chatbot built using **Google Gemini API** and **Streamlit**.  
The system provides structured guidance on tech roles, skill development, certifications, career transitions, and interview preparation.

This project demonstrates how to design and implement a modular, production-style Generative AI application with clean backend architecture.

---

## 🧠 Problem Statement

Build a domain-specific GenAI chatbot that:

- Integrates Google Gemini API
- Uses secure API key management via environment variables
- Implements structured prompt engineering
- Supports multi-turn contextual conversations
- Follows modular backend architecture
- Includes logging and error handling
- Uses Streamlit for an interactive UI

---

## 📁 Project Structure

```
genai-career-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
├── memory/
├── prompts/
├── services/
├── utils/
└── logs/
```

### Module Responsibilities

- **app.py** → UI rendering and user interaction  
- **services/** → Gemini API integration and response handling  
- **prompts/** → Structured prompt engineering  
- **memory/** → Multi-turn conversation management  
- **utils/** → Logging and helper utilities  
- **config/** → Secure environment configuration  

---

## 🏗 System Architecture

```
User
  ↓
Streamlit UI
  ↓
Backend Engine
  ↓
Prompt Builder
  ↓
Gemini API
  ↓
Response Processing
  ↓
UI Rendering
```

The architecture ensures separation of concerns, maintainability, and scalability.

---

## ⚙️ Features

- Secure Gemini API integration  
- Environment-based configuration  
- Structured system prompts  
- Multi-turn session memory  
- Token-aware context handling  
- Logging of API calls and errors  
- Retry and fallback handling  
- Clean and responsive Streamlit interface  

---

## 💡 Supported Topics

- Data Science  
- AI / ML  
- Software Development  
- Cloud & DevOps  
- Interview Preparation  
- Resume Building  

---

## ▶️ How to Run the Application

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Create `.env` File

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-1.5-flash
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

Open in your browser:

```
http://localhost:8501
```

---

## 🎯 Project Objective

This project demonstrates the practical implementation of a structured GenAI chatbot system using Google Gemini API. It highlights skills in:

- Backend modular design  
- Prompt engineering  
- API integration  
- Session-based memory handling  
- Logging and error management  
- Streamlit UI development  

---

⭐ If you found this project useful, consider giving it a star.
