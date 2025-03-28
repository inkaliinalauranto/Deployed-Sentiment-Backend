from functools import wraps

from flask import request

from init_db import init_db_conn
from services.user_service_sa import UserServiceSa
from tools.token_methods_sa import TokenMethodsSa


def require_user(decorated_function):
    @wraps(decorated_function)
    def wrapper(*args, **kwargs):
        token: str | None = request.headers.get("Authorization")

        if token is None:
            raise Exception("Token not in header")

        header_parts: list[str] = token.split(" ")

        if len(header_parts) != 2:
            raise Exception("Not valid token header")

        if header_parts[0] != "Bearer":
            raise Exception("Not valid token type")

        claims: dict = TokenMethodsSa().validate_token(header_parts[1])

        with init_db_conn() as conn:
            user = UserServiceSa(conn).get_by_id(int(claims["sub"]))

        if user is None:
            raise Exception("User not found")

        return decorated_function(user, *args, **kwargs)

    return wrapper
