import json
import time
from kafka import KafkaConsumer, KafkaProducer
from config import KAFKA_SERVER, ORDER_TOPIC, RETRY_TOPIC

def write_log(message):
    with open("../log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

worker_name = input("Worker name: ")

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)
consumer = KafkaConsumer(
    ORDER_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    group_id="order-workers",
    auto_offset_reset="latest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print(f"{worker_name} started")
write_log(f"[SYSTEM] {worker_name} started")

for message in consumer:
    order = message.value
    if order["amount"] < 0:
        print(f"[{worker_name}] Failed Order {order['order_id']}")
        write_log(f"[FAILED] {worker_name} | Order {order['order_id']} | {order['customer']} | ${order['amount']}")
        producer.send(RETRY_TOPIC, order)
        producer.flush()
    else:
        print(f"[{worker_name}] Processed Order {order['order_id']} ({order['customer']})")
        write_log(f"[OK] {worker_name} | Order {order['order_id']} | {order['customer']} | ${order['amount']}")