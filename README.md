# 🧠 AI-Interview-Agent  
## Autonomous AI Interview Conductor

---

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
