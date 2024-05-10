from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from starlette import status

from src.dependecy import get_user_from_token_http
from src.models import UserModel
from src.schemas import ApiResponse
from src.service import SensorService

router = APIRouter(
    prefix="/sensor/v1"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/list", response_model=ApiResponse)
async def get_list(_: UserModel = Depends(get_user_from_token_http), sensor_service: SensorService = Depends()):
    sensors = await sensor_service.get_list_sensor()
    return ApiResponse(
        status=status.HTTP_200_OK,
        payload=sensors
    )

@router.get("/sensor/{sgid}", response_model=ApiResponse)
async def get_sensor_by_sgid(sgid: str, _: UserModel = Depends(get_user_from_token_http), sensor_service: SensorService = Depends()):
    sensor = await sensor_service.get_sensor_by_sgid(sgid)
    return ApiResponse(
        status=status.HTTP_200_OK,
        payload=sensor
    )