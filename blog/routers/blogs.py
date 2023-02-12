from fastapi import APIRouter, Depends, status
from schemas import Blog, ShowBlog, User
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from internal import blog
from auth import get_current_user

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ShowBlog)
def create(blogs: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.create_blog(blogs, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowBlog])
def get_all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.get_all(db)


@router.get('/{blog_id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get_id(blog_id, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.get_id(blog_id, db)


@router.delete('/{blog_id}')
def delete_blog(blog_id, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.delete_id(blog_id, db)

