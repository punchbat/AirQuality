from fastapi import WebSocket
from typing import List

import logging

from starlette import status
from starlette.websockets import WebSocketState

logger = logging.getLogger(__name__)

class WebsocketManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"Connected {websocket.client}")

    async def disconnect(
            self,
            websocket: WebSocket,
            code: int = status.WS_1000_NORMAL_CLOSURE,
            reason: str | None = "Server closed the connection"
        ):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            if websocket.application_state != WebSocketState.DISCONNECTED:
                await websocket.close(code=code, reason=reason)
                logger.info(f"Disconnected {websocket.client}")

    async def broadcast(self, data: dict):
        disconnected_websockets = []
        for websocket in self.active_connections:
            try:
                await websocket.send_json(data)
            except Exception as e:
                logger.error(f"Error sending data: {e}. Disconnecting {websocket.client}.")
                disconnected_websockets.append(websocket)

        for websocket in disconnected_websockets:
            await self.disconnect(websocket)

    async def send_personal_message(self, data: dict, websocket: WebSocket):
        try:
            await websocket.send_json(data)
        except Exception as e:
            logger.error(f"Error sending personal data: {e}. Disconnecting {websocket.client}.")
            await self.disconnect(websocket)