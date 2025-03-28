from typing import Type

from flask import jsonify, request
from decorators.get_db_conn import get_db_conn
from decorators.init_service import init_service
from decorators.require_user import require_user
from dtos.auth import UserResDto, UserReqDto
from models import User
from services.user_service_base import UserServiceBase
from tools.token_methods_sa import TokenMethodsSa


@get_db_conn
@init_service("user")
def get_users(service: UserServiceBase):
    users: list[Type[User]] = service.get_all()
    return jsonify([(UserResDto.model_validate(user)).dict() for user in users])


@get_db_conn
@init_service("user")
def register(service: UserServiceBase):
    try:
        input_data: bytes = request.data
        # Lähde: https://vik-y.medium.com/pydantic-fast-and-pythonic-data-validation-for-your-python-applications-70fe339e4107
        parsed_input_data: UserReqDto = UserReqDto.parse_raw(input_data)

        if not parsed_input_data.username or not parsed_input_data.password:
            return jsonify({"Error": "Invalid request body"}), 400

        user: User = service.create(req=parsed_input_data)

        return jsonify((UserResDto.model_validate(user)).dict())
    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@get_db_conn
@init_service("user")
def login(service: UserServiceBase):
    try:
        input_data: bytes = request.data
        parsed_input_data: UserReqDto = UserReqDto.parse_raw(input_data)

        if not parsed_input_data.username or not parsed_input_data.password:
            return jsonify({"Error": "Invalid request body"}), 400

        #######################
        # Tuo symmetric token mielummin dekoraattorin kautta
        #######################
        token_string = service.login(req=parsed_input_data, token=TokenMethodsSa())
        return jsonify({"token": token_string})

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


@require_user
def get_account(user: User):
    try:
        return jsonify((UserResDto.model_validate(user)).dict())
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
