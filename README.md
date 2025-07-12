# Sentiment Analyzer

A full-stack sentiment classification system with Hugging Face Transformers on the backend and a modern React + Vite frontend. The app allows users to enter text and receive real-time sentiment predictions via an API.

---

### 📁 Project Structure

```text
sentiment-analyzer/
├── backend/
│   ├── __pycache__/
│   ├── app/
│   │   └── predict.py              # Inference logic
│   ├── model/                      # Saved model files
│   ├── Dockerfile                  # Backend Dockerfile
│   ├── main.py                     # FastAPI application
│   └── finetune/
│       └── finetune.py             # Finetuning scripts
│
├── frontend/
│   ├── node_modules/
│   ├── src/
│   │   ├── App.jsx                 # Main React component
│   │   └── main.jsx                # React entry point
│   ├── index.css                   # Stylesheet
│   ├── index.html                  # HTML template
│   ├── package.json                # Frontend deps
│   ├── package-lock.json
│   ├── vite.config.mjs            # Vite config
│   └── Dockerfile                 # Frontend Dockerfile
│
├── .gitignore
├── .dockerignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```
---

## 🛠️ Setup & Run Instructions

### Fine-tune the Model **(First Run Only)**
Before launching the backend, make sure to fine-tune and save the model using:

```bash
cd backend/finetune
python finetune.py
```
This will generate the model and tokenizer files under backend/model/.

### 🔁 One-Step Setup Using Docker

```docker-compose up --build```

Once running:

* 💻 Frontend: [http://localhost:3000](http://localhost:3000)
* ⚙️ Backend (API + docs): [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ⚠️ Manual Setup

### Fine-tune the Model (First Run Only)
Before launching the backend, make sure to fine-tune and save the model using:

```bash
cd backend/finetune
python finetune.py
```
This will generate the model and tokenizer files under backend/model/.

### 🧹 Backend (FastAPI + Transformers)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r ../requirements.txt
uvicorn main:app --reload
```

### 🎨 Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

---

## 🧠 Design Decisions

* **Model**: Hugging Face Transformers with preloaded sentiment classifier.
* **Backend**: FastAPI – fast async API with automatic docs.
* **Frontend**: React with Vite – minimal, fast, and easily styled.
* **Containerization**: Dockerized with clean separation of frontend and backend for modular deployment.
* **Finetuning**: Modular script provided (`finetune.py`) for optional supervised fine-tuning.

---

## ⏱ CPU vs. GPU Fine-tune Benchmarks

| Device                  | Dataset Size | Epochs | Avg. Time    |
| ----------------------- | ------------ | ------ | ------------ |
| CPU (i5 10th Gen)       | 500 samples  | 3      | \~8 minutes  |
| GPU (Tesla T4 Colab)    | 500 samples  | 3      | \~40 seconds |

---

## 🔀 API Docs

Available at: [http://localhost:8000/docs](http://localhost:8000/docs)

### POST `/predict`

**Request JSON:**

```json
{
  "text": "I love this project!"
}
```
**Response JSON:**

```json
{
  "label": "POSITIVE",
  "score": 0.9984
}
```

---

## 📹 Project Demo

🎥 [Watch the 3-min Demo Video](https://www.youtube.com/watch?v=XYR_QuZr0Dc)

---

### 👨‍💻 Author

**Rusheil Singh Baath**  
B.Tech in Computer Science Engineering  
Specialization: Artificial Intelligence & Data Science

---
