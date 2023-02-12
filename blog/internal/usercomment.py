from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..schemas import Comment


def create_comment(db: Session, post_id: int, comment: Comment):
    search_post = db.query(models.Blog).filter(models.Blog.post_id == post_id).first()
    if not search_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'Message': f'Blog post id {post_id} is not available'})
    db_comment = models.Comment(post_id=post_id, **comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
