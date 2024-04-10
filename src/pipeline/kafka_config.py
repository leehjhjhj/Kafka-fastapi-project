import json
import asyncio

loop = asyncio.get_event_loop()
KAFKA_BOOTSTRAP_SERVERS = ['my-kafka:9092']
KAFKA_TOPIC_NAME = 'test'
VALUE_SERIALIZER = str.encode
VALUE_DESERIALIZER = lambda x: json.loads(x.decode('utf-8'))