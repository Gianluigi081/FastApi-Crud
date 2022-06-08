from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.task_schema import TaskSchema
from config.db import engine
from model.tasks import tasks
from typing import List

task = APIRouter()

@task.get("/")
def root():
    return {"message": "Por favor, ingrese a: http://127.0.0.1:8000/docs"}


#Crear tarea
@task.post("/api/task", status_code=HTTP_201_CREATED)
def create_task(data_task: TaskSchema):
    with engine.connect() as conn:
        #convertir en diccionario
        task_modify = data_task.dict()
        print(task_modify)
        conn.execute(tasks.insert().values(task_modify))

        return Response(status_code=HTTP_201_CREATED)

#Actualizar
@task.put("/api/task/{task_id}")
def update_task(data_update: TaskSchema, task_id: str):
    with engine.connect() as conn:
        conn.execute(tasks.update().values(title=data_update.title, description=data_update.description).where(tasks.c.id==task_id))

        result = conn.execute(tasks.select().where(tasks.c.id==task_id)).first()

        return result

#Borrar usuarios
@task.delete("/api/task/{task_id}", status_code=HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    with engine.connect() as conn:
        conn.execute(tasks.delete().where(tasks.c.id==task_id))

        return Response(status_code=HTTP_204_NO_CONTENT)

#Todas las tareas
@task.get("/api/task", response_model=List[TaskSchema])
def get_tasks():
    with engine.connect() as conn:
        result = conn.execute(tasks.select()).fetchall()

    return result

#Mostrar información de una sola tarea
@task.get("/api/user/{task_id}", response_model=TaskSchema)
def get_task(task_id: str):
    with engine.connect() as conn:
        result = conn.execute(tasks.select().where(tasks.c.id == task_id)).first()

    return result