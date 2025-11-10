from Entities.models import *

def create_user_repo(session, username, hashed_password, email=''):
    user = User(username=username, password_hash=hashed_password, email=email)
    session.add(user)
    session.commit()
    return user

def get_by_id_repo(session, user_id):
    return session.query(User).get(user_id)

def get_user_by_username_repo(session, username):
    user = session.query(User).filter_by(username=username).first()
    return user

def get_user_by_email_repo(session, email):
    user = session.query(User).filter_by(email=email).first()
    return user

def update_user_repo(session, username, hashed_password, email):
    user = session.query(User).filter_by(username=username).first()
    try:
        user.username = username
        user.hashed_password = hashed_password
        user.email = email
        session.commit()
    except:
        session.rollback()
    return user

def delete_user_repo(session, user_id):
    user = session.query(User).where(User.id == user_id).first()
    session.delete(user)
    session.commit()

    if get_by_id_repo(session, user_id):
        return False
    else:
        return True