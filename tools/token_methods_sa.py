import os
from typing import Any

import jwt

from tools.token_methods_base import TokenMethodsBase


class TokenMethodsSa(TokenMethodsBase):
    def create_token(self, payload: dict[str, Any]) -> str:
        try:
            token = jwt.encode(payload=payload,
                               key=os.getenv("KEY"),
                               algorithm="HS512")

            return token
        except Exception:
            raise Exception("Token cannot be encoded")

    def validate_token(self, token_str) -> dict:
        try:
            claims = jwt.decode(token_str,
                                key=os.getenv("KEY"),
                                algorithms="HS512")

            return claims
        except Exception:
            raise Exception("Token cannot be decoded or it is expired")
