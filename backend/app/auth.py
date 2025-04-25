from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json, bcrypt

router = APIRouter()
USERS_FILE = "users.json"

class UserIn(BaseModel):
    username: str
    password: str = None

def load_users():
    try:
        with open(USERS_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

@router.post("/register")
def register(user: UserIn):
    users = load_users()
    if user.username in users:
        raise HTTPException(400, "Usuário já existe")
    pwd = user.password or bcrypt.gensalt().decode()
    hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()
    users[user.username] = hashed
    save_users(users)
    return {"username": user.username}

@router.post("/login")
def login(user: UserIn):
    users = load_users()
    hashed = users.get(user.username)
    if not hashed or not bcrypt.checkpw(user.password.encode(), hashed.encode()):
        raise HTTPException(401, "Credenciais inválidas")
    return {"message": "Login bem-sucedido"}
