from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

from datetime import datetime

Base = declarative_base()


class User(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password_hash = Column(String(150), nullable=False)
    email = Column(String(50), nullable=True)
    level = Column(Integer, nullable=False, default=0)
    xp = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.now)
    image_path = Column(String(100), nullable=True)

class Campaign(Base):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(500), nullable=False)
    image_url = Column(String(120), nullable=False)
    difficulty = Column(Integer, nullable=False)
    multiplier = Column(Float, nullable=False)
    # based on difficulty setting

class Cached_Recipes(Base):
    __tablename__ = 'cached_recipes'
    id = Column(Integer, primary_key=True)
    api_id = Column(Integer, nullable=False)
    title = Column(String(50), nullable=False)
    ingredients = Column(String(500), nullable=False)
    instructions = Column(String(500), nullable=False)
    image_url = Column(String(120), nullable=False)

class Game_Sessions(Base):
    __tablename__ = 'game_sessions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    recipe_id = Column(Integer, ForeignKey('cached_recipes.id'), nullable=False)
    status = Column(Integer, nullable=False)
    timer_duration = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    completed_at = Column(DateTime, default=datetime.now)
    dish_image = Column(String(120), nullable=False)
    ai_score = Column(Float, nullable=False)

class UserScore(Base):
    __tablename__ = 'user_scores'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'), nullable=False)
    experience = Column(Float, nullable=False)
    game_score = Column(Float, nullable=False)

engine = create_engine('sqlite:///game.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db_session = Session()