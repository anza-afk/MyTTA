from sqlalchemy.orm import Session

import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(
        models.User.id == user_id
    ).first()


def create_user(
        db: Session,
        user: schemas.tickets.UserCreate,
) -> models.User :
    # add hash password func here
    db_user = models.User(
        **user.dict(),
    )
    db.add(db_user)
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
        ticket: schemas.tickets.TicketCreate,
        user_id: int
) -> models.Ticket :
    db_ticket = models.Ticket(
        **ticket.dict(),
        owner_id = user_id
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket