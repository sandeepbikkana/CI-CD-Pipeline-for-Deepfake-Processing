from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Deepfake Detection API")


class AudioRequest(BaseModel):
    audio_url: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/detect")
def detect(req: AudioRequest):
    # Placeholder for ML inference
    score = 0.87
    return {"deepfake_probability": score, "verdict": "fake" if score > 0.5 else "real"}
