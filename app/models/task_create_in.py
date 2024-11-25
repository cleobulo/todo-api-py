from pydantic import BaseModel
from app.utils.statuses import StatusTask

class TaskCreateIn(BaseModel):
    title: str
    description: str = None
    status: StatusTask = StatusTask.To_Do

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