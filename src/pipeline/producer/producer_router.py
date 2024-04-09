from fastapi import APIRouter, HTTPException
from .producer import Producer
from .schema import Message, KafkaResponse
import json

producer_route = APIRouter()

@producer_route.post('/create_message')
def send(message: Message):
    producer = Producer()
    try:
        producer.send(message=message)
        return message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))