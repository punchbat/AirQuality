import redis
import json

from src.config import config

import logging

logger = logging.getLogger(__name__)

class RedisManager:
    def __init__(
            self,
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            password=config.REDIS_PASSWORD,
            db=config.REDIS_DB
        ):
        self.client = redis.StrictRedis(host=host, port=port, password=password, db=db, decode_responses=True)

        logger.info('Initializing Redis')

    def set(self, key, data):
        if isinstance(data, (dict, list)):
            data = json.dumps(data)
        self.client.rpush(key, data)

    def get_all(self, key):
        data_json_list = self.client.lrange(key, 0, -1)
        self.client.delete(key)
        return [json.loads(data_json) for data_json in data_json_list]

    def get_with_batch(self, key, batch_size=config.REDIS_BATCH_SIZE):
        data_json_list = self.client.lrange(key, 0, batch_size - 1)
        if data_json_list:
            self.client.ltrim(key, batch_size, -1)
        return [json.loads(data_json) for data_json in data_json_list]