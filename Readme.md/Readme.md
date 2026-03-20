# Used Car Price Predictor 🚗

An AI-powered web application that predicts used car prices in India.

## Live Demo
🌐 [Click here to view the app]https://used-car-price-predictor-e7km.onrender.com/

## Features
- Predict used car prices instantly
- 38 car brands supported
- 9500+ cars trained
- Clean UI

## Tech Stack
- Python
- Flask
- Scikit-learn (Random Forest)
- HTML / CSS / JavaScript
- Deployed on Render

## Project Structure
```
used-car-predictor/
├── app.py
├── requirements.txt
├── brand_model_map.json
├── used_car_price_prediction_model.pkl
├── label_encoders.pkl
└── templates/
    └── index.html

## How to Run Locally
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Open `http://127.0.0.1:5000`

## Model Details
- Algorithm: Random Forest Regressor
- Features: Brand, Model, Age, KM Driven, Transmission, Owner, Fuel Type
- Dataset: Used Car Dataset (9500+ records)