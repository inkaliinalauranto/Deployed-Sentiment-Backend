from functools import wraps
from flask import jsonify, current_app

from init_db import init_db_conn


def get_db_conn(decorated_function):
    @wraps(decorated_function)
    def wrapper(*args, **kwargs):
        try:
            with init_db_conn() as conn:
                return current_app.ensure_sync(decorated_function)(conn, *args, **kwargs)
        except Exception as e:
            return jsonify({"Error": str(e)})
    return wrapper
