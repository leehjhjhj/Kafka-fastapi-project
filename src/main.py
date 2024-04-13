from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pipeline.producer.producer_router import producer_route
from pipeline.consumer.consumer_router import consume
from article.router import article_router
import asyncio

app = FastAPI()
app.include_router(producer_route)
app.include_router(article_router)
asyncio.create_task(consume())

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)