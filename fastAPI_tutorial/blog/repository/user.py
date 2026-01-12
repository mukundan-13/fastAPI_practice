from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas
from ..hashing import Hash


def createUser(request:schemas.BlogCreate,db:Session):
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

def showById(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    return user