# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 01:16:03 2021

@author: sagar kumar
"""

from flask import Flask, request, jsonify
import numpy as np
import joblib
import json

pkl_file = "iris-trained-model.pkl"

app = Flask(__name__)

@app.route('/predict/', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)


if __name__ == '__main__':
    model = joblib.load(pkl_file)
    app.run(host='0.0.0.0', port = 5000)