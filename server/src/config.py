import os

from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), '.env')

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=DOTENV, case_sensitive=True)
    
    AUTH_SECRET_KEY: str = '9_FO38Vd63Lht_kHh1Hc7Z7t6XG7nI4zvp2PAoXKsJQ'
    AUTH_ALGORITHM: str = 'HS256'
    AUTH_TOKEN_TTL: int = 60 * 60 * 24 * 7 # 7 days
    AUTH_TOKEN_NAME: str = 'token'
    AUTH_TOKEN_PATH: str = '/'
    AUTH_TOKEN_DOMAIN: str = 'localhost'
    AUTH_TOKEN_SECURE: bool = False
    AUTH_TOKEN_HTTP_ONLY: bool = True

    CORS_ALLOW_ORIGINS: list[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ['GET','POST','DELETE']
    CORS_ALLOW_HEADERS: list[str] = ['*']

    REDIS_HOST: str = 'air_quality_redis'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = 'root1234'
    REDIS_DB: int = 0
    REDIS_BATCH_SIZE: int = 50

    REDIS_SENSOR_DATA_KEY: str = "sensor_data"

    DB_USER: str = 'root'
    DB_PASSWORD: str = 'root1234'
    DB_HOST: str = 'air_quality_db'
    DB_PORT: int = 5432
    DB_NAME: str = 'air_quality_db'

    RABBIT_MQ_USER: str = 'root'
    RABBIT_MQ_PASSWORD: str = 'root1234'
    RABBIT_MQ_HOST: str = 'air_quality_rabbitmq'
    RABBIT_MQ_PORT: str = '5672'
    RABBIT_MQ_EXCHANGE_NAME: str = 'sensor_data_exchange'
    RABBIT_MQ_QUEUE_NAME: str = 'sensor_data_queue'
    RABBIT_MQ_ROUTING_KEY: str = 'sensor_data'

    MESSAGE_BUFFER_SIZE: int = 100

    def get_db_uri(self) -> str:
        return (
            f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

    def get_rabbit_mq_uri(self) -> str:
        return (
            f'amqp://{self.RABBIT_MQ_USER}:{self.RABBIT_MQ_PASSWORD}'
            f'@{self.RABBIT_MQ_HOST}:{self.RABBIT_MQ_PORT}'
        )

config = Settings()