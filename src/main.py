from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pipeline.producer.producer_router import producer_route
from pipeline.consumer.consumer_router import consume
import asyncio

app = FastAPI()
app.include_router(producer_route)
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