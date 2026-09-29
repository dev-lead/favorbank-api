import time
from fastapi import FastAPI, Request
from app.api.v1.endpoints.health import router as app_router

app = FastAPI(title="FavorBank API")

# Include the endpoint router under the /api/v1 prefix
app.include_router(app_router, prefix="/api/v1", tags=["App"])


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    request.state.start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - request.state.start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}"
    return response