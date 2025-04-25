from fastapi import APIRouter
from pydantic import BaseModel
import json, os

router = APIRouter()
RESPONSES_FILE = "responses.json"

class CalibragemIn(BaseModel):
    username: str
    question_id: str
    answer: str
    metadata: dict = {}

def init_storage():
    if not os.path.exists(RESPONSES_FILE):
        with open(RESPONSES_FILE, 'w') as f:
            json.dump([], f)

@router.post("/")
def submit_response(data: CalibragemIn):
    init_storage()
    with open(RESPONSES_FILE, 'r+') as f:
        arr = json.load(f)
        arr.append(data.dict())
        f.seek(0)
        json.dump(arr, f, indent=2)
    return {"status": "OK"}
