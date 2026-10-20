from pathlib import Path
import json
from functools import lru_cache
import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

APP_DIR = Path(__file__).resolve().parent
app = FastAPI(title="Antispam ML API", version="1.0.0")

class EmailRequest(BaseModel):
    text: str = Field(min_length=1, max_length=100000)

class BatchRequest(BaseModel):
    texts: list[str] = Field(min_length=1, max_length=100)

@lru_cache(maxsize=1)
def load_artifacts():
    # Для инференса используется только сохранённая в проекте модель.
    model = joblib.load(APP_DIR / "model.joblib")
    metadata = json.loads((APP_DIR / "metadata.json").read_text(encoding="utf-8"))
    return model, metadata

@app.get("/health")
def health():
    model, meta = load_artifacts()
    return {"status":"ok", "model":meta["best_model"]}

@app.post("/predict")
def predict(request: EmailRequest):
    model, meta = load_artifacts()
    p = float(model.predict_proba([request.text])[0,1])
    label = "spam" if p >= float(meta["spam_threshold"]) else "ham"
    return {"label":label, "spam_probability":round(p,6),
            "threshold":meta["spam_threshold"]}

@app.post("/predict/batch")
def predict_batch(request: BatchRequest):
    model, meta = load_artifacts()
    p_list = model.predict_proba(request.texts)[:,1]
    threshold = float(meta["spam_threshold"])
    return {"results":[{"label":"spam" if p>=threshold else "ham",
                         "spam_probability":round(float(p),6)} for p in p_list]}
