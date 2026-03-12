from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CaseSchema(BaseModel):
    id: Optional[int] = None
    case_number: str
    case_initiated_on: Optional[datetime] = None
    case_updated: Optional[datetime] = None
    completed_status: bool = False

    class Config:
        from_attributes = True
        orm_mode = True