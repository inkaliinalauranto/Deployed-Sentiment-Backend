import abc
from typing import Type

from dtos.auth import UserReqDto
from models import User
from tools.token_methods_base import TokenMethodsBase


class UserServiceBase(abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> list[Type[User]]:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_id(self, user_id: int) -> Type[User]:
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, req: UserReqDto) -> User:
        raise NotImplementedError()

    @abc.abstractmethod
    def login(self, req: UserReqDto, token: TokenMethodsBase) -> str:
        raise NotImplementedError()