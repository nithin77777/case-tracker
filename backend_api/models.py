from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
import datetime
from .db_connection import Base


class CaseData(Base):
    __tablename__ = "test_Data"

    id = Column(Integer, primary_key=True, index=True)
    case_number = Column(String, index=True)
    case_initiated_on = Column(DateTime)
    case_updated = Column(DateTime, default=datetime.datetime.now)
    completed_status = Column(Boolean, default=False)
