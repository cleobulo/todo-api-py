from fastapi import APIRouter, status, HTTPException, Query
from fastapi.encoders import jsonable_encoder
from app.models.task import Task
from app.models.task_create_in import TaskCreateIn
# from app.models.task_create_out import TaskCreateOut
from app.models.task_update_in import TaskUpdateIn
from app.models.task_update_out import TaskUpdateOut
# from app.models.task_list_out import TasksListOut
from app.providers.db.engine import SessionDep
from app.providers.models.task import Task as TaskDB
from typing_extensions import Annotated
from sqlmodel import select
from typing import List

router = APIRouter()

@router.post("/task/", status_code=status.HTTP_201_CREATED)
async def createTask(task_in: TaskCreateIn, session: SessionDep) -> Task:
    task = session.exec(select(TaskDB).where(TaskDB.title == task_in.title)).one_or_none()
    
    if task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este item já existe!")
    else:
        createTaskOnDB = TaskDB(**jsonable_encoder(task_in))
        session.add(createTaskOnDB)
        session.commit()
        session.refresh(createTaskOnDB)
        return createTaskOnDB

@router.get("/tasks/", status_code=status.HTTP_200_OK)
async def listAllTasks(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> List[Task]:
    tasks = session.exec(select(TaskDB).offset(offset).limit(limit)).all()
    return tasks

@router.patch("/task/{taskId}", status_code=status.HTTP_200_OK)
async def updateTask(task_id: int, task_in: TaskUpdateIn, session: SessionDep):
    task = session.get(TaskDB, task_id)
    
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este item não existe!")
    
    taskUpdateData = task_in.model_dump(exclude_unset=True)
    task.sqlmodel_update(taskUpdateData)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
