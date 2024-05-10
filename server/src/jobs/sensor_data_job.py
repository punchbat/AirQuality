from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import APIRouter

from src.core import get_db_asynccontextmanager, RedisManager
from src.repository import SensorDataRepository, SensorRepository
from src.service import SensorDataService

def init_sensor_data_job(router: APIRouter):
    scheduler = AsyncIOScheduler()

    async def save_air_quality_data():
        async with get_db_asynccontextmanager() as session:
            sensor_repository = SensorRepository(session=session)
            sensor_data_repository = SensorDataRepository(session=session)
            redis_manager = RedisManager()
            sensor_data_service = SensorDataService(sensor_data_repository=sensor_data_repository, sensor_repository=sensor_repository, cache=redis_manager)
            await sensor_data_service.create_sensor_data_from_cache()

    @router.on_event("startup")
    async def startup_event():
        scheduler.add_job(save_air_quality_data, 'cron', second='*/10')
        scheduler.start()

    @router.on_event("shutdown")
    async def shutdown_event():
        scheduler.shutdown()