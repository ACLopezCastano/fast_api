# app/models/user.py
from pydantic import BaseModel

class User(BaseModel):
    id: int
    nombre: str
    email: str