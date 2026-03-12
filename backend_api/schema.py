from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CaseSchema(BaseModel):
    id: int
    case_number: str
    case_initiated_on: Optional[datetime]
    case_updated: Optional[str]
    completed_status: bool

    class Config:
        orm_mode = True