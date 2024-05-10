from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import SensorModel
from src.repository.base_repository import BaseRepository
from src.core import get_db
from sqlalchemy.future import select

class SensorRepository(BaseRepository[SensorModel]):
    def __init__(self, session: AsyncSession = Depends(get_db)):
        super().__init__(SensorModel, session)

    async def get_by_sgid(self, sgid: str) -> SensorModel:
        result = await self.db.execute(select(self.model).where(self.model.sgid == sgid))
        return result.scalars().first()