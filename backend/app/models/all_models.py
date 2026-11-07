from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    full_name = Column(String(100))
    diet_type = Column(String(50), default="normal")
    daily_calorie_goal = Column(Integer, default=2000)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Recipe(Base):
    __tablename__ = "recipes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    slug = Column(String(180), unique=True, nullable=False)
    prep_time_minutes = Column(Integer, nullable=False)
    cook_time_minutes = Column(Integer, nullable=False)
    difficulty = Column(String(20), default="Dễ")
    base_servings = Column(Integer, default=2)
    calories_per_serving = Column(Numeric(6,2), default=0)
    is_public = Column(Boolean, default=True)