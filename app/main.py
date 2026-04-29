from fastapi import FastAPI
from app.core.config import settings
from app.db.database import Base, engine
from app.api.routes import notes


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="A simple but production-structured Notes REST API",
    version="1.0.0",
    debug=settings.DEBUG
)

app.include_router(notes.router, prefix="/notes", tags=["Notes"])


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME
    }
