# 💼 Smart IT Career Assistant (Gemini API Powered)

A production-ready AI-powered Career Guidance Chatbot built using **Google Gemini API** and **Streamlit**.

This application provides structured, professional IT career guidance including roadmaps, skills, certifications, salary insights, and project suggestions.

---

## 🚀 Project Overview

Smart IT Career Assistant is a domain-specific Generative AI chatbot designed to simulate a real-world production architecture.

It includes:

- Secure Gemini API integration
- Structured prompt engineering
- Multi-turn conversation memory
- Sliding window context trimming
- Token-aware response handling
- Error handling with logging
- Modular clean architecture
- Professional Streamlit UI

---

## 🧠 Problem Statement

Build a production-grade domain-specific GenAI chatbot that:

- Integrates Google Gemini API
- Uses environment-based API key management
- Implements structured system prompts
- Supports contextual multi-turn conversations
- Follows clean backend architecture
- Handles API errors and edge cases
- Provides structured professional responses

---

## 🏗️ Project Architecture

The system follows clean modular architecture:

User  
→ Streamlit UI  
→ Memory Manager  
→ Gemini Service  
→ System Prompt  
→ Google Gemini API  
→ Response Rendering  

---

## 📂 Project Structure

```
genai-career-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
│   └── settings.py
│
├── memory/
│   └── session_memory.py
│
├── prompts/
│   └── system_prompt.py
│
├── services/
│   └── gemini_service.py
│
└── utils/
    └── logger.py
```

---

## 📌 Module Responsibilities

### app.py
- Streamlit UI rendering
- Chat interface
- Sidebar configuration
- Conversation display

### services/gemini_service.py
- Gemini API configuration
- Chat session handling
- Sliding window context trimming
- Error handling (quota, invalid key, model issues)

### prompts/system_prompt.py
- Structured system instruction
- Professional response formatting rules

### memory/session_memory.py
- Multi-turn conversation memory
- Session-based state management
- Automatic history trimming

### config/settings.py
- Environment variable loading
- Secure API key configuration

### utils/logger.py
- API logging
- Error tracking

---

## 🛠 Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv
- Logging module

---

## 🧩 Key Features

✔ Structured professional career guidance  
✔ Multi-turn contextual conversation  
✔ Sliding window memory control  
✔ Token overflow prevention  
✔ Environment-based API configuration  
✔ Robust error handling  
✔ Clean modular architecture  
✔ Production-ready design  

---

## 📊 Response Structure

The assistant provides structured answers in the following format:

1. Overview  
2. Required Skills  
3. Learning Roadmap  
4. Projects  
5. Certifications  
6. Career Path  
7. Salary Insights  
8. Final Advice  

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Create `.env` File

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-2.5-flash
```

### Step 3: Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## ⚠️ Error Handling Implemented

The system handles:

- API quota exceeded (429)
- Invalid API key
- Invalid role formatting
- Model not found
- Generic API errors

---

## 🎯 Production-Grade Practices Used

- Environment variable configuration
- Modular folder structure
- Context trimming for token control
- Structured prompt engineering
- Clean separation of concerns
- Professional UI rendering
- Defensive programming

---

## 📈 Use Cases

This project is suitable for:

- AI / ML Internship Submissions
- Generative AI Portfolio Projects
- Backend Architecture Demonstration
- Streamlit Production App Example
- Gemini API Integration Showcase

---

## 📌 Conclusion

Smart IT Career Assistant demonstrates the development of a structured, production-style Generative AI application using Google Gemini API.

It reflects strong understanding of:

- LLM integration
- Prompt engineering
- Context management
- Clean architecture
- Production-level error handling

---

⭐ If you found this project useful, feel free to star the repository.
