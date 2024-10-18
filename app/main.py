from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TaskCreateIn(BaseModel):
    title: str
    description: str = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Nova task",
                    "description": "Nova tarefa chata pra caralho!"
                }
            ]
        }
    }


class TaskCreateOut(BaseModel):
    id: int
    title: str
    description: str
    status: StatusTask

class TasksListOut(BaseModel):
    items: List[Task]
    size: int

class TaskUpdateIn(BaseModel):
    title: str = None
    description: str = None
    status: StatusTask = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Alterar task",
                    "description": "Alterar tarefa chata pra caralho!",
                    "status": 2
                }
            ]
        }
    }

class TaskUpdateOut(BaseModel):
    id: int
    title: str
    description: str
    status: StatusTask

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
