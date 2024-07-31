import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Upload predictions data
predictions_pd = pd.read_pickle("predictions.pkl")


@app.route("/anomalies", methods=["GET"])
def get_anomalies():
    anomalies = predictions_pd[predictions_pd["prediction"] == 1]  # Cluster 1 defined as anomaly
    return jsonify(anomalies.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)
