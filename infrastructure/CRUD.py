from sqlalchemy.testing.pickleable import User


def create_user(session, username, hashed_password, email):
    user = User(username=username, password=hashed_password, email=email)
    session.add(user)
    session.commit()
    return user

def get_by_id(session, user_id):
    return session.query(User).get(user_id)

def get_user_by_username(session, username):
    user = session.query(User).filter_by(username=username).first()
    return user

def get_user_by_email(session, email):
    user = session.query(User).filter_by(email=email).first()
    return user

def update_user(session, username, hashed_password, email):
    user = session.query(User).filter_by(username=username).first()
    try:
        user.username = username
        user.hashed_password = hashed_password
        user.email = email
        session.commit()
    except:
        session.rollback()
    return user

def delete_user(session, username):
    user = session.query(User).filter_by(username=username).first()
    session.delete(user)
    session.commit()
    return