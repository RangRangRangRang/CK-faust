from faust import App, Record

app = App(
    "ck_faust",
    broker="kafka://kafka:9092",
    value_serializer="raw",
)


class Event(Record, serializer="json"):
    id: str
    value: str


topic = app.topic("events", value_type=Event)


@app.agent(topic)
async def process(events):
    async for event in events:
        print(f"Processed event: {event.id} => {event.value}")
