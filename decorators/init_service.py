from functools import wraps

from flask import jsonify

from services.service_factory import init_user_service
from services.user_service_base import UserServiceBase


def init_service(name):
    def decorator(decorated_function):
        @wraps(decorated_function)
        def wrapper(conn, *args, **kwargs):
            service: None | UserServiceBase = None
            try:
                if name == "user":
                    service: UserServiceBase = init_user_service(conn)

                return decorated_function(service, *args, **kwargs)
            except Exception as e:
                return jsonify({"Error": str(e)})

        return wrapper
    return decorator
