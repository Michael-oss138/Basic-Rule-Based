from flask import Flask, request, jsonify
from classifier import classify_job

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    title = data.get("title", "")

    result = classify_job(title)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)