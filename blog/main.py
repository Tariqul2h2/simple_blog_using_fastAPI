from fastapi import FastAPI
import models
from database import engine
from routers import blogs, users, login, comments

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(login.router)
app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(comments.router)
