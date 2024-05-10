import asyncio

import logging

from rabbit import RabbitMQProducer
from logger import setup_logger
from sensor_data_model import generate_random_sensor_data

setup_logger()

logger = logging.getLogger(__name__)

rabbit_producer = RabbitMQProducer()

async def main():
    logger.info(f"Starting producing...")
    await rabbit_producer.connect_to_rabbit()
    try:
        while True:
            sensor_data = generate_random_sensor_data()
            await rabbit_producer.publish_message(sensor_data.to_json())
            await asyncio.sleep(2)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
    finally:
        await rabbit_producer.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
