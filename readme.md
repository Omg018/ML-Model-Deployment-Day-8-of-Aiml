# 🚀 FastAPI Machine Learning Deployment

This project demonstrates how to deploy a **Machine Learning model** (Cat vs Dog classifier) using **FastAPI**, containerize it with **Docker**, and make it production-ready.

## 📌 Overview
- Built a REST API for ML model inference using FastAPI
- Integrated a pre-trained **Cat vs Dog CNN model** (from [previous project](https://github.com/Omg018/Cat-Vs-Dog-Classifier-Using-TensorFlow-Keras ))
- Added advanced features:
  - Pydantic request validation
  - Async support
  - Error handling
- Containerized with Docker for easy deployment

## 🔧 Prerequisites
- Python 3.8+
- Docker (for containerization)
- ML model file (`cat_dog_classifier.keras`)

## 🛠️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Om018/ML-Model-Deployment-Day-8-of-Aiml
cd fastapi-ml-deployment
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your ML model
Place your trained model (from the previous Cat vs Dog project) in the `/` directory.

## 🚦 Running the API

### Development mode
```bash
uvicorn main:app --reload
```

### Production mode (with Docker)
```bash
docker build -t fastapi-ml .
docker run -p 8000:8000 fastapi-ml
```

## 🌐 API Endpoints

| Endpoint  | Method | Description |
|-----------|--------|-------------|
| `/`       | GET    | Health check |
| `/predict` | POST  | Make predictions (accepts image file) |
| `/docs`   | GET    | Interactive API documentation |

## 🐳 Docker Deployment
The included **Dockerfile** lets you deploy this anywhere:
- **AWS ECS/EC2**
- **Google Cloud Run**
- **Azure Container Instances**

## 🔗 Previous Projects
- (from [Link](https://github.com/Omg018/Cat-Vs-Dog-Classifier-Using-TensorFlow-Keras))

## 📝 Notes
- This implementation uses the same Cat vs Dog CNN model from our previous training project.
- For best performance, ensure your input images match the training dimensions (typically **224x224** for most CNN models).

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.
