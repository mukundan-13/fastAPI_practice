from fastapi import APIRouter, Depends
from ..import database, schemas
from sqlalchemy.orm import Session
from ..repository import user
router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.createUser(request,db)


@router.get("/{id}", response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(database.get_db)):
    return user.showById(id,db)
