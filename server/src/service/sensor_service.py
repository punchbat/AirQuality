from fastapi import Depends
from sqlalchemy.exc import  SQLAlchemyError

from src.core import ConflictException
from src.repository import SensorRepository

import logging

from src.schemas import SensorResponse

logger = logging.getLogger(__name__)

class SensorService:
    def __init__(
            self,
            sensor_repository: SensorRepository = Depends(SensorRepository),
        ):
        self.sensor_repository = sensor_repository

    async def get_list_sensor(self) -> list[SensorResponse]:
        try:
            entities = await self.sensor_repository.get_list()
            return [SensorResponse(
                    id=str(entity.id),
                    sgid=entity.sgid,
                    name=entity.name,
                    description=entity.description,
                    latitude=entity.latitude,
                    longitude=entity.longitude,
                    createdAt=entity.created_at,
                    updatedAt=entity.updated_at,
                ) for entity in entities]
        except SQLAlchemyError as e:
            raise ConflictException(f"Database error: {str(e)}")

    async def get_sensor_by_sgid(self, sgid: str) -> SensorResponse:
        try:
            sensor = await self.sensor_repository.get_by_sgid(sgid)
            return SensorResponse(
                    id=str(sensor.id),
                    sgid=sensor.sgid,
                    name=sensor.name,
                    description=sensor.description,
                    latitude=sensor.latitude,
                    longitude=sensor.longitude,
                    createdAt=sensor.created_at,
                    updatedAt=sensor.updated_at,
                )
        except SQLAlchemyError as e:
            raise ConflictException(f"Database error: {str(e)}")