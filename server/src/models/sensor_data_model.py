from sqlalchemy import Column, FLOAT, NUMERIC, UUID, ForeignKey

from .base_model import BaseDBModel

class SensorDataModel(BaseDBModel):
    __tablename__: str = "sensor_data"

    sensor_id = Column(UUID, ForeignKey('sensors.id'), nullable=False)

    temperature = Column(FLOAT, nullable=True)
    humidity = Column(FLOAT, nullable=True)
    CO2 = Column(FLOAT, nullable=True)

    latitude = Column(NUMERIC, nullable=True)
    longitude = Column(NUMERIC, nullable=True)