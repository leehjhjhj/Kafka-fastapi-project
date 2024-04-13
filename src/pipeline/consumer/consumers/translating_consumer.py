from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from pipeline.kafka_config import (
    KAFKA_BOOTSTRAP_SERVERS,
    VALUE_DESERIALIZER,
    loop,
    VALUE_SERIALIZER
)
from .consumer import Consumer
import boto3, asyncio, os, json
from concurrent.futures import ThreadPoolExecutor
from functools import partial

class TranslatingConsumer(Consumer):
    def __init__(self, group_id):
        self.consumer = AIOKafkaConsumer(
            'article.translation.requests',
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            group_id=group_id,
            value_deserializer=VALUE_DESERIALIZER,
            max_poll_records=10,
            auto_offset_reset='earliest'
        )
        self.producer = AIOKafkaProducer(
            loop=loop,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=VALUE_SERIALIZER
        )
        self.translate_client = boto3.client(
            service_name='translate',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name='ap-northeast-2'
        )
    async def start(self):
        await self.consumer.start()
        await self.producer.start()

    async def stop(self):
        await self.consumer.stop()
        await self.producer.stop()

    async def consume(self):
        try:
            async for msg in self.consumer:
                print(f"🌹 raw.article에서 받았다.{msg.value['title']}")
                result = await self.translate(msg)
                sending_message = json.dumps(result.value)
                await self.producer.send_and_wait(topic='article.saving.requests', value=sending_message)
        except Exception as e:
            print(f"error: {e}")
        finally:
            await self.stop()

    async def translate(self, msg):
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            SourceLanguageCode =  msg.value['source_language']
            for target in ['title', 'content']:
                if SourceLanguageCode == 'ko':
                    TargetLanguageCode = 'ja'
                else:
                    TargetLanguageCode = 'ko'
                
                func = partial(
                    self.translate_client.translate_text,
                    Text=msg.value[target],
                    SourceLanguageCode=SourceLanguageCode,
                    TargetLanguageCode=TargetLanguageCode
                )
                response = await loop.run_in_executor(executor, func)
                msg.value[f'translated_{target}'] = response.get('TranslatedText')
        return msg