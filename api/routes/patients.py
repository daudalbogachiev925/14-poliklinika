from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class PIn(BaseModel):
    full_name: str
    birth: date | None = None
    phone: str | None = None
    policy: str

@router.post("/")
def create(data: PIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO patients (full_name, birth, phone, policy)
        VALUES (:full_name,:birth,:phone,:policy) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/{patient_id}")
def get(patient_id: int, db: Session = Depends(get_session)):
    p = db.execute(text("SELECT * FROM patients WHERE id=:i"), {"i": patient_id}).fetchone()
    if not p: raise HTTPException(404)
    return dict(p._mapping)
