from kafka import KafkaConsumer
from kafka import TopicPartition

from datetime import datetime
from datetime import timezone
from datetime import timedelta

from config import get_kafka_config
from config import get_kafka_topic


class Consumer():
    def __init__(self, config):
        config['fetch_max_wait_ms'] = 100
        self.consumer = KafkaConsumer(**config)

    def consume(self, topic, partitions, count=10):
        topic = topic
        self.consumer.assign(
            [TopicPartition(topic, partition) for partition in partitions]
        )
        consumed = 0
        for msg in self.consumer:
            source_time = datetime.fromisoformat(msg.value.decode('utf8'))
            delta = (datetime.utcnow().replace(tzinfo=timezone.utc) - source_time) / timedelta(milliseconds=1)
            print(f'Partition {msg.partition} latency: {delta} ms')
            consumed += 1
            if consumed == count:
                break


if __name__ == '__main__':
    consumer = Consumer(get_kafka_config())
    partitions = [0]
    consumer.consume(get_kafka_topic(), partitions)
