from typing import Optional

from pydantic import BaseModel

class IncidentCreate(BaseModel):
    title: str
    description: str
    priority: str

class IncidentResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str

    class Config:
        from_attributes = True

class IncidentUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None