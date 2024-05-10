import os

from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), '.env')

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=DOTENV, case_sensitive=True)
    
    RABBIT_MQ_USER: str = 'root'
    RABBIT_MQ_PASSWORD: str = 'root1234'
    RABBIT_MQ_HOST: str = 'air_quality_rabbitmq'
    RABBIT_MQ_PORT: str = '5672'
    RABBIT_MQ_EXCHANGE_NAME: str = 'sensor_data_exchange'
    RABBIT_MQ_QUEUE_NAME: str = 'sensor_data_queue'
    RABBIT_MQ_ROUTING_KEY: str = 'sensor_data'

    def get_rabbit_mq_uri(self) -> str:
        return (
            f'amqp://{self.RABBIT_MQ_USER}:{self.RABBIT_MQ_PASSWORD}'
            f'@{self.RABBIT_MQ_HOST}:{self.RABBIT_MQ_PORT}'
        )

config = Settings()