from .base import BaseAPIModel
from datetime import datetime
from typing import Optional

class SensorResponse(BaseAPIModel):
    id: str
    sgid: str
    name: str
    description: str
    latitude: float
    longitude: float
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None