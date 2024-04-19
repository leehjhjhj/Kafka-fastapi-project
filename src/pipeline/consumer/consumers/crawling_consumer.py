from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from core.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    VALUE_DESERIALIZER,
    loop,
    VALUE_SERIALIZER
)
from .consumer import Consumer
from article.domain.model import Article
import json, asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup

class CrawlingConsumer(Consumer):
    def __init__(self, group_id):
        self.consumer = AIOKafkaConsumer(
            'article.crawling.requests',
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
                sending_message = await self.get_detail_page(msg)
                await self.producer.send_and_wait(topic='article.translation.requests', value=sending_message)
        except Exception as e:
            print(f"error: {e}")
        finally:
            await self.stop()

    async def get_detail_page(self, msg):
        source_newspaper = msg.value.get('source_newspaper')
        msg.value.get('source_language')
        async with ClientSession() as session:
            async with session.get(msg.value.get('link')) as response:
                html = await response.text()
                loop = asyncio.get_event_loop()
                content =  await loop.run_in_executor(None, self.parse_html, html, source_newspaper)
                return {
                    "source_language": msg.value.get('source_language'),
                    "content": content
                }
                
    def parse_html(self, html, source_newspaper):
        soup = BeautifulSoup(html, 'html.parser')
        content = ''
        if source_newspaper == 'ytn':
            content = soup.find('div', id='CmAdContent').find('span').text
        elif source_newspaper == 'yahoo':
            content = soup.find('div', class_='article_body').get_text()
        return content


