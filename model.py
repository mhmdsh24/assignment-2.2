from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import torch
import requests
import io

class ImageClassifier:
    def __init__(self, model_name="google/vit-base-patch16-224"):
        self.model = AutoModelForImageClassification.from_pretrained(model_name)
        self.feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
        self.labels = self.model.config.id2label

    def predict(self, image: Image.Image):
        inputs = self.feature_extractor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class = logits.argmax(-1).item()
        return self.labels[predicted_class]
