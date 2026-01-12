from fastapi import APIRouter, HTTPException, Depends, status
from ..import database, schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash
router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    # remove leading/trailing spaces and truncate string to 72 characters
    safe_password = request.password.strip()[:72]

    # hash with bcrypt

    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    return {"id": new_user.id, "name": new_user.name, "email": new_user.email}


@router.get("/{id}", response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    return user
