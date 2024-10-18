from pydantic import BaseModel

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