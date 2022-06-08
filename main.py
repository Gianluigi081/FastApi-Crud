from fastapi import FastAPI
from dotenv import load_dotenv
from router.router_users import user
from router.router_tasks import task

app = FastAPI()

app.include_router(user)

app.include_router(task)