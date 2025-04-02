from fastapi import FastAPI, File, UploadFile
from PIL import Image
from model import ImageClassifier
import io

app = FastAPI()
classifier = ImageClassifier()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    label = classifier.predict(image)
    return {"predicted_label": label}
