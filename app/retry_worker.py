import json
import time
from kafka import KafkaConsumer
from config import KAFKA_SERVER, RETRY_TOPIC

def write_log(message):
    with open("../log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

consumer = KafkaConsumer(
    RETRY_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Retry Worker started")
write_log("[SYSTEM] Retry Worker started")

for message in consumer:
    order = message.value
    print(f"Retrying Order {order['order_id']}...")
    write_log(f"[RETRY] Retrying Order {order['order_id']} | {order['customer']}")
    time.sleep(3)
    print(f"Retry Success Order {order['order_id']}")
    write_log(f"[RETRY-OK] Order {order['order_id']} retry success")