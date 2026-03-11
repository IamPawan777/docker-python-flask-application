# 🐍 Flask App

A simple Python Flask application, Docker-ready and GitHub-ready.

---

## 📁 Project Structure 

```
flask-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker image definition
├── docker-compose.yml  # Docker Compose config
├── .gitignore
└── templates/
    └── index.html      # Home page template
```

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python app.py
```
Visit: http://localhost:5000

---

## 🐳 Docker Commands

### Build the image
```bash
docker build -t flask-app .
```

### Run the container
```bash
docker run -p 5000:5000 flask-app
```

### Run with Docker Compose
```bash
docker-compose up --build
```

### Stop containers
```bash
docker-compose down
```

### View running containers
```bash
docker ps
```

### View logs
```bash
docker logs <container_id>
```

---

## 📦 Push to GitHub

```bash
# Initialize repo
git init
git add .
git commit -m "Initial commit: Flask app"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/flask-app.git
git branch -M main
git push -u origin main
```

---

## 🌐 API Endpoints

| Method | Endpoint     | Description        |
|--------|--------------|--------------------|
| GET    | `/`          | Home page          |
| GET    | `/health`    | Health check       |
| GET    | `/api/hello` | Sample API route   |
