from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/schedule/{date}")
def schedule(date: str, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/schedule.sql').read()),
                                                 {"date": date}).fetchall()]

@router.get("/load")
def load(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/doctor_load.sql').read())).fetchall()]

@router.get("/noshows")
def noshows(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/noshows.sql').read())).fetchall()]

@router.get("/kpi")
def kpi(db: Session = Depends(get_session)):
    return dict(db.execute(text(open('sql/kpi.sql').read())).fetchone()._mapping)
