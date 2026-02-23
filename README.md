# 💼 Smart IT Career Assistant
A Production-Ready AI Career Guidance Chatbot using Google Gemini API and Streamlit

---

## 🚀 Project Overview

Smart IT Career Assistant is a domain-specific AI chatbot designed to provide structured and professional IT career guidance.

The application integrates Google Gemini API with a clean modular architecture and supports multi-turn contextual conversations using Streamlit session state.

It delivers detailed, structured responses including:

- Career Overview
- Required Skills
- Learning Roadmap
- Suggested Projects
- Certifications
- Career Path
- Salary Insights
- Final Advice

---

## 🧠 Objective

To build a production-style Generative AI chatbot that:

- Securely integrates Google Gemini API
- Uses environment-based configuration (.env)
- Implements structured prompt engineering
- Supports multi-turn chat memory
- Controls token overflow using sliding window trimming
- Includes robust error handling
- Logs system errors for debugging

---

## 🏗️ System Architecture

User  
→ Streamlit UI (`app.py`)  
→ Session Memory Manager (`session_memory.py`)  
→ Gemini Service Layer (`gemini_service.py`)  
→ Structured System Prompt (`system_prompt.py`)  
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

## 📌 Implementation Details

### 1️⃣ Streamlit UI (app.py)

- Wide layout configuration
- Sidebar with supported topics
- Chat-style message display
- Clear chat functionality
- Real-time spinner during response generation
- Session-based memory initialization

---

### 2️⃣ Gemini Service Layer (services/gemini_service.py)

- Configures API using environment variable
- Initializes `GenerativeModel`
- Uses structured system instruction
- Sliding window context trimming (`MAX_CONTEXT_MESSAGES = 4`)
- Converts Streamlit chat format to Gemini format
- Handles structured API errors:
  - Quota exceeded (429)
  - Invalid API key
  - Model not found
  - Role formatting errors
- Logs all runtime errors

---

### 3️⃣ Prompt Engineering (prompts/system_prompt.py)

Defines strict professional response structure:

1. Overview  
2. Required Skills  
3. Learning Roadmap  
4. Projects  
5. Certifications  
6. Career Path  
7. Salary Insights  
8. Final Advice  

Ensures consistent, detailed, and structured responses.

---

### 4️⃣ Conversation Memory (memory/session_memory.py)

- Uses Streamlit session state
- Maintains multi-turn chat history
- Limits stored messages (`MAX_HISTORY = 10`)
- Automatically trims older messages
- Prevents token overflow

---

### 5️⃣ Configuration (config/settings.py)

- Loads environment variables using python-dotenv
- Reads:
  - `GEMINI_API_KEY`
  - `MODEL_NAME`
- Default model: `gemini-2.5-flash`

---

### 6️⃣ Logging (utils/logger.py)

- Creates `logs/` folder automatically
- Writes logs to `logs/app.log`
- Logs all Gemini API errors
- Helps debugging and monitoring

---

## 🛠 Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv
- Logging module

---

## ✨ Key Features

✔ Structured professional career guidance  
✔ Multi-turn contextual conversation  
✔ Sliding window memory trimming  
✔ Token overflow protection  
✔ Environment-based configuration  
✔ Defensive error handling  
✔ Runtime logging  
✔ Clean modular architecture  

---

## ▶️ How to Run the Application

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 2: Create `.env` File

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-2.5-flash
```

---

### Step 3: Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🎯 Production Practices Demonstrated

- Environment-based API management
- Modular folder structure
- Structured system prompt design
- Sliding window context control
- Multi-turn session management
- Centralized error logging
- Clean separation of concerns

---

## 📌 Conclusion

Smart IT Career Assistant demonstrates a structured, production-oriented LLM integration using Google Gemini API.

The project highlights understanding of:

- LLM integration
- Prompt engineering
- Context management
- Streamlit-based UI design
- Error handling & logging
- Clean backend architecture
---

⭐ If you found this project useful, consider giving it a star.
