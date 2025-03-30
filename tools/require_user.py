from typing import Type

from flask import Request

from init_db import init_db_conn
from models import User
from services.service_factory import init_user_service
from services.user_service_base import UserServiceBase
from tools.token_methods_sa import TokenMethodsSa


def require_user(req: Request, return_user=False) -> Type[User] | None:
    try:
        token: str | None = req.headers.get("Authorization")

        if token is None:
            raise Exception("Token not in header")

        header_parts: list[str] = token.split(" ")

        if len(header_parts) != 2:
            raise Exception("Not valid token header")

        if header_parts[0] != "Bearer":
            raise Exception("Not valid token type")

        # Validoidaan token:
        claims: dict = TokenMethodsSa().validate_token(header_parts[1])

        with init_db_conn() as conn:
            user_service: UserServiceBase = init_user_service(conn)

            user: Type[User] = user_service.get_by_id(int(claims["sub"]))

            if return_user is True:
                return user

    except Exception as e:
        raise e
