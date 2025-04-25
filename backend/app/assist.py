from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/suggest")
async def suggest_word(audio: UploadFile = File(None), text: str = ""):
    # processar áudio com ASR ou usar LLM para sugerir complemento
    return {"suggestion": "palavra_exemplo"}
