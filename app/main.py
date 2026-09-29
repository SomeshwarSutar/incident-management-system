from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.incident import router as incident_router

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Sims API",
    description="API for managing incidents in the Sims application",
    version="1.0.0"
)

app.include_router(incident_router, prefix="/api/incidents", tags=["incidents"])


@app.get("/health", tags=["health"])
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


def __main__():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    __main__()