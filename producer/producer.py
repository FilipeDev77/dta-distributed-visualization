from kafka import KafkaProducer
import random
import time
import json
import threading

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'sensor-data'


def generate_stock_data():
    stock_data = {
        "symbol": "DTAcoin",  
        "open": round(random.uniform(100.0, 1500.0), 2),
        "high": round(random.uniform(100.0, 1500.0), 2),
        "low": round(random.uniform(100.0, 1500.0), 2),
        "close": round(random.uniform(100.0, 1500.0), 2),
        "timestamp": time.time()
    }
    return stock_data


def send_data(sensor_name):
    print(f"[Producer-{sensor_name}] Sending Apple stock data...")
    while True:
        data = generate_stock_data()
        producer.send(topic, value=data)
        print(f"[Producer-{sensor_name}] Sent: {data}")
        time.sleep(1)


for i in range(3):
    threading.Thread(target=send_data, args=(f"S{i+1}",), daemon=True).start()


while True:
    time.sleep(1)
