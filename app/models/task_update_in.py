from pydantic import BaseModel
from app.utils.statuses import StatusTask

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