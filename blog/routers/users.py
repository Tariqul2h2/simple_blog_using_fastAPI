from fastapi import APIRouter, Depends, status
from ..schemas import User, ShowUser, AllUser
from sqlalchemy.orm import Session
from ..database import get_db
from ..internal import user
from ..auth import get_current_user
from typing import List

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)


@router.post('/sign_up', status_code=status.HTTP_201_CREATED, response_model=ShowUser)
def sign_up(users: User, db: Session = Depends(get_db)):
    return user.create_user(users, db)


@router.get('/{username}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user(username, db: Session = Depends(get_db), get_current_user: User = Depends(get_current_user)):
    return user.get_user(username, db)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[AllUser])
def get_all(db: Session = Depends(get_db), get_current_user: User = Depends(get_current_user)):
    return user.get_all_user(db)


@router.delete('/{username}')
def delete_user(username, db: Session = Depends(get_db), get_current_user: User = Depends(get_current_user)):
    return user.delete_user(username, db)
