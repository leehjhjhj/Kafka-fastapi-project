from fastapi import APIRouter
from .raw_article_consumer import RawArticleConsumer

consumer_route = APIRouter()

async def consume():
    raw_article_consumer = RawArticleConsumer(group_id="test-group")
    await raw_article_consumer.start()
    await raw_article_consumer.consume()
