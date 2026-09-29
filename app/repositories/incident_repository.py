from sqlalchemy.orm import Session
from app.domain.models import Incident

class IncidentRepository:

    def create(self, db: Session, incident: Incident) -> Incident:
        db.add(incident)
        db.commit()
        db.refresh(incident)
        return incident

    def get_all(self, db: Session) -> list[Incident]:
        return db.query(Incident).all()

    def get_by_id(self, db: Session, incident_id: int) -> Incident | None:
        return db.query(Incident).filter(Incident.id == incident_id).first()

    def update(self, db: Session, incident: Incident) -> Incident:
        db.commit()
        db.refresh(incident)
        return incident

    def delete(self, db: Session, incident: Incident) -> None:
        db.delete(incident)
        db.commit()