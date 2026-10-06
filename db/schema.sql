CREATE TABLE doctors (
    id BIGSERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    spec TEXT NOT NULL,
    cabinet TEXT,
    active BOOLEAN DEFAULT TRUE
);

CREATE TABLE patients (
    id BIGSERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    birth DATE,
    phone TEXT,
    policy TEXT UNIQUE
);

CREATE TABLE slots (
    id BIGSERIAL PRIMARY KEY,
    doctor_id BIGINT REFERENCES doctors(id),
    dt TIMESTAMP NOT NULL,
    duration_min INT DEFAULT 30,
    status TEXT DEFAULT 'free',
    UNIQUE(doctor_id, dt)
);

CREATE TABLE appointments (
    id BIGSERIAL PRIMARY KEY,
    slot_id BIGINT REFERENCES slots(id),
    patient_id BIGINT REFERENCES patients(id),
    status TEXT DEFAULT 'booked',
    created TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_slots_doctor ON slots(doctor_id);
CREATE INDEX idx_slots_dt ON slots(dt);
CREATE INDEX idx_app_status ON appointments(status);
