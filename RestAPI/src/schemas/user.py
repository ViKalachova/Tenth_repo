from pydantic import BaseModel, EmailStr, Field, PastDate, ConfigDict

from src.entity.models import Role


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=8)


class UserResponse(BaseModel):
    id: int = 1
    username: str
    email: str
    avatar: str
    role: Role
    model_config = ConfigDict(from_attributes=True)  # noqa


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = 'bearer'


class RequestEmail(BaseModel):
    email: EmailStr

