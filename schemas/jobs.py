from pydantic import BaseModel

# Job Pydantic models
class JobBase(BaseModel):
    name: str
    departments: list[int]

    class Config:
        orm_mode = True


class Job(JobBase):
    id: int
    departments: list[int]


class JobCreate(JobBase):
    pass


# Department Pydantic models
class DepartmentBase(BaseModel):
    id: int
    name: str
    address: str
    jobs: list[int]

    class Config:
        orm_mode = True


class Department(DepartmentBase):
    id: int


class DepartmentCreate(DepartmentBase):
    pass



