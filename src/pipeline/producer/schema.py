from pydantic import BaseModel

class Message(BaseModel):
    title: str
    link: str
    img_link: str

class KafkaResponse(BaseModel):
    message: str
    data: dict