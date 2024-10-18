from pydantic import BaseModel
from typing import List
from app.models.task import Task

class TasksListOut(BaseModel):
    items: List[Task]
    size: int