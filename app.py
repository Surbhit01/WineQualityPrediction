from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from WineQualityPrediction.pipeline.prediction import PredictionPipeline

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@app.route("/train", methods=["GET"])
def training():
    os.system("python main.py")
    return "Training Successful"


@app.route("/predict", methods=["POST", "GET"])
def prediction():
    if request.method == "POST":
        try:
            fixed_acidity = float(request.form["fixed_acidity"])
            volatile_acidity = float(request.form["volatile_acidity"])
            citric_acid = float(request.form["citric_acid"])
            residual_sugar = float(request.form["residual_sugar"])
            chlorides = float(request.form["chlorides"])
            free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
            total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
            density = float(request.form["density"])
            pH = float(request.form["pH"])
            sulphates = float(request.form["sulphates"])
            alcohol = float(request.form["alcohol"])

            data = [
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol,
            ]

            data = np.array(data).reshape(1, 11)
            print(data)
            predictionPipeline = PredictionPipeline()
            print("Predicting values..")
            predict = predictionPipeline.predict(data)
            print(predict)
            return render_template("results.html", prediction=str(round(predict[0], 2)))

        except Exception as e:
            print("Exception in app.py: ", e)
            return "Encountered an error. Please check logs"

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    # app.run(host="0.0.0.0", port=8080)
