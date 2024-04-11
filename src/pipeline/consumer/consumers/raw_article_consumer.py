from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from pipeline.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC_NAME,
    VALUE_DESERIALIZER,
    VALUE_SERIALIZER,
    loop
)
from .consumer import Consumer
from datetime import datetime
from config import AsyncSession
from article.domain.model import Article
from sqlalchemy import select, cast, Date
import json

class RawArticleConsumer(Consumer):
    def __init__(self, group_id):
        self.consumer = AIOKafkaConsumer(
            KAFKA_TOPIC_NAME,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=group_id,
            value_deserializer=VALUE_DESERIALIZER,
            max_poll_records=10,
            auto_offset_reset='earliest'
        )
        self.producer = AIOKafkaProducer(
            loop=loop,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=VALUE_SERIALIZER
        )

    async def start(self):
        await self.consumer.start()
        await self.producer.start()

    async def stop(self):
        await self.consumer.stop()
        await self.producer.stop()

    async def consume(self):
        try:
            async for msg in self.consumer:
                if self._is_keyword_in_title(msg) and not await self._is_exist_article(msg):
                    try:
                        print(f"✅ {msg.value['title']} sending")
                        sending_message = json.dumps(msg.__dict__)
                        await self.producer.send_and_wait(topic='article.crawling.requests', value=sending_message)
                    except Exception as e:
                        print(f"Sending error: {e}")
        except Exception as e:
            print(f"error: {e}")
        finally:
            await self.stop()

    async def _is_exist_article(self, message):
        async with AsyncSession() as session:
            today = datetime.now().date()
            existing_urls = await session.execute(select(Article.original_article_url).where(cast(Article.create_at, Date) == today))
            existing_urls = existing_urls.scalars().all()
            if message.value['link'] in existing_urls:
                return True
            else:
                return False
            
    def _is_keyword_in_title(self, message):
        title = message.value['title']
        source_language = message.value['source_language']
        keyword_set = set()
        if source_language == "ko":
            keyword_set.update(["일본", "日", "기시다", "주한", "미일", "북일", "한일"])
        elif source_language == "jp":
            keyword_set.update(["韓国", "韓"])

        for i in range(len(title)):
            for j in range(i + 1, len(title) + 1):
                if title[i:j] in keyword_set:
                    return True
        return False
        