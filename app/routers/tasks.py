from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder
from app.models.task import Task

router = APIRouter()

tasksList = list()

@router.post("/task/", status_code=status.HTTP_201_CREATED, response_model=TaskCreateOut)
async def createTask(task: TaskCreateIn):
    global taskNewItem

    for taskItem in tasksList:
        if taskItem.title == task.title:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este item já existe!")
    else:
        taskNewItem = Task(
            id=tasksList.__len__() + 1,
            title=task.title,
            description=task.description
        )
        tasksList.append(taskNewItem)

    return taskNewItem

@router.get("/tasks/", status_code=status.HTTP_200_OK, response_model=TasksListOut)
async def listAllTasks():
    tasksListResponse = TasksListOut(
        items=tasksList,
        size=tasksList.__len__()
    )
    return tasksListResponse

@router.patch("/task/{taskId}", status_code=status.HTTP_200_OK, response_model=TaskUpdateOut)
async def updateTask(taskId: int, task: TaskUpdateIn):
    for index, item in enumerate(tasksList):
        if taskId == item.id:
            taskItemStored = Task(**jsonable_encoder(item))
            taskUpdateData = task.model_dump(exclude_unset=True)
            taskUpdatedItem = taskItemStored.model_copy(update=taskUpdateData)
            tasksList[index] = taskUpdatedItem
            return taskUpdatedItem
        
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este item não existe!")
