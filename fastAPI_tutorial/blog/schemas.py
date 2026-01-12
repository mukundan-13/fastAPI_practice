from pydantic import BaseModel
from typing import List

class BlogCreate(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

class ShowBlog(BlogCreate):
    class Config:
        orm_mode = True

# for fetching the title alone
# class ShowBlog(BaseModel):
#     title: str
#     body:str

#     class Config:
#         orm_mode = True


# class BlogResponse(BlogCreate):
#     id: int

#     class Config:
#         orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs:List[BlogCreate]=[]
    class Config:
        orm_mode = True

class ShowBlog(BlogCreate):
    title:str
    body:str
    creator:ShowUser
    class Config:
        orm_mode = True