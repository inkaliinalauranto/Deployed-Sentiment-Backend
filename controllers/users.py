from typing import Type

from flask import jsonify, request
from decorators.get_db_conn import get_db_conn
from decorators.init_service import init_service
from decorators.init_token_methods import init_token_methods
from dtos.users import UserResDto, UserReqDto, PasswordReqDto
from models import User
from services.user_service_base import UserServiceBase
from tools.require_user import require_user
from tools.token_methods_base import TokenMethodsBase

USER_SERVICE = "user"


@get_db_conn
@init_service(USER_SERVICE)
def get_users(service: UserServiceBase):
    try:
        require_user(request)

        users: list[Type[User]] = service.get_all()
        return jsonify([(UserResDto.model_validate(user)).dict() for user in users])
    except Exception as e:
        return jsonify({"Error": str(e)})


def get_logged_in_user():
    try:
        user: User = require_user(request, True)
        return jsonify((UserResDto.model_validate(user)).dict())
    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@get_db_conn
@init_service(USER_SERVICE)
def register(service: UserServiceBase):
    try:
        if not request.json.get("username") or not request.json.get("password"):
            return jsonify({"Error": "Invalid request body"}), 400

        # Lähde: https://vik-y.medium.com/pydantic-fast-and-pythonic-data-validation-for-your-python-applications-70fe339e4107
        parsed_input_data: UserReqDto = UserReqDto.parse_raw(request.data)

        user: User = service.create(req=parsed_input_data)

        return jsonify((UserResDto.model_validate(user)).dict()), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@get_db_conn
@init_service(USER_SERVICE)
@init_token_methods
def login(service: UserServiceBase, token_methods: TokenMethodsBase):
    try:
        if not request.json.get("username") or not request.json.get("password"):
            return jsonify({"Error": "Invalid request body"}), 400

        parsed_input_data: UserReqDto = UserReqDto.parse_raw(request.data)

        token_string = service.login(req=parsed_input_data, token=token_methods)
        return jsonify({"token": token_string})

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@get_db_conn
@init_service(USER_SERVICE)
def change_password_for_logged_in_user(service: UserServiceBase):
    try:
        logged_in_user: User = require_user(request, True)

        if not request.json.get("password"):
            return jsonify({"Error": "Invalid request body"}), 400

        parsed_input_data: PasswordReqDto = PasswordReqDto.parse_raw(request.data)

        user: User = service.change_password(parsed_input_data, logged_in_user.id)

        return jsonify((UserResDto.model_validate(user)).dict())

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@get_db_conn
@init_service(USER_SERVICE)
def remove_logged_in_user(service: UserServiceBase):
    try:
        user: User = require_user(request, True)
        service.delete(user)
        return jsonify({"Success": f"User {user.username} with the id of {user.id} removed"})
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
