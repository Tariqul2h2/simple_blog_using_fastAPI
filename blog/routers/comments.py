from fastapi import APIRouter, Depends
from ..schemas import Comment
from sqlalchemy.orm import Session
from ..database import get_db
from ..internal import usercomment

router = APIRouter(
    tags=['Comment'],
    prefix='/blog'
)


@router.post("/{post_id}/comment")
def create_comment(comment: Comment, post_id: int, db: Session = Depends(get_db)):
    return usercomment.create_comment(db=db, post_id=post_id, comment=comment)
