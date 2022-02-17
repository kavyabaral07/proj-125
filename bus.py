from flask import Flask, jsonify, request
from classifier import  get_prediction

app = Flask(_name_)

@app.route("/predict-alphabet", methods=["POST"])
def predict_data():
  image = request.files.get("alphabet")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200

if _name_ == "_main_":
  app.run(debug=True)
  © 2022 GitHub, Inc.
