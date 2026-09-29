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