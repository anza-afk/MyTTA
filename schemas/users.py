from pydantic import BaseModel

# User Pydantic models
class UserBase(BaseModel):
    email: str
    is_active: bool = True

    class Config:
        orm_mode = True


class User(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class Superuser(BaseModel):
    user_id = int


# Profile Pydantic models
class ProfileBase(BaseModel):
    name: str
    surmane: str
    patronymic: str

    class Config:
        orm_mode = True


class Profile(ProfileBase):
    id: int
    job_id: int
    department_id: int


class ProfileCreate(ProfileBase):
    name: str
    surmane: str
    patronymic: str
