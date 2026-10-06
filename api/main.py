from fastapi import FastAPI
from routes import doctors, patients, slots, appointments, reports

app = FastAPI(title="Clinic API")
app.include_router(doctors.router, prefix="/doctors", tags=["doctors"])
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(slots.router, prefix="/slots", tags=["slots"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/health")
def health(): return {"status": "ok"}
