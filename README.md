# 🧠 AI-Interview-Agent  
## Autonomous AI Interview Conductor

---

The **AI Interview Agent** is a full-stack application designed to conduct personalized, adaptive interviews using advanced language models. It simulates an intelligent interviewer by dynamically analyzing job descriptions, resumes, and role-specific context to generate targeted questions and provide insightful evaluations.

This POC showcases the use of lightweight OpenAI GPT-4.1 nano models integrated into a scalable, containerized architecture—ideal for real-time, cloud-based AI interview automation.

---

## 🔍 Key Features

- ✨ **Personalized Interviews** — Generates role-specific interview questions using LLMs.
- 📄 **Resume + JD Parsing** — Extracts context from candidate profiles and job descriptions.
- 🧠 **LLM-Driven Logic** — Uses **OpenAI GPT-4.1 nano** for dynamic question generation and scoring.
- 🌐 **Web Interface** — Built with a React frontend and FastAPI backend.
- 🐳 **Containerized** — Fully Dockerized for local development and production deployment.
- ☁️ **Cloud Ready** — Easily deployable on VMs (AWS EC2, GCP, Azure) with Docker support.

---

## 📦 Tech Stack

- **Frontend**: React.js  
- **Backend**: FastAPI (Python 3.9)  
- **LLM API**: OpenAI GPT-4.1 nano via custom wrapper  
- **Database**: MongoDB Atlas (for storing interview state/history)  
- **Deployment**: Docker, Docker Compose  

---

## 🧪 Use Cases

- AI-powered interview system
- Adaptive role-specific interview coaching
- Resume and JD analysis-driven question pipelines

---

## 🚀 Quick Start

Want to run this locally or on a cloud VM using Docker? [See full deployment guide ⬇️]



### 🔧 Local Setup (Using Docker Desktop)

1. **Clone the repository**  
   ```bash
   git clone https://github.com/srinivas-300/AI-Interview-Agent.git
   cd AI-Interview-Agent
   ```

2. **Configure environment variables**  
   Create a `.env` file in the root directory and fill in the following:
   ```env
   OPENAI_API_KEY=
   MONGO_USERNAME=
   MONGO_PASSWORD=
   TAVILY_API_KEY=
   EMAIL_API_KEY=
   EMAIL_SENDER=
   ADMIN_EMAIL=
   frontend_url=        # Local or EC2 IP with port (for CORS)
   REACT_APP_BACKEND_URL= # Backend IP with port
   ```

3. **MongoDB Setup**  
   Ensure MongoDB Atlas or local instance is running with the following collections:
   - `selection`
   - `interview_result`
   - `chat`

4. **Run Locally**
   ```bash
   docker-compose build --no-cache
   docker-compose up
   ```

---

### ☁️ Deploy on AWS EC2

#### 🐋 Step 1: Tag and Push Docker Images

Make sure you're logged into Docker Hub (`docker login`), then tag and push the images:

```bash
# Backend
docker tag ai-interview-agent-backend <your-dockerhub-username>/ai-interview-agent-backend:latest
docker push <your-dockerhub-username>/ai-interview-agent-backend:latest

# Frontend
docker tag ai-interview-agent-frontend <your-dockerhub-username>/ai-interview-agent-frontend:latest
docker push <your-dockerhub-username>/ai-interview-agent-frontend:latest
```

#### 💻 Step 2: Set Up EC2 VM

1. **SSH into your instance**  
   ```bash
   ssh <ec2-user>@<your-ec2-ip>
   ```

2. **Install Docker**  
   ```bash
   sudo apt update
   sudo apt install docker.io -y
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

3. **Login to Docker**  
   ```bash
   docker login
   ```

---

### 🚀 Run on EC2 (2 Methods)

#### ✅ Method 1: Using `docker-compose.prod.yml` (Recommended)

1. Copy your `.env` and `docker-compose.prod.yml` files to the EC2 instance.

2. Run:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

#### ✅ Method 2: Manual Run

```bash
# Backend
docker run -d -p 8000:8000 <your-dockerhub-username>/ai-interview-agent-backend:latest

# Frontend
docker run -d -p 3000:3000 <your-dockerhub-username>/ai-interview-agent-frontend:latest
```

---

### ⚡ Instant Test Run (via Docker Desktop)

If you're testing from any machine with Docker Desktop installed:

```bash
docker run -d -p 8000:8000 saisrinivas300/ai-interview-agent-backend:latest
docker run -d -p 3000:3000 saisrinivas300/ai-interview-agent-frontend:latest
```

## 🧠 Core Functionality

This AI Interview Agent is structured around four intelligent components that simulate a personalized, role-aware interview experience using OpenAI GPT‑4.1 nano:

---

### 🔧 Tool Agent

- Determines whether a candidate question requires external information via Tools.
- Guides the LLM using a strict YES/NO format before tool invocation.
- If a tool output is provided, the LLM integrates it into its answer; otherwise, it answers directly using internal knowledge.

---

### 📋 Interview Setup

- Analyzes job descriptions to extract core responsibilities, technical skills, soft skills, and hidden expectations.
- Evaluates the candidate's resume to assess strengths, red flags, and follow-up cues.
- Combines JD and resume insights to generate interview strategy guidelines.
- Produces 6–8 personalized questions including technical, behavioral, and analytical types tailored to the candidate and role.

---

### 🗣️ Real-Time Evaluation & Interaction

- Continuously evaluates candidate responses for soft skills such as tone, body language (inferred), communication, and inclusion awareness.
- Dynamically adapts the interview flow based on response quality, evaluation feedback, and conversation history.
- Manages intro greetings, thoughtful follow-ups, and natural transitions across questions.
- Ensures a professional, human-like interview tone throughout.

---

### 📊 Final Evaluation & Feedback

- Builds a custom scoring rubric with 5–7 evaluation dimensions aligned to the role.
- Scores the candidate across all dimensions with justifications, including an overall Goodness of Fit rating.
- Detects structural issues in interview flow (e.g., premature endings).
- Generates constructive, encouraging feedback for the candidate without disclosing rubric or scoring details.

---

This modular design enables fully automated yet highly adaptive interviews tailored to any role, making it ideal for scalable talent evaluation.


### 1. 🧭 High-Level Flow of Interview Agent
<img width="616" height="274" alt="Screenshot 2025-07-14 022127" src="https://github.com/user-attachments/assets/bf7a5b22-5202-4998-b31a-948a9b8fb735" />


### 2. 🔄 LangGraph Agent
<img width="866" height="548" alt="Screenshot 2025-07-14 022626" src="https://github.com/user-attachments/assets/94d5a385-716b-4791-be62-86ca7e1dbd09" />

### 3. 🧠 Internal Architecture of the Interview Agent

<img width="972" height="970" alt="Screenshot 2025-07-14 021953" src="https://github.com/user-attachments/assets/8e964681-951f-49fe-bc3f-2c7a3a184f68" />

### 4. ☁️ Cloud Deployment Architecture

<img width="1122" height="382" alt="Screenshot 2025-07-14 022225" src="https://github.com/user-attachments/assets/74bb4801-b04f-4753-891a-60600f744028" />





