from fastapi import FastAPI
from .database import engine
from . import models
from .routers import blog,user,authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# for creating the JSON data


# @app.post("/blogs", status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# for deleting the data


# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# def destroy(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# # for updating the data


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update(id, request: schemas.BlogCreate, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found")
#     blog.update(request.dict())
#     db.commit()
#     return "updated"

# for seeing the data


# @app.get("/blogs", response_model=List[schemas.ShowBlog], tags=['blogs'])
# def get_blogs(db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).all()
#     return blog


# @app.get("/blogs/{id}", status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id {id} is not available")
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {"details":f"Blog with the id {id} is not available"}
#     return blogs


# @app.post("/user", response_model=schemas.ShowUser, tags=['users'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     # remove leading/trailing spaces and truncate string to 72 characters
#     safe_password = request.password.strip()[:72]

#     # hash with bcrypt

#     new_user = models.User(
#         name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#     return {"id": new_user.id, "name": new_user.name, "email": new_user.email}


# @app.get("/user/{id}", response_model=schemas.ShowUser, tags=['users'])
# def show_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found")
#     return user
