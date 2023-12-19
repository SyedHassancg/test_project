import logging
from typing import Dict, Any

from fastapi import APIRouter, Request, status
from fastapi.responses import ORJSONResponse

logger = logging.getLogger(__name__)

callback_router = APIRouter(
    prefix="/callback",
    responses={404: {"description": "Not found"}},
)


@callback_router.post("/")
async def create_transaction(
        request_data: Request, json_data: Dict[str, Any]
) -> ORJSONResponse:
    """
    Logs JSON data.

    Args:
        json_data: Data in json format.
        request_data: Request.

    Returns:
        Success message.
    """
    logger.info(json_data)
    return ORJSONResponse(
        content={"data": json_data}, status_code=status.HTTP_200_OK
    )
