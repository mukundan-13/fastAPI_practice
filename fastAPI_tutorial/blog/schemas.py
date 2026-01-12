from pydantic import BaseModel
from typing import List, Optional

# ---------------- BLOG ----------------

class BlogCreate(BaseModel):
    title: str
    body: str

    model_config = {
        "from_attributes": True
    }


# ---------------- USER ----------------

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogCreate] = []

    model_config = {
        "from_attributes": True
    }


# ---------------- BLOG RESPONSE ----------------

class ShowBlog(BlogCreate):
    creator: Optional[ShowUser] = None   # 🔥 THIS FIXES 500 ERROR

    model_config = {
        "from_attributes": True
    }
