from functools import wraps
from init_db import init_db_conn


def get_db_conn(decorated_function):
    @wraps(decorated_function)
    def wrapper(*args, **kwargs):
        with init_db_conn() as conn:
            return decorated_function(conn, *args, **kwargs)
    return wrapper
