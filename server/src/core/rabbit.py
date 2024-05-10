import json
import aio_pika
from aio_pika import ExchangeType

from src.config import config

import logging

logger = logging.getLogger(__name__)

class RabbitMQConsumer:
    def __init__(
            self,
            websocket_manager,
            cache,
            rabbit_mq_uri: str = config.get_rabbit_mq_uri(),
            exchange_name: str = config.RABBIT_MQ_EXCHANGE_NAME,
            queue_name: str = config.RABBIT_MQ_QUEUE_NAME,
            routing_key: str = config.RABBIT_MQ_ROUTING_KEY
        ):
        self.websocket_manager = websocket_manager
        self.cache = cache
        self.rabbit_url = rabbit_mq_uri
        self.exchange_name = exchange_name
        self.queue_name = queue_name
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

        # Объявляем очередь
        self.queue = await self.channel.declare_queue(
            self.queue_name,
            durable=True,  # Долговечная
            auto_delete=False  # Не удалять автоматически
        )
        logger.info('Declared rabbit_mq queue')

        # Привязываем очередь к обменнику
        await self.queue.bind(self.exchange, self.routing_key)
        logger.info('Binded rabbit_mq queue')

    async def start_consuming(self):
        logger.info('Start consuming messages')

        await self.connect_to_rabbit()

        try:
            # Начинаем слушать сообщения из очереди
            async for message in self.queue:
                async with message.process():
                    try:
                        data: dict = json.loads(message.body.decode())

                        self.cache.set(config.REDIS_SENSOR_DATA_KEY, data)

                        await self.websocket_manager.broadcast(data)
                        # Не подтверждаем сообщениеwebsocket_manager, оно остаётся в очереди
                    except json.JSONDecodeError as e:
                        logger.error(f"JSON decoding error: {e}")
                    except Exception as e:
                        logger.error(f"Error processing message: {e}")

                    data = message.body.decode()
                    await self.websocket_manager.broadcast(data)  # Отправка данных всем подключенным через WebSocket
        except Exception as e:
            logger.error(f"Error in consumer: {e}")

    async def disconnect(self):
        logger.info("Close connection to rabbit_mq")
        await self.connection.close()