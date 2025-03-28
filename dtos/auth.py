from pydantic import BaseModel


class UserReqDto(BaseModel):
    username: str
    password: str


class UserResDto(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True
