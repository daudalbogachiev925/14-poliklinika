SELECT d.id, d.full_name, d.spec,
       COUNT(s.id) AS total_slots,
       COUNT(s.id) FILTER (WHERE s.status='booked') AS booked,
       COUNT(s.id) FILTER (WHERE s.status='done') AS done,
       ROUND(100.0 * COUNT(s.id) FILTER (WHERE s.status IN ('booked','done')) /
             NULLIF(COUNT(s.id),0), 1) AS load_pct
FROM doctors d
LEFT JOIN slots s ON s.doctor_id = d.id
    AND s.dt >= NOW() - INTERVAL '30 days'
GROUP BY d.id
ORDER BY load_pct DESC;
