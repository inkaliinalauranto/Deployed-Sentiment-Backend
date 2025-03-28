from sqlalchemy import Column, Integer, LargeBinary
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(Integer, nullable=False, unique=True)
    hashed_password = Column(LargeBinary, nullable=False)
