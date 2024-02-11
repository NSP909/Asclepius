-- Insert user information
INSERT INTO usertable (username, user_type)
VALUES ('Charlie Wang', 1);

INSERT INTO userinfo (user_id, fullname, user_height, user_weight, race, date_of_birth, ethnicity, sex, gender)
SELECT user_id, 'Charlie Wang', 180, 80, 'Asian', '1995-10-20', 'Chinese', 'Male', 'Male'
FROM usertable
WHERE username = 'Charlie Wang';

-- Insert medical records
INSERT INTO notes (user_id, note, note_date, history_user_id)
SELECT user_id, 'Routine checkup, everything seems normal', DATE '2023-02-10', 1
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Follow up on previous diagnosis', DATE '2023-06-15', 2
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Prescription refill', DATE '2023-09-20', 3
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Complains of chest pain', DATE '2023-12-05', 4
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Emergency visit due to sudden collapse', DATE '2024-02-01', 5
FROM usertable
WHERE username = 'Charlie Wang';

INSERT INTO medicine (user_id, med_name, med_dosage, med_frequency, med_date, history_user_id)
SELECT user_id, 'Paracetamol', '500mg', 'As needed', DATE '2023-02-10', 1
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Lisinopril', '10mg', 'Once daily', DATE '2023-06-15', 2
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Metformin', '1000mg', 'Twice daily', DATE '2023-09-20', 3
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Aspirin', '81mg', 'Once daily', DATE '2023-12-05', 4
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Emergency medication', 'Varies', 'As needed', DATE '2024-02-01', 5
FROM usertable
WHERE username = 'Charlie Wang';

INSERT INTO vitals (user_id, vital_name, vital_value, vital_date, history_user_id)
SELECT user_id, 'Blood Pressure', '130/80 mmHg', DATE '2023-02-10', 1
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Heart Rate', '85 bpm', DATE '2023-06-15', 2
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Blood Sugar', '115 mg/dL', DATE '2023-09-20', 3
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Respiratory Rate', '18 breaths/min', DATE '2023-12-05', 4
FROM usertable
WHERE username = 'Charlie Wang';

INSERT INTO vaccine (user_id, vac_name, vac_date, history_user_id)
SELECT user_id, 'Flu Vaccine', DATE '2022-09-01', 1
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'COVID-19 Vaccine', DATE '2023-05-30', 2
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Tetanus Vaccine', DATE '2020-07-10', 3
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Hepatitis B Vaccine', DATE '2018-11-25', 4
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'MMR Vaccine', DATE '2015-04-10', 5
FROM usertable
WHERE username = 'Charlie Wang';

INSERT INTO lab_result (user_id, lab_result, lab_date, history_user_id)
SELECT user_id, 'CBC - Within normal ranges', DATE '2023-02-10', 1
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Cholesterol - Elevated', DATE '2023-06-15', 2
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'HbA1c - Within target range', DATE '2023-09-20', 3
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Troponin - Elevated', DATE '2023-12-05', 4
FROM usertable
WHERE username = 'Charlie Wang';

INSERT INTO surgeries (user_id, surgery, surgery_date, history_user_id)
SELECT user_id, 'Appendectomy', DATE '2012-04-20', 1
FROM usertable
WHERE username = 'Charlie Wang'
UNION ALL
SELECT user_id, 'Gallbladder Removal', DATE '2017-10-15', 2
FROM usertable
WHERE username = 'Charlie Wang';

INSERT INTO emergencies (user_id, emergency_name, emergency_date, history_user_id)
SELECT user_id, 'Sudden collapse', DATE '2024-02-01', 5
FROM usertable
WHERE username = 'Charlie Wang';

INSERT INTO diagnosis (user_id, diagnosis, diag_date, history_user_id)
SELECT user_id, 'Arrythmia', DATE '2024-02-01', 5
FROM usertable
WHERE username = 'Charlie Wang'
RETURNING user_id, diag_id;

INSERT INTO symptoms (user_id, diag_id, symptom, symptom_date, history_user_id)
SELECT user_id, diag_id, 'Chest pain', DATE '2023-12-05', 4
FROM diagnosis
WHERE user_id = (SELECT user_id FROM usertable WHERE username = 'Charlie Wang')
UNION ALL
SELECT user_id, diag_id, 'Shortness of breath', DATE '2024-02-01', 5
FROM diagnosis
WHERE user_id = (SELECT user_id FROM usertable WHERE username = 'Charlie Wang');
