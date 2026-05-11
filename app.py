from flask import Flask, request, jsonify
from classifier import classify_job
import pandas as pd

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()

    jobs = data.get("jobs", "")

    results = []
    for job in jobs:
        title = job.get("title", "")

        result = classify_job(title)

        results.append(result)

    return jsonify({
        "results": results
    })


@app.route("/upload-csv", methods=["POST"])
def upload_csv():

    if "file" not in request.files:
        return jsonify({
            "error": "No file uploaded"
        }), 400

    file = request.files["file"]

    try:
        df = pd.read_csv(file)

        results = []

        for _, row in df.iterrows():

            title = str(row["title"])

            result = classify_job(title)

            results.append(result)

        return jsonify({
            "total_jobs": len(results),
            "results": results
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)