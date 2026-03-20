from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('used_car_price_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[
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