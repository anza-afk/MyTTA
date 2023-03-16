from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from schemas import tickets, jobs, users


def commit_to_db(db:Session, db_model: models.Base) -> None:
    db.add(db_model)
    db.commit()
    db.refresh(db_model)


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(
        models.User.email == email
    ).first()


def create_superuser(
    user_id: int,
    db: Session
) -> None:
    db_superuser = models.Superuser(
            user_id=user_id
        )
    commit_to_db(db=db, db_model=db_superuser)


def create_user(
        db: Session,
        user: users.UserCreate,
        is_super: bool
) -> models.User :
    # add hash password func here
    db_user = models.User(
        **user.dict(),
    )
    commit_to_db(db=db, db_model=db_user)

    if is_super:
        create_superuser(db=db, user_id=db_user.id)
    
    return db_user


def update_user(
        db: Session,
        user_id: int,
        update_data: users.UserBase,
) -> models.User :
    db_user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail=f'The User with the id {user_id} is not found'
        )
    else:
        
        for key, value in update_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user


def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ticket).offset(skip).limit(limit).all()


def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket).filter(
        models.Ticket.id == ticket_id
    ).first()


def create_ticket(
        db: Session,
        ticket: tickets.TicketCreate,
        user_id: int
) -> models.Ticket :
    db_ticket = models.Ticket(
        **ticket.dict(),
        owner_id = user_id
    )
    commit_to_db(db=db, db_model=db_ticket)
    return db_ticket
