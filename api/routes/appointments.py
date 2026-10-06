from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class AIn(BaseModel):
    slot_id: int
    patient_id: int

@router.post("/book")
def book(data: AIn, db: Session = Depends(get_session)):
    slot = db.execute(text("SELECT status FROM slots WHERE id=:i FOR UPDATE"),
                      {"i": data.slot_id}).fetchone()
    if not slot: raise HTTPException(404)
    if slot[0] != 'free': raise HTTPException(400, "Слот уже занят")
    db.execute(text("""
        INSERT INTO appointments (slot_id, patient_id, status)
        VALUES (:slot_id, :patient_id, 'booked')
    """), data.dict())
    db.execute(text("UPDATE slots SET status='booked' WHERE id=:i"), {"i": data.slot_id})
    db.commit()
    return {"status": "booked"}

@router.post("/{app_id}/status")
def set_status(app_id: int, status: str, db: Session = Depends(get_session)):
    if status not in ('done','no_show','cancelled'):
        raise HTTPException(400, "Некорректный статус")
    db.execute(text("UPDATE appointments SET status=:s WHERE id=:i"),
               {"s": status, "i": app_id})
    db.execute(text("""
        UPDATE slots SET status='done'
        WHERE id = (SELECT slot_id FROM appointments WHERE id=:i) AND :s='done'
    """), {"i": app_id, "s": status})
    db.commit()
    return {"status": status}
