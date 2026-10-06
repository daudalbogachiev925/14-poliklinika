SELECT d.id, d.full_name, d.spec,
       COUNT(a.id) AS total,
       COUNT(a.id) FILTER (WHERE a.status='no_show') AS no_shows,
       ROUND(100.0 * COUNT(a.id) FILTER (WHERE a.status='no_show') /
             NULLIF(COUNT(a.id),0), 1) AS no_show_pct
FROM doctors d
LEFT JOIN slots s ON s.doctor_id = d.id
LEFT JOIN appointments a ON a.slot_id = s.id
GROUP BY d.id
ORDER BY no_show_pct DESC;
