
from pydantic import BaseModel
from app.utils.statuses import StatusTask

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: StatusTask = StatusTask.To_Do