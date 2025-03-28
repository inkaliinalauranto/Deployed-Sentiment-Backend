from sqlalchemy.orm import Session

from services.user_service_base import UserServiceBase
from services.user_service_sa import UserServiceSa


def init_user_service(conn: Session) -> UserServiceBase:
    service: UserServiceBase = UserServiceSa(conn)
    return service
