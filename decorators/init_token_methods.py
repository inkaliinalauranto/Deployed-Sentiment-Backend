from functools import wraps
from flask import current_app

from tools.token_methods_base import TokenMethodsBase
from tools.token_methods_sa import TokenMethodsSa


def init_token_methods(decorated_function):
    @wraps(decorated_function)
    def wrapper(service, *args, **kwargs):
        token_methods: TokenMethodsBase = TokenMethodsSa()
        return current_app.ensure_sync(decorated_function)(service, token_methods, *args, **kwargs)
    return wrapper
