import asyncio

from fastapi import WebSocket, Depends, Query
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from fastapi import APIRouter
from starlette import status
from starlette.websockets import WebSocketDisconnect

from src.core import WebsocketManager, RabbitMQConsumer, RedisManager, NotFoundException
from src.dependecy import get_user_from_token_ws, get_user_from_token_http
from src.jobs import init_sensor_data_job
from src.models import UserModel
from src.schemas import ApiResponse
from src.service import JWTService, SensorDataService

import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/sensor-data/v1"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
jwt_service = JWTService()
websocket_manager = WebsocketManager()
redis_manager = RedisManager()
rabbit_consumer = RabbitMQConsumer(websocket_manager=websocket_manager, cache=redis_manager)

init_sensor_data_job(router)

@router.on_event("startup")
async def startup_event():
    asyncio.create_task(rabbit_consumer.start_consuming())

@router.on_event("shutdown")
async def shutdown_event():
    await rabbit_consumer.disconnect()

@router.get("/list", response_model=ApiResponse)
async def get_list_sensor_data_by_filters(
    search: Optional[str] = Query(None),
    temperatureFrom: Optional[float] = Query(None),
    temperatureTo: Optional[float] = Query(None),
    humidityFrom: Optional[float] = Query(None),
    humidityTo: Optional[float] = Query(None),
    co2From: Optional[float] = Query(None),
    co2To: Optional[float] = Query(None),
    createdAtFrom: Optional[str] = Query(None),
    createdAtTo: Optional[str] = Query(None),
    updatedAtFrom: Optional[str] = Query(None),
    updatedAtTo: Optional[str] = Query(None),
    _: UserModel = Depends(get_user_from_token_http),
    sensor_data_service: SensorDataService = Depends()
):
    filters = {
        "search": search,
        "temperature_from": temperatureFrom,
        "temperature_to": temperatureTo,
        "humidity_from": humidityFrom,
        "humidity_to": humidityTo,
        "co2_from": co2From,
        "co2_to": co2To,
        "created_at_from": createdAtFrom,
        "created_at_to": createdAtTo,
        "updated_at_from": updatedAtFrom,
        "updated_at_to": updatedAtTo
    }
    filters = {k: v for k, v in filters.items() if v is not None}

    try:
        sensor_data = await sensor_data_service.get_list_sensor_data_by_filters(filters)
        return ApiResponse(
            status=status.HTTP_200_OK,
            payload=sensor_data
        )
    except Exception as e:
        raise NotFoundException(f"Could not find sensor data by filters {filters}")

@router.websocket("/ws")
async def connect(websocket: WebSocket, _: UserModel = Depends(get_user_from_token_ws)):
    try:
        await websocket_manager.connect(websocket)
        while True:
            # Создаем задачу для отправки сообщения и ждем её выполнения с таймаутом
            try:
                await asyncio.wait_for(websocket.send_text('ping'), timeout=10)
            except asyncio.TimeoutError:
                logger.error("Timeout: Sending 'ping' message took too long.")
                break  # Выход из цикла, если отправка сообщения занимает слишком много времени
            await asyncio.sleep(10)  # Подождать перед отправкой следующего пинга
    except WebSocketDisconnect as e:
        logger.info("WebSocket disconnected gracefully with code: {}".format(e.code))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        await websocket_manager.disconnect(websocket, code=status.WS_1001_GOING_AWAY, reason=str(e))
    finally:
        await websocket_manager.disconnect(websocket)