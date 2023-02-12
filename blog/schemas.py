from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class Blog(BaseModel):
    title: str
    description: str


class User(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    roles: str


class ShowBlog(Blog):
    author: str
    published_date: datetime
    user_comment: List

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    roles: str
    post_id: List[ShowBlog]

    class Config:
        orm_mode = True


class FullUser(BaseModel):
    username: str
    email: str
    full_name: str


class AllUser(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str

# class AllUser(BaseModel):
#     username: str
#     email: str
#     first_name: str
#     last_name: str
#
#     @property
#     def fullname(self):
#         return f"{self.first_name} {self.last_name}"
#
#     class Config:
#         orm_mode = True


class ShowAllBlog(ShowBlog):
    post_id: int

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Comment(BaseModel):
    name: str
    body: str
    email: str


class ShowComment(BaseModel):
    post_num: int
    created_date: datetime
    name: str
    body: str

    class Config:
        orm_mode = True
