import json
import time

from kafka import KafkaProducer

from config import KAFKA_SERVER
from config import ORDER_TOPIC

producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

orders = []

for i in range(1, 21):

    amount = 100

    if i % 7 == 0:
        amount = -100

    orders.append(
        {
            "order_id": i,
            "customer": f"Customer-{i}",
            "amount": amount
        }
    )

for order in orders:

    producer.send(
        ORDER_TOPIC,
        order
    )

    print("Sent:", order)

    time.sleep(0.5)

producer.flush()

print("All orders sent")