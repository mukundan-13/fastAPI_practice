from fastapi import APIRouter
from .. import schemas
from typing import List



router=APIRouter()

@router.get("/blogs", response_model=List[schemas.ShowBlog], tags=['blogs'])
def get_blogs(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog