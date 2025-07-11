from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.predict import load_model

app = FastAPI()

# ✅ Add CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

classifier = load_model()

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input: InputText):
    try:
        result = classifier(input.text)[0]
        return {
            "label": result["label"].lower(),  # Make it lowercase as per requirement
            "score": round(result["score"], 4)
        }
    except Exception as e:
         raise HTTPException(status_code=500, detail=str(e))
     
@app.get("/")
def root():
    return {"message": "Backend is up and running"}