# 🚀 Smart IT Career Assistant  
### Production-Ready GenAI Chatbot using Google Gemini API  

This repository contains a **Production-Ready, Domain-Specific AI Career Assistant Chatbot** built using **Google Gemini API** and **Streamlit**, following clean architecture and real-world AI engineering practices.

The system is deployed on **AWS EC2** and simulates a scalable, production-grade Generative AI application.

---

## 🧩 Project Objective

Design and deploy a production-ready GenAI chatbot that:

- Integrates Google Gemini API securely  
- Implements structured prompt engineering  
- Supports multi-turn contextual conversations  
- Follows modular backend architecture  
- Includes logging and structured error handling  
- Uses environment-based configuration  
- Deploys on AWS EC2 (publicly accessible)

---

## 🎯 Domain: IT Career Strategy Assistant

The chatbot provides structured guidance on:

- Data Science career roadmaps  
- AI / ML learning paths  
- Software Development guidance  
- Cloud & DevOps career planning  
- Interview preparation strategies  
- Resume building advice  
- Salary insights and certifications  

---

## 🏗 System Architecture


User
↓
Streamlit UI Layer
↓
Backend Service Layer
↓
Prompt Engineering Module
↓
Google Gemini API
↓
Response Processing
↓
UI Rendering


The architecture follows separation of concerns and modular design principles.

---

## 📁 Project Structure


genai-career-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
│ └── settings.py
│
├── services/
│ └── gemini_service.py
│
├── prompts/
│ └── system_prompt.py
│
├── memory/
│ └── session_memory.py
│
├── utils/
│ └── logger.py
│
└── logs/


### Module Responsibilities

- **app.py** → UI rendering and chat interaction  
- **gemini_service.py** → API integration and response handling  
- **system_prompt.py** → Structured prompt engineering  
- **session_memory.py** → Multi-turn conversation memory  
- **logger.py** → Logging API calls and errors  
- **settings.py** → Secure configuration management  

---

## 🔐 Security Best Practices

- API keys stored in environment variables  
- `.env` excluded using `.gitignore`  
- No hardcoded credentials  
- Structured exception handling  
- API logic separated from UI  

---

## 🧠 Key Features

- Secure Gemini API integration  
- Multi-turn contextual memory  
- Structured system prompts  
- Role-based domain constraints  
- Token-aware prompt management  
- Logging and fallback handling  
- Clean modular architecture  
- Professional Streamlit UI  
- AWS EC2 deployment  

---

## 💻 Local Setup Instructions

### Step 1 – Clone Repository

```bash
git clone <your-repo-url>
cd genai-career-chatbot
Step 2 – Install Dependencies
pip install -r requirements.txt
Step 3 – Create .env File

Create a .env file in the root directory:

GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-1.5-flash

⚠ Never commit this file to GitHub.

Step 4 – Run Application
streamlit run app.py

Open in browser:

http://localhost:8501
☁ AWS EC2 Deployment

The application is deployed on an Ubuntu-based AWS EC2 instance.

Deployment Configuration

EC2 Instance (Ubuntu)

Port 8501 enabled in Security Group

Environment variables configured securely

Streamlit running on 0.0.0.0

Public IP accessibility enabled

Live Deployment
http://<your-public-ip>:8501
🚀 Scalability Considerations

Modular architecture for extensibility

Separation of UI and backend logic

Token-aware prompt trimming

Logging for monitoring and debugging

Cloud deployment ready

Future Improvements

HTTPS with Nginx

Docker containerization

Persistent database-backed memory

CI/CD pipeline integration

Authentication layer

🛠 Technologies Used

Python

Streamlit

Google Gemini API

AWS EC2

python-dotenv

Logging module

👨‍💻 Author

Lokesh Naidu
Advanced Generative AI Internship
Innomatics Research Labs

🏁 Final Summary

This project demonstrates the design and deployment of a production-grade domain-specific GenAI chatbot system using Google Gemini API.

It implements modular backend architecture, structured prompt engineering, multi-turn memory handling, token optimization, secure configuration management, and AWS cloud deployment aligned with real-world AI engineering standards.
