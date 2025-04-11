
# 💧 Water Quality Prediction API

This project is a RESTful API built using Django REST Framework. It uses a machine learning model to predict the safety level of water based on various chemical parameters. The prediction output includes a safety **score** and a corresponding **message** explaining the water quality.

----------

## 📁 Project Structure

```
waterpredictor/
├── api/
│   ├── views.py
│   ├── serializers.py
│   └── Saved-models/
│       ├── final_ensemble_model.pkl
│       ├── scaler.pkl
│       └── feature_columns.pkl
├── manage.py
└── waterpredictor/
    └── settings.py

```

----------

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/water-predictor.git
cd water-predictor

```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

```

### 3. Install required packages

```bash
pip install -r requirements.txt

```

> **Note:** Make sure `dill`, `joblib`, `pandas`, `django`, and `djangorestframework` are included in your `requirements.txt`.

### 4. Apply migrations

```bash
python manage.py migrate

```

### 5. Run the development server

```bash
python manage.py runserver

```

----------

## 🚀 API Endpoint

### **POST** `/api/predict/`

#### Request Body (JSON)

```json
{
  "ph": 7.0,
  "Hardness": 150.0,
  "Solids": 15000.0,
  "Chloramines": 7.5,
  "Sulfate": 300.0,
  "Conductivity": 350.0,
  "Organic_carbon": 10.0,
  "Trihalomethanes": 60.0,
  "Turbidity": 3.0
}

```

#### Response

```json
{
  "score": 0.85,
  "message": "💧 Very safe. Water quality is excellent."
}

```

----------

## 🧠 How It Works

-   Loads a pre-trained ML model (`final_ensemble_model.pkl`) and scaler at server startup.
    
-   Accepts input features via POST request.
    
-   Scales the data and predicts the safety score.
    
-   Returns a meaningful interpretation of water quality based on the score.
    

----------

## 📝 Model Files

Ensure the following files exist inside the `Saved-models/` folder:

-   `final_ensemble_model.pkl` – Trained ML model (using `dill`)
    
-   `scaler.pkl` – Fitted feature scaler
    
-   `feature_columns.pkl` – List of expected feature column names
    

----------

## 🧪 Testing with Postman

1.  Set the method to `POST`
    
2.  URL: `http://127.0.0.1:8000/api/predict/`
    
3.  Headers:
    
    -   `Content-Type`: `application/json`
        
4.  Body: raw JSON (example above)
    

----------

## 🛠 Built With

-   Python 3.x
    
-   Django
    
-   Django REST Framework
    
-   Pandas
    
-   Dill & Joblib
    

----------

## 📌 Author

Created with 💙 by Ronnie Allen  
Feel free to contribute, fork, or reach out if you'd like to improve this!

----------
