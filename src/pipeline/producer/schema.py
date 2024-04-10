from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    title: str
    link: str
    img_link: Optional[str]
    source_language: str

class KafkaResponse(BaseModel):
    message: str
    data: dict