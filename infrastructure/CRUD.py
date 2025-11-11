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

def update_user_xp_repo(session, user_id, xp_gain):
    user = session.query(User).filter_by(id=user_id).first()

    # Ensure xp_gain is a number, not a tuple
    if isinstance(xp_gain, (tuple, list)):
        xp_gain = xp_gain[0]  # Take first element if it's a tuple/list

    # Convert to integer to be safe
    xp_gain = int(xp_gain)

    user.xp +=  xp_gain
    session.commit()
    return user

def delete_user_repo(session, user_id):
    user = session.query(User).where(User.id == user_id).first()
    session.delete(user)
    session.commit()

    if get_by_id_repo(session, user_id):
        return False
    else:
        return True

def save_user_avatar_repo(session, user_id, path):
    user = session.query(User).where(User.id == user_id).first()
    user.image_path = path
    session.commit()

    return user