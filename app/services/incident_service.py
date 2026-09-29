from sqlalchemy.orm import Session

from app.domain.schemas import IncidentCreate
from app.repositories.incident_repository import IncidentRepository
from app.domain.models import Incident

class IncidentService:

    def __init__(self, repository: IncidentRepository):
        self.repository = repository

    def create_incident(self, db: Session, request: IncidentCreate) -> Incident:
        
        incident = Incident(
            title=request.title,
            description=request.description,
            severity=request.severity
        )

        return self.repository.create(db, incident)

    def get_all_incidents(self, db: Session) -> list[Incident]:
        return self.repository.get_all(db)

    def get_incident_by_id(self, db: Session, incident_id: int) -> Incident | None:
        return self.repository.get_by_id(db, incident_id)