import random
import time
from flask import Flask, render_template, Response, request, jsonify
from kafka import KafkaConsumer
import json

app = Flask(__name__)


consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='web-group'  
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    
    symbol = request.args.get('symbol')
    
    if not symbol:
        return jsonify({"status": "No symbol provided"}), 400

    
    data = {
        'symbol': symbol,
        'timestamp': int(time.time()),  
        'price': round(random.uniform(100.0, 1500.0), 2)  
    }

    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
