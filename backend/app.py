import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

def generate_candlestick_data(num_points=100):
    data = []
    current_time = int(time.time())
    price = 100
    for i in range(num_points):
        open_price = price
        close_price = open_price + random.uniform(-1, 1)
        high_price = max(open_price, close_price) + random.uniform(0, 0.5)
        low_price = min(open_price, close_price) - random.uniform(0, 0.5)
        data.append({
            "time": current_time - (num_points - i) * 86400,  # One day interval
            "open": open_price,
            "high": high_price,
            "low": low_price,
            "close": close_price,
        })
        price = close_price
    return data

@app.route("/api/data")
def get_data():
    return jsonify(generate_candlestick_data())

@app.route("/api/market_summary", methods=["POST"])
def get_market_summary():
    data = request.get_json()
    if not data or "candlestick_data" not in data:
        return jsonify({"error": "Missing candlestick_data"}), 400

    candlestick_data = data["candlestick_data"]

    prompt = "Analyze the following candlestick data and provide a brief market summary:\n\n"
    for item in candlestick_data:
        prompt += f"Time: {item['time']}, Open: {item['open']}, High: {item['high']}, Low: {item['low']}, Close: {item['close']}\n"

    api_key = os.environ.get("OPENAI_API_KEY")
    api_base_url = os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1")

    if not api_key:
        return jsonify({"error": "OPENAI_API_KEY not configured"}), 500

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
    }

    try:
        response = requests.post(f"{api_base_url}/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        summary = response.json()["choices"][0]["message"]["content"]
        return jsonify({"summary": summary})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
