from pydantic import BaseModel
from app.utils.statuses import StatusTask

class TaskCreateOut(BaseModel):
    id: int
    title: str
    description: str
    status: StatusTask