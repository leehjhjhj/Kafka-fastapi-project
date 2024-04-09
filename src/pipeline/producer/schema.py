from pydantic import BaseModel

class Message(BaseModel):
    message: str

class KafkaResponse(BaseModel):
    message: str
    data: dict