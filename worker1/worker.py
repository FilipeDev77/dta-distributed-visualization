from kafka import KafkaConsumer
import time
import json
import threading
import requests


consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='latest',
    enable_auto_commit=False,
    fetch_min_bytes=1,
    fetch_max_wait_ms=500,
    heartbeat_interval_ms=1000,
    session_timeout_ms=10000,
    max_poll_records=1
)

BACKEND_URL = 'http://backend:5000/get_data'

print("[Worker] Waiting for new messages...")

def process_message(data):
    print(f"[Worker] Processing: {data}")
    try:
        
        response = requests.get(BACKEND_URL, params={'symbol': data['symbol']})
        
        if response.status_code == 200:
            print(f"[Worker] Data sent successfully: {data}")
        else:
            print(f"[Worker] Failed to send data. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"[Worker] Failed to send data: {e}")
    time.sleep(0.2)

while True:
    messages = consumer.poll(timeout_ms=500, max_records=1)
    if messages:
        for topic_partition, msgs in messages.items():
            for message in msgs:
                data = message.value.decode('utf-8')
                data = json.loads(data)
                
                data['timestamp'] = int(time.time())  
                
                threading.Thread(target=process_message, args=(data,), daemon=True).start()
    else:
        print("[Worker] No new messages...")
