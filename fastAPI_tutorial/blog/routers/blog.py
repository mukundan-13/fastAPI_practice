from fastapi import APIRouter, Depends, status
from .. import schemas, database
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog
router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)


@router.get("/", response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    return blog.create(request,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(database.get_db)):
    return blog.destroy(id,db)

# for updating the data


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    return blog.update(id,request,db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id:int, db: Session = Depends(database.get_db)):
   return blog.showById(id,db)
