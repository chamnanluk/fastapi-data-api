from pydantic import BaseModel, Field


class RefreshRequest(BaseModel):
    report_name: str = Field(..., min_length=3, max_length=100)


class RefreshResponse(BaseModel):
    message: str
    report_name: str
