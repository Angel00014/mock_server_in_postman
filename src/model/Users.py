from typing import List, Optional

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


class UpdateUser(BaseModel):
    role_id: int
    firstName: str
    lastName: str
    dep_id: str

class PartUpdateUser(BaseModel):
    role_id: Optional[int]
    firstName: Optional[str]
    lastName: Optional[str]
    dep_id: Optional[str]


class Users(BaseModel):
    users: List[ItemUsers]
