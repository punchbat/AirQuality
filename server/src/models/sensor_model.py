from sqlalchemy import Column, VARCHAR, TEXT, NUMERIC

from .base_model import BaseDBModel

class SensorModel(BaseDBModel):
    __tablename__: str = "sensors"

    sgid = Column(VARCHAR(64), nullable=False, index=True, unique=True)
    name = Column(VARCHAR(255), nullable=True)
    description = Column(TEXT, nullable=True)

    latitude = Column(NUMERIC, nullable=False)
    longitude = Column(NUMERIC, nullable=False)