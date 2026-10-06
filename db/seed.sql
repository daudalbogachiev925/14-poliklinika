INSERT INTO doctors (full_name, spec, cabinet) VALUES
('Иванов И.И.','Терапевт','101'),
('Петрова П.П.','Кардиолог','205'),
('Сидоров С.С.','Невролог','310');

INSERT INTO patients (full_name, birth, phone, policy) VALUES
('Смирнов А.А.','1985-05-05','+7900','POL001'),
('Кузнецова М.И.','1990-08-15','+7901','POL002'),
('Орлов В.П.','1978-02-20','+7902','POL003');

INSERT INTO slots (doctor_id, dt) VALUES
(1,'2024-02-01 09:00'),(1,'2024-02-01 09:30'),(1,'2024-02-01 10:00'),
(2,'2024-02-01 11:00'),(2,'2024-02-01 11:30'),
(3,'2024-02-01 14:00'),(3,'2024-02-01 14:30');

INSERT INTO appointments (slot_id, patient_id, status) VALUES
(1,1,'done'),(2,2,'no_show'),(3,3,'done'),(4,1,'booked');
