from typing import Annotated

import sqlalchemy
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session

db_url="postgresql://postgres:amani55@localhost:5432/house"
engine=create_engine(db_url)

session_local=sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db=session_local()
    try:
        yield db
    finally:
        db.close()


db_dep=Annotated[session,Depends(get_db)]

