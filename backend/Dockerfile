FROM python:3.9

WORKDIR /app

# ✅ Copy requirements.txt from root (go up one level from Dockerfile)
COPY ../requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy all backend source code (relative to build context)
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
