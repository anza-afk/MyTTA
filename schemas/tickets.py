from pydantic import BaseModel, FilePath
from datetime import datetime

# Ticket Pydantic models
class TicketBase(BaseModel):
    title: str
    text: str
    # image: FilePath | None
    image: str | None
    created_at: datetime

    class Config:
        orm_mode = True


class Ticket(TicketBase):
    id: int
    owner_id: int


class TicketCreate(TicketBase):
    pass


# Comment Pydantic models
class CommentBase(BaseModel):
    text: str
    image: str
    created_at: datetime

    class Config:
        orm_mode = True


class Comment(CommentBase):
    id: int
    user_id: int
    ticket_id: int
    parent_id: int | None
    resolved_at: datetime | None

class CommentCreate(CommentBase):
    pass