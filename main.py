from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import crud, models, schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="MyTTA")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def index():
    return {'message': 'mytta main app'}


@app.get('/tickets/', response_model=list[schemas.Ticket])
async def read_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tickets = crud.get_tickets(db, skip=skip, limit=limit)
    return tickets