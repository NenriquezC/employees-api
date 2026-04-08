from fastapi import FastAPI
from app.database import engine, Base
from app.routes import employee_router, auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employees API",
    description="REST API for employee management with JWT authentication",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(employee_router)

@app.get("/")
def root():
    return {"message": "Employees API is running"}