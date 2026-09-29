from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    status = Column(String, default="open", nullable=False)
    