# bot.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/ping")
def ping():
    """Health check endpoint"""
    return jsonify({
        "status": "ok",
        "message": "pong",
        "bot_name": os.getenv("BOT_NAME", "SimpleBot"),
        "version": "1.1"
    })

@app.route("/predict", methods=["POST"])
def predict():
    """
    Example inference endpoint.
    Expects JSON input: {"x": <number>}
    Returns: y = 2x + 1
    """
    data = request.get_json(silent=True) or {}
    x = data.get("x", None)

    if x is None:
        return jsonify({"error": "Missing 'x' in request body"}), 400

    try:
        x_val = float(x)
        y = 2 * x_val + 1
    except (TypeError, ValueError):
        return jsonify({"error": "x must be a number"}), 400

    return jsonify({
        "input": x_val,
        "output": y,
        "model": "y = 2x + 1",
        "bot_name": os.getenv("BOT_NAME", "SimpleBot")
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
