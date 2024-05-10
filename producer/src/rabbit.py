import json
import aio_pika
from aio_pika import ExchangeType

from config import config

import logging

logger = logging.getLogger(__name__)

class RabbitMQProducer:
    def __init__(
            self,
            rabbit_mq_uri: str = config.get_rabbit_mq_uri(),
            exchange_name: str = config.RABBIT_MQ_EXCHANGE_NAME,
            routing_key: str = config.RABBIT_MQ_ROUTING_KEY
        ):
        self.rabbit_url = rabbit_mq_uri
        self.exchange_name = exchange_name
        self.routing_key = routing_key

        logger.info('Initializing RabbitMQConsumer')

    async def connect_to_rabbit(self):
        self.connection = await aio_pika.connect_robust(self.rabbit_url)
        self.channel = await self.connection.channel()  # Создаем канал
        logger.info('Created rabbit_mq channel')

        # Объявляем обменник
        self.exchange = await self.channel.declare_exchange(
            self.exchange_name,
            ExchangeType.DIRECT,  # Тип обменника: Direct, Fanout, Topic, Headers
            durable=True  # Долговечный
        )
        logger.info('Declared rabbit_mq exchange')

    async def publish_message(self, message: str):
        message_body = message.encode()
        await self.exchange.publish(
            aio_pika.Message(body=message_body),
            routing_key=self.routing_key
        )
        logger.info(f"Published message {message}")

    async def disconnect(self):
        logger.info("Close connection to rabbit_mq")
        await self.connection.close()