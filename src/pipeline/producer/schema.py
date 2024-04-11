from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    title: str
    link: str
    img_link: Optional[str]
    date: str
    content: str
    source_language: str
    source_newspaper: str

class KafkaResponse(BaseModel):
    message: str
    data: dict