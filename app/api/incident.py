from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.domain.schemas import (
    IncidentCreate, 
    IncidentResponse
)

from app.repositories.incident_repository import (
    IncidentRepository
)

from app.services.incident_service import (
    IncidentService
)

router = APIRouter()

repository = IncidentRepository()
service = IncidentService(repository)

@router.post("/", response_model=IncidentResponse)
def create_incident(incident: IncidentCreate, db: Session = Depends(get_db)):
    return service.create_incident(db,incident)

@router.get("/", response_model=list[IncidentResponse])
def list_incidents(db: Session = Depends(get_db)):
    return service.get_all_incidents(db)

@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    return service.get_incident_by_id(db, incident_id)