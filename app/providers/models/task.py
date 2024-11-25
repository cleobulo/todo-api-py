from sqlmodel import SQLModel, Field
from typing import Union
from app.utils.statuses import StatusTask

class Task(SQLModel, table=True):
    id: Union[int, None] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str = Field(index=True)
    status: int = Field(index=True)

