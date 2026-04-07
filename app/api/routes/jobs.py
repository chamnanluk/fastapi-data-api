from fastapi import APIRouter, BackgroundTasks

from app.schemas.jobs import RefreshRequest, RefreshResponse
from app.services.job_service import write_job_log

router = APIRouter(tags=["Jobs"])


@router.post("/refresh-report", response_model=RefreshResponse)
def refresh_report(payload: RefreshRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_job_log, payload.report_name)
    return RefreshResponse(
        message="Refresh request accepted",
        report_name=payload.report_name,
    )
