import abc
from typing import Any


class TokenMethodsBase(abc.ABC):
    @abc.abstractmethod
    def create_token(self, payload: dict[str, Any]) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def validate_token(self, token_str) -> dict:
        raise NotImplementedError()
