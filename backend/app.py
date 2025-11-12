from flask import Flask, jsonify
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

if __name__ == "__main__":
    app.run(debug=True, port=5001)
