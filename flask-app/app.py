from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({"status": "ok", "message": "Flask app is running!"})

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask!", "version": "1.0.0"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
