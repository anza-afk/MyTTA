from pydantic import BaseModel


class Job(BaseModel):
    id: int
    name: str
    departments: list[int]


class Department(BaseModel):
    id: int
    name: str
    address: str
    jobs: list[int]


class User(BaseModel):
    id: int
    email: str
    passworf: str
    is_active: bool
    is_superuser: bool


class SuperUser(User):
    user_id = int


class Profile(BaseModel):
    id: int
    name: str
    surmane: str
    patronymic: str
    job_id: int
    department_id: int


class Ticket(BaseModel):
    id: int
    title: str
    text: str
    image: str
    owner_id: int


class Comment(BaseModel):
    id: int
    text: str
    image: str
    user_id: int
    ticket_id: int
    parent_id: int