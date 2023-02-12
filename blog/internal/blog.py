from fastapi import status, HTTPException
from sqlalchemy.orm import Session
import models
from schemas import Blog


def create_blog(blog: Blog, db: Session):
    # need to get the current user
    new_blog = models.Blog(title=blog.title, description=blog.description, author='tabbi')

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_id(blog_id, db: Session):
    blogs = db.query(models.Blog).filter(models.Blog.post_id == blog_id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'Message': f'Blog id {blog_id} is not available'})
    return blogs


def delete_id(blog_id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.post_id == blog_id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'Message': f'Blog id {blog_id} is not available'})
    else:
        db.commit()
        return {'Message': f'Blog id {blog_id} is deleted'}
