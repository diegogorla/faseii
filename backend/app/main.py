from fastapi import FastAPI
from app.auth import router as auth_router
from app.calibragem import router as calibragem_router
from app.exercises import router as exercises_router
from app.assist import router as assist_router

app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(calibragem_router, prefix="/calibragem")
app.include_router(exercises_router, prefix="/exercises")
app.include_router(assist_router, prefix="/assist")

@app.get("/")
def root():
    return {"message": "AphasiAPP API Running"}
