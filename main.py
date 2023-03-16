from fastapi import APIRouter, FastAPI, Depends, HTTPException, Body
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import crud, models
from schemas import jobs, tickets, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="MyTTA")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return {'message': 'mytta main app'}


@app.get('/users/', response_model=list[users.User])
def read_users(
    skip: int = 0,
    limit: int = 100,db: Session = Depends(get_db)
):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


@app.get('/users/{user_id}', response_model=users.User)
def fetch_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    return user


@app.post('/users/', response_model=users.User)
def create_user(
    user: users.UserCreate,
    db: Session = Depends(get_db),
    is_super: bool = Body(default=False)
):
    if crud.get_user_by_email(db=db, email=user.email):
        raise HTTPException(
            status_code=400,
            detail=f"{user.email} is already registered"
        )
    return crud.create_user(db=db, user=user, is_super=is_super)


@app.patch('/users/', response_model=users.User)
def update_user(
    user_id: int,
    user: users.UserBase,
    db: Session = Depends(get_db),
    # is_super: bool = Body(default=False)
):
    update_data = user.dict()
    return crud.update_user(
        db=db,
        user_id=user_id,
        update_data=update_data
    )


@app.get('/tickets/', response_model=list[tickets.Ticket])
def read_tickets(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    tickets = crud.get_tickets(db=db, skip=skip, limit=limit)
    return tickets


@app.get('/tickets/{ticket_id}', response_model=tickets.Ticket)
def fetch_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db=db, ticket_id=ticket_id)
    return ticket


@app.post('/tickets/', response_model=tickets.Ticket)
def create_ticket_for_user(
    user_id: int,
    ticket: tickets.TicketCreate,
    db: Session = Depends(get_db)
):
    return crud.create_ticket(
        db=db,
        ticket=ticket,
        user_id=user_id
    )