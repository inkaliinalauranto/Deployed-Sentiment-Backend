from typing import Type

from flask import jsonify, request
from decorators.get_db_conn import get_db_conn
from decorators.init_service import init_service
from decorators.init_token_methods import init_token_methods
from decorators.require_user import require_user
from dtos.users import UserResDto, UserReqDto
from models import User
from services.user_service_base import UserServiceBase
from tools.token_methods_base import TokenMethodsBase

USER_SERVICE = "user"
NO_SERVICE = "no"


@get_db_conn
@init_service(USER_SERVICE)
def get_user(service: UserServiceBase, user_id):
    user = service.get_by_id(user_id)
    return jsonify((UserResDto.model_validate(user)).dict())


@require_user(USER_SERVICE)
def get_users(user: User, service: UserServiceBase):
    try:
        users: list[Type[User]] = service.get_all()
        return jsonify([(UserResDto.model_validate(user)).dict() for user in users])
    except Exception as e:
        return jsonify({"Error": str(e)})


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

        #######################
        # Tuo symmetric token mielummin dekoraattorin kautta
        #######################
        token_string = service.login(req=parsed_input_data, token=token_methods)
        return jsonify({"token": token_string})

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@require_user(NO_SERVICE)
def get_account(user: User):
    try:
        return jsonify((UserResDto.model_validate(user)).dict())
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
