from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Reporting Service")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Reporting Service funcionando"}

@app.get("/health")
def health():
    return {"status": "ok", "service": "reporting"}