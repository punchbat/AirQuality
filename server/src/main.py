from fastapi import FastAPI
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from src.config import config
from src.core import add_application_exception_handler, exceptions_to_status_codes
from src.logger import setup_logger
from src.router import auth_router, profile_router, sensor_data_router, sensor_router
from src.schemas import ApiResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ALLOW_ORIGINS,
    allow_credentials=config.CORS_ALLOW_CREDENTIALS,
    allow_methods=config.CORS_ALLOW_METHODS,
    allow_headers=config.CORS_ALLOW_HEADERS,
)

setup_logger()

add_application_exception_handler(app, exceptions_to_status_codes)

app.include_router(auth_router, prefix="/api", tags=["Auth"])
app.include_router(profile_router, prefix="/api", tags=["Profile"])
app.include_router(sensor_router, prefix="/api", tags=["Sensor"])
app.include_router(sensor_data_router, prefix="/api", tags=["SensorData"])

@app.get("/ping", tags=["Healthcheck"], response_model=ApiResponse[str])
def ping():
    return ApiResponse(
        status=status.HTTP_200_OK,
        payload="pong"
    )