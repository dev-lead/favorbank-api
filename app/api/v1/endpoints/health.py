import time
from fastapi import APIRouter, status, Depends, Request
from app.core.config import Settings, get_settings
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

router = APIRouter(tags=["Health Check"])

class HealthResponse(BaseModel):
    status: str
    project_name: str
    environment: str
    process_time: float

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,  # Allows instantiating with either user_id or userId
    )

# Endpoint
@router.get("/health", status_code=status.HTTP_200_OK, response_model=HealthResponse)
async def get_status(request: Request, settings: Settings = Depends(get_settings)):
    start_time = getattr(request.state, "start_time", time.perf_counter())
    elapsed = round(time.perf_counter() - start_time, 4)

    health = HealthResponse(
        status="healthy",
        project_name=settings.PROJECT_NAME,
        environment=settings.ENVIRONMENT,
        process_time=elapsed
    )

    return health
