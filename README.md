# LLM Chat System – DT1 Assignment

## 1. Project Overview

This project implements a simple chat system powered by a Large Language Model (LLM).  
It is built for the DT1 course and shows how to connect:

- a **Streamlit frontend**
- a **Flask backend API**
- a remote LLM provider (**OpenRouter**)
- all running together on a **Google Cloud VM** using **Docker Compose**.

The user types a message in the web interface, the backend sends it to OpenRouter (DeepSeek model), and the reply is shown back in the browser.

---

## 2. System Architecture

High-level architecture:

- **Streamlit frontend (Docker container)**
  - Runs on port **8501**
  - Sends HTTP requests to the backend

- **Flask backend API (Docker container)**
  - Runs on port **5001**
  - Exposes `/chat` and `/ping` routes
  - Calls the OpenRouter API with the user’s input and `model_id`

- **OpenRouter (LLM provider)**
  - Hosts the DeepSeek Chat model
  - Returns the model’s response to the backend

Text diagram:

 ┌────────────────────────────────┐         ┌─────────────────────────────┐
 │        Streamlit Frontend      │  HTTP    │         Flask Backend       │
 │  (User types a message)        ├────────► │  /chat endpoint             │
 │  Runs on port :8501            │          │  Calls OpenRouter API       │
 └────────────────────────────────┘          └───────────────┬────────────┘
                                                             │
                                                             ▼
                                                ┌─────────────────────────┐
                                                │     OpenRouter API      │
                                                │ (DeepSeek Chat Model)   │
                                                └─────────────────────────┘

---

# 🔧 **3. Technologies Used**

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | Python Flask |
| LLM Provider | OpenRouter (DeepSeek) |
| Deployment | Google Cloud VM |
| Containers | Docker + Docker Compose |
| Networking | GCP Firewall rules |

---

# 🗂 **4. Project Structure**

llm-app/
 ├── api.py                 # Flask backend API
 ├── frontend.py            # Streamlit frontend UI
 ├── docker-compose.yml     # Docker environment (frontend + backend)
 ├── README.md              # This documentation
---

# **5. How to Run the Project Locally**

### 1️⃣ Clone the repository
```bash
git clone <your repository link>
cd llm-app
export OPENROUTER_API_KEY="your_key_here"
docker-compose up --build
http://localhost:8501
---

# **6. Deployment on Google Cloud VM**

This project was deployed on:

- **VM Name:** dt1-vm1
- **External IP:** 34.155.85.52
- **Ports Used:**
  - `8501` → Streamlit frontend
  - `5001` → Flask backend

### Steps taken:

1. Installed Docker + Docker Compose  
2. Cloned the project into the VM  
3. Added environment variable:
```bash
export OPENROUTER_API_KEY="your_key"
docker-compose up -d --build
Allowed traffic in GCP Firewall:

8501 (Streamlit)

5001 (Flask)

Student IP: 91.168.189.252/32

Professor IP range: 147.87.0.0/16

Final Notes

Frontend successfully communicates with backend.

Backend successfully calls OpenRouter DeepSeek Chat.

The system is fully deployed and functional.

Meets DT1 assignment requirements.


Credits

Student: Maja Tomovic

Course: DT1 – Enabling Technologies

Instructor: Singh Siddhartha
