from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import json

app = Flask(__name__)

with open('used_car_price_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

with open('brand_model_map.json', 'r') as f:
    brand_model_map = json.load(f)

@app.route('/')
def home():
    brands = sorted(list(brand_model_map.keys()))
    return render_template('index.html',
                           brands=brands,
                           brand_model_map=brand_model_map)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    brand_encoded = encoders['brand'].transform([data['brand']])[0]
    model_encoded = encoders['model'].transform([data['car_model']])[0]
    features = np.array([[
        brand_encoded,
        model_encoded,
        data['age'],
        data['km_driven'],
        data['transmission'],
        data['owner'],
        data['fuel_type']
    ]])
    prediction = model.predict(features)[0]
    return jsonify({'predicted_price': round(float(prediction), 2)})

if __name__ == '__main__':
    app.run(debug=True)
