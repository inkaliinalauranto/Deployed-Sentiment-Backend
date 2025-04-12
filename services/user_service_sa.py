from datetime import datetime
from typing import Type

import bcrypt
from sqlalchemy import func
from sqlalchemy.orm import Session

from dtos.users import UserReqDto, PasswordReqDto
from models import User
from services.user_service_base import UserServiceBase
from tools.token_methods_base import TokenMethodsBase


class UserServiceSa(UserServiceBase):
    def __init__(self, conn: Session):
        self.conn = conn

    def get_all(self) -> list[Type[User]]:
        users = self.conn.query(User).all()
        return users

    def get_by_id(self, user_id: int) -> User:
        user: User | None = self.conn.query(User).filter(User.id == user_id).first()

        if user is None:
            raise Exception("User not found")

        return user

    def create(self, req: UserReqDto) -> User:
        try:
            existing_username: User | None = (self.conn.query(User)
                                              .filter(func.lower(User.username) == req.username.lower())
                                              .first())

            if existing_username is not None:
                ##########################
                # Tähän jokin custom exception, jonka avulla controllerista saa
                # nostettua virheen kustomoidulla statuskoodilla
                ###########################
                raise Exception("Username already taken")

            user: User = User(username=req.username,
                              hashed_password=bcrypt.hashpw(req.password.encode("utf-8"),
                                                            bcrypt.gensalt()))

            self.conn.add(user)
            self.conn.commit()
            return user

        except Exception as e:
            self.conn.rollback()
            raise e

    def login(self, req: UserReqDto, token: TokenMethodsBase) -> str:
        try:
            user: User | None = self.conn.query(User).filter(User.username == req.username).first()

            if user is None:
                raise Exception("User not found")

            if bcrypt.checkpw(req.password.encode("utf-8"), user.hashed_password):
                return token.create_token({"sub": str(user.id),
                                           "username": user.username,
                                           "iat": datetime.now().timestamp(),
                                           "exp": datetime.now().timestamp() + (3600 * 24 * 7)})

            raise Exception("Error with login")
        except Exception as e:
            raise e

    def change_password(self, req: PasswordReqDto, user_id: int) -> User:
        try:
            user: User = self.get_by_id(user_id)

            user.hashed_password = bcrypt.hashpw(req.password.encode("utf-8"),
                                                 bcrypt.gensalt())

            self.conn.commit()
            self.conn.refresh(user)

            return user

        except Exception as e:
            self.conn.rollback()
            raise e

    def delete(self, user: User) -> None:
        try:
            self.conn.delete(user)
            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            raise e
