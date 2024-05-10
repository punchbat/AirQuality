from typing import Dict, Optional

from fastapi import Depends
from sqlalchemy import select, or_, cast, String
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import SensorDataModel, SensorModel
from src.repository.base_repository import BaseRepository
from src.core import get_db

class SensorDataRepository(BaseRepository[SensorDataModel]):
    def __init__(self, session: AsyncSession = Depends(get_db)):
        super().__init__(SensorDataModel, session)

    async def get_list_sensor_data_by_filter(self, filters: Dict[str, Optional[str]]) -> list[SensorDataModel]:
        query = select(self.model)

        if 'search' in filters and filters['search']:
            search_pattern = f"%{filters['search']}%"

            sub_query = select(SensorModel.id).where(
                or_(
                    SensorModel.sgid.ilike(search_pattern),
                    SensorModel.name.ilike(search_pattern),
                    cast(SensorModel.id, String).ilike(search_pattern)
                )
            )

            sub_result = await self.db.execute(sub_query)
            sensor_ids = sub_result.scalars().all()

            if sensor_ids:
                query = query.where(self.model.sensor_id.in_(sensor_ids))
            else:
                return []

        if 'temperatureFrom' in filters and filters['temperatureFrom']:
            query = query.where(self.model.temperature >= float(filters['temperatureFrom']))
        if 'temperatureTo' in filters and filters['temperatureTo']:
            query = query.where(self.model.temperature <= float(filters['temperatureTo']))
        if 'humidityFrom' in filters and filters['humidityFrom']:
            query = query.where(self.model.humidity >= float(filters['humidityFrom']))
        if 'humidityTo' in filters and filters['humidityTo']:
            query = query.where(self.model.humidity <= float(filters['humidityTo']))
        if 'co2From' in filters and filters['co2From']:
            query = query.where(self.model.CO2 >= float(filters['co2From']))
        if 'co2To' in filters and filters['co2To']:
            query = query.where(self.model.CO2 <= float(filters['co2To']))
        if 'createdAtFrom' in filters and filters['createdAtFrom']:
            query = query.where(self.model.created_at >= filters['createdAtFrom'])
        if 'createdAtTo' in filters and filters['createdAtTo']:
            query = query.where(self.model.created_at <= filters['createdAtTo'])
        if 'updatedAtFrom' in filters and filters['updatedAtFrom']:
            query = query.where(self.model.created_at >= filters['updatedAtFrom'])
        if 'updatedAtTo' in filters and filters['updatedAtTo']:
            query = query.where(self.model.created_at <= filters['updatedAtTo'])

        result = await self.db.execute(query)

        return result.scalars().all()