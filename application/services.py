from Entities.DTOs import CreateUserDto, UpdateUserDto
from infrastructure.CRUD import *
from Entities.models import db_session

def create_user_ser(user_dto: CreateUserDto):
    return create_user_repo(db_session, user_dto.username, user_dto.password, user_dto.email)

def get_user_by_id_ser(user_id):
    return get_by_id_repo(db_session, user_id)

def get_user_by_username_ser(username):
    return get_user_by_username_repo(db_session, username)

def get_user_by_email_ser(email):
    return get_user_by_email_repo(db_session, email)

def update_user_ser (updated_user_dto: UpdateUserDto):
    return update_user_repo(
        session=db_session,
        username=updated_user_dto.username,
        hashed_password=updated_user_dto.password,
        email=updated_user_dto.email
    )

def delete_user_ser(user_id):
    return delete_user_repo(db_session, user_id=user_id)

def save_user_avatar_ser(user_id, path):
    return save_user_avatar_repo(
        session=db_session,
        user_id=user_id,
        path=path)

def update_user_xp_ser(user_id, xp_gain):
    return update_user_xp_repo(
        session=db_session,
        user_id=user_id,
        xp_gain=xp_gain
    )