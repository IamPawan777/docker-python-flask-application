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

## 🐳 Step to Containerize the project

### clone in AWS Linux
```bash
    git clone <repository-link>
```
### change directory here 2 times
```bash
    cd <project-name>        -> check: $ ls -l
    cd <project-name>        -> until 'Dockerfile' not showing
```

### Build the image
```bash
docker build -t flask-app .
```

### Run the container
```bash
docker run -d -p 8080:5000 --name python-checker flask-app
```

### View running containers
```bash
docker ps
```

### View logs
```bash
docker logs <container_id>
```

### search on browser
```
    <EC2-public-ip>:<host-ip>
Eg: 44.192.69.78:8080/
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
