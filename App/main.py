from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data (first run only, harmless later)
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# ---------- Text cleaning (same as training) ----------
def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www.\S+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in stop_words and len(t) > 2]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)

# ---------- Load model ----------
MODEL_PATH = "App/sentiment_model.pkl"
model = joblib.load(MODEL_PATH)

# ---------- FastAPI app ----------
app = FastAPI(
    title="E-commerce Review Sentiment API",
    description="Predict sentiment (positive/negative) for Flipkart reviews.",
    version="1.0.0"
)

# ---------- Request schema ----------
class ReviewRequest(BaseModel):
    review_text: str

# ---------- Health check ----------
@app.get("/")
def root():
    return {"message": "Sentiment API is running. Use POST /predict with review_text."}

# ---------- Prediction endpoint ----------
@app.post("/predict")
def predict_sentiment(payload: ReviewRequest):
    raw_text = payload.review_text
    cleaned = clean_text(raw_text)

    # model expects a list of texts
    pred = model.predict([cleaned])[0]

    return {
        "review_text": raw_text,
        "clean_text": cleaned,
        "predicted_sentiment": pred
    }
