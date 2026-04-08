from pydantic import BaseModel

class Task(BaseModel):
    title: str

class TokenData(BaseModel):
    token: str