from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class SIn(BaseModel):
    doctor_id: int
    dt: datetime
    duration_min: int = 30

@router.post("/")
def create(data: SIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO slots (doctor_id, dt, duration_min)
        VALUES (:doctor_id, :dt, :duration_min) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/free")
def free_slots(doctor_id: int, date: str, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT * FROM slots
        WHERE doctor_id=:d AND status='free' AND dt::date = :date
        ORDER BY dt
    """), {"d": doctor_id, "date": date}).fetchall()]
