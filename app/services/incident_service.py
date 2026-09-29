from sqlalchemy.orm import Session

from app.domain.schemas import IncidentCreate, IncidentUpdate
from app.repositories.incident_repository import IncidentRepository
from app.domain.models import Incident

class IncidentService:

    def __init__(self, repository: IncidentRepository):
        self.repository = repository

    def create_incident(self, db: Session, request: IncidentCreate) -> Incident:
        
        incident = Incident(
            title=request.title,
            description=request.description,
            priority=request.priority
        )

        return self.repository.create(db, incident)

    def get_all_incidents(self, db: Session) -> list[Incident]:
        return self.repository.get_all(db)

    def get_incident_by_id(self, db: Session, incident_id: int) -> Incident | None:
        return self.repository.get_by_id(db, incident_id)

    def update_incident(self, db: Session, incident_id: int, request: IncidentUpdate) -> Incident | None:
        incident = self.repository.get_by_id(db, incident_id)
        if not incident:
            return None
       
        updates = request.model_dump(exclude_unset=True)

        for key, value in updates.items():
            setattr(incident, key, value)

        return self.repository.update(db, incident)

    def delete_incident(self, db: Session, incident_id: int) -> bool | None:
        incident = self.repository.get_by_id(db, incident_id)
        if not incident:
            return None
        self.repository.delete(db, incident)
        return True