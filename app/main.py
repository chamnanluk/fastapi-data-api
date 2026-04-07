import time

from fastapi import FastAPI, Request

from app.api.routes import health, jobs, metrics, orders, sales
from app.core.config import settings

app = FastAPI(title=settings.app_name)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    response.headers["X-Process-Time"] = str(duration)
    return response


app.include_router(health.router)
app.include_router(orders.router)
app.include_router(metrics.router)
app.include_router(sales.router)
app.include_router(jobs.router)
