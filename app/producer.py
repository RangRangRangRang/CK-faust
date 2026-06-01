import asyncio

from app import Event, topic, app


async def produce_events() -> None:
    await app.start()
    try:
        for index in range(1, 11):
            event = Event(id=str(index), value=f"message-{index}")
            print(f"Producing event: {event}")
            await topic.send(value=event)
            await asyncio.sleep(1)
    finally:
        await app.stop()


if __name__ == "__main__":
    asyncio.run(produce_events())
