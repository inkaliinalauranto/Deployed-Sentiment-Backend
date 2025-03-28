from functools import wraps

from decorators.get_db_conn import get_db_conn
from services.service_factory import init_user_service
from services.user_service_base import UserServiceBase


def init_service(name):
    def decorator(route_handler_function):
        @wraps(route_handler_function)
        def wrapper(conn, *args, **kwargs):
            service: None | UserServiceBase = None
            if name == "user":
                service: UserServiceBase = init_user_service(conn)

            return route_handler_function(service, *args, **kwargs)

        return wrapper

    return decorator
