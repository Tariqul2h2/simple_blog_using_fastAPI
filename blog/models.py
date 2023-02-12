from database import Base
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Role(str):
    pass


class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    roles = Column(String)

    post_id = relationship('Blog', back_populates='creator')


class Blog(Base):
    __tablename__ = 'blog'

    post_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String, ForeignKey('users.username'))
    description = Column(String)
    published_date = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship('User', back_populates='post_id')
    user_comment = relationship("Comment", back_populates="post_related")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    name = Column(String)
    email = Column(String)
    body = Column(String)
    post_id = Column(Integer, ForeignKey("blog.post_id"))

    post_related = relationship("Blog", back_populates="user_comment")
