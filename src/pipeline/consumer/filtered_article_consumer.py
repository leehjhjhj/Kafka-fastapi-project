from aiokafka import AIOKafkaConsumer
from pipeline.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    VALUE_DESERIALIZER
)
from .consumer import Consumer
from config import AsyncSession
from article.domain.model import Article
from sqlalchemy import select, cast, Date
import json

class FilteredArticleConsumer(Consumer):
    def __init__(self, group_id):
        self.consumer = AIOKafkaConsumer(
            'filtered.article',
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=group_id,
            value_deserializer=VALUE_DESERIALIZER,
            max_poll_records=10,
            auto_offset_reset='earliest'
        )
    async def start(self):
        await self.consumer.start()

    async def stop(self):
        await self.consumer.stop()

    async def consume(self):
        try:
            async for msg in self.consumer:
                pass
        except Exception as e:
            print(f"error: {e}")
        finally:
            await self.stop()