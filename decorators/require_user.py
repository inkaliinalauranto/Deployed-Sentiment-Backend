from functools import wraps

from flask import request, jsonify

from init_db import init_db_conn
from services.service_factory import init_user_service
from tools.token_methods_sa import TokenMethodsSa


def require_user(name):
    def decorator(decorated_function):
        @wraps(decorated_function)
        def wrapper(*args, **kwargs):
            try:
                token: str | None = request.headers.get("Authorization")

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
                    user_service = init_user_service(conn)

                    user = user_service.get_by_id(int(claims["sub"]))

                    if name == "user":
                        return decorated_function(user, user_service, *args, **kwargs)

                    return decorated_function(user, *args, **kwargs)
            except Exception as e:
                return jsonify({"Error": str(e)})
        return wrapper
    return decorator
