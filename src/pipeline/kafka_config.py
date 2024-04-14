import json
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

loop = asyncio.get_event_loop()
KAFKA_BOOTSTRAP_SERVERS = os.environ['KAFKA_BOOTSTRAP_SERVERS']
KAFKA_TOPIC_NAME = 'test'
VALUE_SERIALIZER = str.encode
VALUE_DESERIALIZER = lambda x: json.loads(x.decode('utf-8'))