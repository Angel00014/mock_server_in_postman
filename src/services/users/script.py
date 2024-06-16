from fastapi import FastAPI
from src.model.Users import Users
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



# @app.post("/createUser")
#
#
# @app.post("/updateUser")
#
#
# @app.post("/partUpdateUser/{id}")
#
#
# @app.post("/deleteUser/{id}")