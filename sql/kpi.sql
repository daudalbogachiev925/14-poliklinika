SELECT
    COUNT(*) AS total_appointments,
    COUNT(*) FILTER (WHERE status='done') AS done,
    COUNT(*) FILTER (WHERE status='no_show') AS no_shows,
    COUNT(*) FILTER (WHERE status='booked') AS future
FROM appointments
WHERE created >= NOW() - INTERVAL '30 days';
