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


class Role(BaseModel):
    id: int
    name: str


class User(BaseModel):
    id: int
    email: str
    passworf: str
    is_active: bool


class SuperUser(User):
    tickets = list[int]


class Profile(BaseModel):
    id: int
    name: str
    surmane: str
    patronymic: str
    job_id: int
    department_id: int


class Ticket(BaseModel):
    id: int
    name: str
    description: str
    owner: int
