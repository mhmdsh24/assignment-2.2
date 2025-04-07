# Sentiment Analysis & Image Classification API

This project provides an API for sentiment analysis and image classification using FastAPI and Hugging Face models. It includes endpoints for analyzing text sentiment and classifying images.

---

## 🚀 Features

- **Sentiment Analysis**: Analyze the sentiment of a given text using a pre-trained DistilBERT model.
- **Image Classification**: Classify images using a Vision Transformer (ViT) model.
- **FastAPI**: Clean and efficient API design.
- **Pre-trained Models**: Utilizes models from Hugging Face for high accuracy.

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

## 📡 API Endpoints

### `POST /sentiment`

- **Description**: Analyze the sentiment of a given text.
- **Request**:
  - Content-Type: `application/json`
  - Body: `{"text": "Your text here"}`
- **Response**: Sentiment analysis result.

#### Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/sentiment" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
```

### `POST /image`

- **Description**: Classify an uploaded image.
- **Request**:
  - Content-Type: `multipart/form-data`
  - Form-data key: `file`
  - Value: Image file (JPG, PNG, etc.)
- **Response**: Predicted label of the image.

#### Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/image" \
  -F "file=@path_to_your_image.jpg"
```

---

## 🧪 Testing with Postman

1. **Sentiment Analysis**:
   - Create a **POST** request to `http://127.0.0.1:8000/sentiment`.
   - Set the body to raw JSON: `{"text": "Your text here"}`.
   - Send the request to receive the sentiment analysis.

2. **Image Classification**:
   - Create a **POST** request to `http://127.0.0.1:8000/image`.
   - Go to the **Body** tab → Select **form-data**.
   - Add a new field:
     - **Key**: `file`
     - **Type**: `File`
     - **Value**: Choose an image from your device.
   - Send the request to receive the image classification.

---

## 🧪 Testing with FastAPI Interactive Docs

FastAPI provides an interactive API documentation interface that you can use to test the endpoints.

1. **Access the Documentation**:
   - Start the FastAPI server by running:
     ```bash
     uvicorn main:app --reload
     ```
   - Open your web browser and go to `http://127.0.0.1:8000/docs`.

2. **Using the Interactive Docs**:
   - You will see a list of available endpoints.
   - Click on an endpoint to expand it and see the details.
   - You can test the endpoints directly from the browser by filling in the required fields and clicking the "Execute" button.
   - The response will be displayed below the request parameters.

This interface is a convenient way to explore and test the API without needing external tools like Postman or curl.

---

## �� Folder Structure

```