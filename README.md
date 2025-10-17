# DT1 Assignment - LLM Text Completion System

## Project Overview
This project implements a full-stack LLM (Large Language Model) text completion system with a Streamlit frontend and Flask backend, deployed on Google Cloud Platform using Docker containers.

## System Architecture

### Components
1. **Frontend**: Streamlit web application (Port 8501)
2. **Backend**: Flask API server (Port 8000) 
3. **External Service**: OpenRouter API for LLM inference
4. **Infrastructure**: Google Cloud Platform VM with Docker

### Architecture Diagram

User 
  │
  ↓ HTTP Requests
[Streamlit Frontend:8501]
  │
  ↓ API Calls  
[Flask Backend:8000]
  │
  ↓ OpenRouter API
[LLM Models]
  │
  ↓ Responses
[Streamlit Frontend]

## Prerequisites
- Docker & Docker Compose
- Google Cloud Platform account
- OpenRouter API account
- Python 3.10+

## Setup Instructions

### 1. Clone Repository
```bash
git clone <your-repository-url>
cd dt1-25

### 2. Environment Configuration
Create `.env` file:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here

## Account Information

- **GitHub**: majat4
- **Docker Hub**: majat4

## Contributors
- Maja Tomovic - Primary developer
- Sid Singh (sid027) - Added as contributor for evaluation