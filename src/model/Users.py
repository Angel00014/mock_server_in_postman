from typing import List

from pydantic import BaseModel, RootModel


class ItemUsers(BaseModel):
    id: int
    role_id: int
    firstName: str
    lastName: str
    dep_id: str


class ReturnOneUser(BaseModel):
    id: int
    role_id: int
    firstName: str
    lastName: str
    dep_id: str


class CreateUser(BaseModel):
    role_id: int
    firstName: str
    lastName: str
    dep_id: str


class Users(BaseModel):
    users: List[ItemUsers]
