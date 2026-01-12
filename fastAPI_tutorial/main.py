from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


@app.get('/')
def index():
    return {"data": {"name": "abc"}}


@app.get('/about')
def about():
    return {"data": "about page"}


@app.get('/blog')
def get(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db list'}
    else:
        return {'data': f'{limit} all blogs from the db list...........'}


@app.get('/blog/unpublished')
def show():
    return {"blog": "All unpublished"}


@app.get('/blog/{id}')
def show(id: int):
    return {"data": id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]=None


@app.post('/blog')
def create(blog: Blog):
    return {"data": f"blog is created with title as {blog.title}"}


