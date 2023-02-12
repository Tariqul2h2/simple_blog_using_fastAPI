from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///blog.db", connect_args={'check_same_thread': False})
SessionMaker = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
Base = declarative_base()


def get_db():
    db = SessionMaker()
    try:
        yield db
    finally:
        db.close()
