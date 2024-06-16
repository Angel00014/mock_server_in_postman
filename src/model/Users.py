from typing import List

from pydantic import BaseModel, RootModel


class ItemUsers(BaseModel):
    id: int
    role_id: int
    firstName: str
    lastName: str
    dep_id: str


class Users(BaseModel):
    users: List[ItemUsers]



# {
#         "id": 521,
#         "role_id": "2",
#         "firstName": "Natali",
#         "lastName": "Smith",
#         "dep_id": "2"
#  }
