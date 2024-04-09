from kafka import KafkaProducer
from pipeline.kafka_config import KAFKA_BOOTSTRAP_SERVERS, VALUE_SERIALIZER, KAFKA_TOPIC_NAME
from .schema import Message
import json

class Producer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=VALUE_SERIALIZER
            )

    def send(self, message: Message):
        message_str = json.dumps(message.__dict__)
        self.producer.send(KAFKA_TOPIC_NAME, value=message_str)
        self.producer.flush()
        self.producer.close()