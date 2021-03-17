import asyncio

from producer import Producer
from consumer import Consumer

from config import get_kafka_config
from config import get_kafka_topic

consume_count = 20
# Produce more than expecting to consume because some
# of the intial messages might not be consumed when
# starting from the latest offset.
produce_count = consume_count + 10


async def run_test(partition_lists):
    producer = Producer(get_kafka_config())
    coroutines = [
        asyncio.create_task(
            producer.produce(get_kafka_topic(), produce_count)
        )
    ]
    for partition_list in partition_lists:
        consumer = Consumer(get_kafka_config())
        coroutines.append(
            asyncio.to_thread(
                consumer.consume,
                get_kafka_topic(),
                partition_list,
                int(consume_count / len(partition_lists))
            )
        )
    await asyncio.gather(*coroutines)


async def main():
    print('Testing latency with 2 partitions and 1 consumer')
    await run_test([[0, 1]])

    print('Testing latency with 1 partition per consumer')
    await run_test([[0], [1]])


asyncio.run(main())
