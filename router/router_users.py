from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUserSchema
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from fastapi.responses import JSONResponse

user = APIRouter()


#Crear
@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    with engine.connect() as conn:
        #convertir en diccionario
        user_modify = data_user.dict()
        #Codificar la contraseña
        user_modify["password"] = generate_password_hash(data_user.password, "pbkdf2:sha256:40", 30)

        conn.execute(users.insert().values(user_modify))
        return Response(status_code=HTTP_201_CREATED)


#Login
@user.post("/api/user/login")
def login(data_user: DataUserSchema):
    with engine.connect() as conn:
        #Comparar si los email son iguales
        result = conn.execute(users.select().where(users.c.email == data_user.email)).first()

        if result != None:
            check_password = check_password_hash(result[2], data_user.password)

            if check_password:
                return {
                    "status": 200,
                    "message": "Access success"
                }

        return {
            "status": HTTP_401_UNAUTHORIZED,
            "message": "Access denied"
        }