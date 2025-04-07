# 503N Assignment 2.2: 🖼️ Image Recognition API with FastAPI + Hugging Face ViT

This project uses `google/vit-base-patch16-224` from Hugging Face to create an image classification API using **FastAPI**. You can send an image file to the API and receive the top predicted labels.

---

## 🚀 Features

- Accepts an image file via POST request
- Returns the **top 3 predicted class labels**
- Powered by a pre-trained Vision Transformer (ViT) model from Hugging Face
- Clean API design using FastAPI
- GitHub-friendly structure for collaboration

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mhmdsh24/assignment-2.2.git
cd assignment-2.2
```

### 2. Create a Virtual Environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

---

## 📡 API Endpoint

### `POST /predict`

#### Request:

- Content-Type: `multipart/form-data`
- Form-data key: `file`
- Value: Image file (JPG, PNG, etc.)

#### Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -F "file=@path_to_your_image.jpg"
```

#### Example Response:

```json
{
  "predictions": [
    {"label": "tabby cat", "score": 0.8376},
    {"label": "tiger cat", "score": 0.121},
    {"label": "Egyptian cat", "score": 0.041}
  ]
}
```

---

## 🧪 Testing with Postman

1. Open Postman and create a **POST** request to:
   ```
   http://127.0.0.1:8000/predict
   ```

2. Go to the **Body** tab → Select **form-data**

3. Add a new field:
   - **Key**: `file`
   - **Type**: `File`
   - **Value**: Choose an image from your device

4. Click **Send**. You will get a list of top predictions with confidence scores.

---

## 🔄 Folder Structure

```
assignment-2.2/
├── .gitignore             # gitignore file
├── imagefeature.py        # image feature endpoint
├── sentimentfeature.py    # sentiment analysis endpoint
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---



## 📌 Model Info

- Model: `google/vit-base-patch16-224`
- Dataset: Trained on ImageNet-1k (1,000 classes)
- Labels: Common everyday objects, animals, tools, foods, and more
