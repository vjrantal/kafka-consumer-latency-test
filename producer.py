import asyncio

from datetime import datetime
from datetime import timezone

from kafka import KafkaProducer

from config import get_kafka_config
from config import get_kafka_topic


class Producer():
    def __init__(self, config):
        self.producer = KafkaProducer(**config)

    async def produce(self, topic, count=10):
        for produced in range(count):
            now = str(datetime.utcnow().replace(tzinfo=timezone.utc))
            # print(f'Produced {produced} at: {now}')
            future = self.producer.send(topic, str.encode(now))
            future.get(timeout=1)
            await asyncio.sleep(1)


if __name__ == '__main__':
    producer = Producer(get_kafka_config())
    asyncio.run(producer.produce(get_kafka_topic()))
