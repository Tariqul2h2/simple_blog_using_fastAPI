from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..schemas import User
from ..hashpass import Hash


def create_user(users: User, db: Session):
    new_user = models.User(
        username=users.username,
        password=Hash.bcrypt(users.password),
        first_name=users.first_name,
        last_name=users.last_name,
        email=users.email,
        roles=users.roles)
    search_user = db.query(models.User).filter(models.User.username == new_user.username).first()
    if search_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'Message': f'User {new_user.username} is already registered'})
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(username, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'Message': f'User {username} is not available'})
    return user


def get_all_user(db: Session):
    users = db.query(models.User).all()
    return users


def delete_user(username, db: Session):
    user = db.query(models.User).filter(models.User.username == username).delete(synchronize_session=False)
    db.query(models.Blog).filter(models.Blog.author == username).delete(synchronize_session=False)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            'Message': f'User {username} is not available'})
    else:
        db.commit()
        return {'Message': f'User {username} is deleted'}
