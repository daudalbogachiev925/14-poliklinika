SELECT s.id, d.full_name AS doctor, d.spec, s.dt, s.duration_min,
       s.status,
       p.full_name AS patient
FROM slots s
JOIN doctors d ON d.id = s.doctor_id
LEFT JOIN appointments a ON a.slot_id = s.id
LEFT JOIN patients p ON p.id = a.patient_id
WHERE s.dt::date = :date
ORDER BY s.dt;
