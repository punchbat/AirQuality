from typing import Dict, Optional

from fastapi import Depends
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from src.config import config
from src.core import ConflictException, RedisManager
from src.models import SensorDataModel
from src.repository import SensorDataRepository, SensorRepository

import logging

from src.schemas import SensorDataResponse

logger = logging.getLogger(__name__)

class SensorDataService:
    def __init__(
            self,
            sensor_repository: SensorRepository = Depends(SensorRepository),
            sensor_data_repository: SensorDataRepository = Depends(SensorDataRepository),
            cache: RedisManager = Depends(),
        ):
        self.cache = cache
        self.sensor_repository = sensor_repository
        self.sensor_data_repository = sensor_data_repository

    async def create_sensor_data_from_cache(self) -> list[SensorDataModel]:
        try:
            data_list: list[dict] = self.cache.get_all(config.REDIS_SENSOR_DATA_KEY)
            if not data_list:
                logger.info("No data to process in Redis")
                return []

            sensors = await self.sensor_repository.get_list()
            sensor_map = {}
            for sensor in sensors:
                sensor_map.setdefault(sensor.sgid, sensor)

            for data in data_list:
                sensor = sensor_map.get(data.get("sgid"))
                del data['sgid']
                data.setdefault("sensor_id", sensor.id)
                data.setdefault("latitude", sensor.latitude)
                data.setdefault("longitude", sensor.longitude)

            entities = await self.sensor_data_repository.create_batch(data_list)
            return entities
        except IntegrityError:
            raise ConflictException("Some sensor data already registered")
        except SQLAlchemyError as e:
            raise ConflictException(f"Database error: {str(e)}")

    async def get_list_sensor_data_by_filters(self, filters: Dict[str, Optional[str]]) -> list[SensorDataResponse]:
        try:
            entities = await self.sensor_data_repository.get_list_sensor_data_by_filter(filters)
            return [SensorDataResponse(
                id=str(entity.id),
                sensorId=str(entity.sensor_id),
                temperature=entity.temperature,
                humidity=entity.humidity,
                CO2=entity.CO2,
                latitude=entity.latitude,
                longitude=entity.longitude,
                createdAt=entity.created_at,
                updatedAt=entity.updated_at,
            ) for entity in entities]
        except SQLAlchemyError as e:
            logger.error(f"Failed to query sensor data: {e}")
            raise ConflictException(f"Database error: {str(e)}")