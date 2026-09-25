from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    prediction = model.predict([[
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]])

    return jsonify({
        "prediction": int(prediction[0])
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)