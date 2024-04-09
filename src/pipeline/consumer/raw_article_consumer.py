from aiokafka import AIOKafkaConsumer
from pipeline.kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC_NAME, VALUE_DESERIALIZER
from .consumer import Consumer

class RawArticleConsumer(Consumer):
    def __init__(self, group_id):
        self.consumer = AIOKafkaConsumer(
            KAFKA_TOPIC_NAME,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=group_id,
            value_deserializer=VALUE_DESERIALIZER,
            auto_offset_reset='earliest'
        )

    async def start(self):
        await self.consumer.start()

    async def stop(self):
        await self.consumer.stop()

    async def consume(self):
        try:
            async for msg in self.consumer:
                print("consumed: ", msg)
        finally:
            await self.consumer.stop()