from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_exercises(username: str):
    # ler responses.json, analisar perfil de anomia/apraxia
    # gerar e retornar lista de exercícios personalizados
    return {
        "exercises": [
            {"id": "ex1", "text": "Nomeie esta figura: ..."},
        ]
    }
