from fastapi import APIRouter
from .consumers.raw_article_consumer import RawArticleConsumer
from .consumers.translating_consumer import TranslatingConsumer
from .consumers.saving_consumer import SavingConsumer
import asyncio

consumer_route = APIRouter()

async def consume():
    raw_article_consumer = RawArticleConsumer(group_id="test-group")
    translating_article_consumer = TranslatingConsumer(group_id='translation-consumer-group')
    saving_consumer = SavingConsumer(group_id='saving-consumer-group')
    await raw_article_consumer.start()
    await translating_article_consumer.start()
    await saving_consumer.start()
    await asyncio.gather(
        raw_article_consumer.consume(),
        translating_article_consumer.consume(),
        saving_consumer.consume()
    )
