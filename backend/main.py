from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text

# Import file kết nối DB và các Model
from app.core.database import get_db, engine, Base
from app.models.all_models import User, Recipe

app = FastAPI(title="Recipe Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API Backend đã chạy thành công!"}

# ==========================================
# API TEST KẾT NỐI DATABASE SUPABASE
# ==========================================
@app.get("/api/test-db")
def test_database_connection(db: Session = Depends(get_db)):
    try:
        # 1. Test query bằng SQL thuần để đếm số lượng Users
        result = db.execute(text("SELECT COUNT(*) FROM users")).scalar()
        
        # 2. Test query bằng SQLAlchemy ORM
        users = db.query(User).limit(5).all()
        user_list = [{"id": u.id, "email": u.email, "username": u.username} for u in users]

        return {
            "status": "success",
            "message": "Kết nối Database Supabase thành công!",
            "total_users_in_db": result,
            "sample_users": user_list
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi kết nối DB: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)