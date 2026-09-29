from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.domain.schemas import (
    IncidentCreate, 
    IncidentResponse,
    IncidentUpdate
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
    incident = service.get_incident_by_id(db, incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.patch("/{incident_id}", response_model=IncidentResponse)
def update_incident(incident_id: int, incident: IncidentUpdate, db: Session = Depends(get_db)):
    updated_incident = service.update_incident(db, incident_id, incident)
    if not updated_incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return updated_incident

@router.delete("/{incident_id}", response_model=bool)
def delete_incident(incident_id: int, db: Session = Depends(get_db)):
    result = service.delete_incident(db, incident_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    return result