from fastapi import FastAPI
from src.model.Users import Users, ReturnOneUser, CreateUser, UpdateUser
from src.config import base_url_mock, auth_token
import requests

app = FastAPI()


@app.get("/getUsers", response_model=Users)
def getUsers():
    try:
        headers = {
            'Authorization': auth_token
        }
        url = f'{base_url_mock}/getUsers'
        response_result = requests.get(url, headers=headers)

        return (response_result.json())
    except Exception as e:
        print(e)


@app.post("/createUser", response_model=ReturnOneUser)
def createUser(request_data: CreateUser):
    try:
        headers = {
            'Authorization': auth_token,
            'Content - Type': 'application/json'
        }
        url = f'{base_url_mock}/createUser'
        response_result = requests.post(url, headers=headers, data=request_data.dict())

        return response_result.json()
    except Exception as e:
        print(e)

@app.put("/updateUser", response_model=ReturnOneUser)
def updateUser(request_data: UpdateUser):
    try:
        headers = {
            'Authorization': auth_token,
            'Content - Type': 'application/json'
        }
        url = f'{base_url_mock}/updateUser'
        response_result = requests.put(url, headers=headers, data=request_data.dict())

        return response_result.json()
    except Exception as e:
        print(e)

# @app.patch("/partUpdateUser/{id}")
#
#
# @app.post("/deleteUser/{id}")
