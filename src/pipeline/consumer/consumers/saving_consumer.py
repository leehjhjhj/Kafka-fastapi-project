from aiokafka import AIOKafkaConsumer
from pipeline.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    VALUE_DESERIALIZER
)
from .consumer import Consumer
from article.domain.model import Article
from core.config import AsyncSession
from datetime import datetime

class SavingConsumer(Consumer):
    def __init__(self, group_id):
        self.consumer = AIOKafkaConsumer(
            'article.saving.requests',
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
                await self.create_and_save_article(msg)
                print("😊 저장 완료")
        except Exception as e:
            print(f"error: {e}")
        finally:
            await self.stop()

    async def create_and_save_article(self, msg):
        source_language = msg.value['source_language']
        async with AsyncSession() as session:
            common_fields = {
                'original_article_url': msg.value['link'],
                'thumbnail_url': msg.value.get('img_link', None),
                'date': msg.value['date'],
                'create_at': datetime.now(),
                'original_language_code': source_language,
                'source_newspaper': msg.value['source_newspaper']
            }
            if source_language == 'ko':
                article_fields = {
                    'title_kr': msg.value['title'],
                    'title_jp': msg.value['translated_title'],
                    'content_kr': msg.value['content'],
                    'content_jp': msg.value['translated_content'],
                    'preview_content_kr': self._make_preview(msg.value['content']),
                    'preview_content_jp': self._make_preview(msg.value['translated_content']),
                }
            else:
                article_fields = {
                    'title_kr': msg.value['translated_title'],
                    'title_jp': msg.value['title'],
                    'content_kr': msg.value['translated_content'],
                    'content_jp': msg.value['content'],
                    'preview_content_kr': self._make_preview(msg.value['translated_content']),
                    'preview_content_jp': self._make_preview(msg.value['content']),
                }
            article = Article(**common_fields, **article_fields)
            session.add(article)
            await session.commit()

    def _make_preview(self, content):
        return content[:50] + '...'