from .base import BaseAPIModel
from datetime import datetime
from typing import Optional

class SensorDataResponse(BaseAPIModel):
    id: str
    sensorId: str
    temperature: float
    humidity: float
    CO2: float
    latitude: float
    longitude: float
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None