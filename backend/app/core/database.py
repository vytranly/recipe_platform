import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Supabase kết nối qua pooler nên cần pool_pre_ping để tránh lỗi rớt mạng
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency để sử dụng trong các API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()