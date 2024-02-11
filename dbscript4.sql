-- Insert user information
INSERT INTO usertable (username, user_type)
VALUES ('Shashwat Singh', 1);

INSERT INTO userinfo (user_id, fullname, user_height, user_weight, race, date_of_birth, ethnicity, sex, gender)
SELECT user_id, 'Shashwat Singh', 175, 75, 'Asian', '1990-05-15', 'Indian', 'Male', 'Male'
FROM usertable
WHERE username = 'Shashwat Singh';

-- Insert medical records
INSERT INTO notes (user_id, note, note_date, history_user_id)
SELECT user_id, 'Routine checkup, everything seems normal', DATE '2023-01-05', 1
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Follow up on previous diagnosis', DATE '2023-03-10', 2
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Prescription refill', DATE '2023-07-20', 3
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Complains of stomach ache', DATE '2023-09-15', 4
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Emergency visit due to accident', DATE '2023-11-25', 5
FROM usertable
WHERE username = 'Shashwat Singh';

INSERT INTO medicine (user_id, med_name, med_dosage, med_frequency, med_date, history_user_id)
SELECT user_id, 'Paracetamol', '500mg', 'As needed', DATE '2023-01-05', 1
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Lisinopril', '10mg', 'Once daily', DATE '2023-03-10', 2
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Metformin', '1000mg', 'Twice daily', DATE '2023-07-20', 3
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Omeprazole', '20mg', 'Once daily', DATE '2023-09-15', 4
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Ibuprofen', '400mg', 'As needed', DATE '2023-11-25', 5
FROM usertable
WHERE username = 'Shashwat Singh';

INSERT INTO vitals (user_id, vital_name, vital_value, vital_date, history_user_id)
SELECT user_id, 'Blood Pressure', '120/80 mmHg', DATE '2023-01-05', 1
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Heart Rate', '75 bpm', DATE '2023-03-10', 2
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Blood Sugar', '110 mg/dL', DATE '2023-07-20', 3
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Temperature', '98.6°F', DATE '2023-09-15', 4
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Respiratory Rate', '16 breaths/min', DATE '2023-11-25', 5
FROM usertable
WHERE username = 'Shashwat Singh';

INSERT INTO vaccine (user_id, vac_name, vac_date, history_user_id)
SELECT user_id, 'Flu Vaccine', DATE '2022-10-01', 1
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'COVID-19 Vaccine', DATE '2023-05-15', 2
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Tetanus Vaccine', DATE '2020-08-20', 3
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Hepatitis B Vaccine', DATE '2018-12-05', 4
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'MMR Vaccine', DATE '2015-06-10', 5
FROM usertable
WHERE username = 'Shashwat Singh';

INSERT INTO lab_result (user_id, lab_result, lab_date, history_user_id)
SELECT user_id, 'CBC - Within normal ranges', DATE '2023-01-05', 1
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Cholesterol - Slightly elevated', DATE '2023-03-10', 2
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'HbA1c - Within target range', DATE '2023-07-20', 3
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Liver Function - Normal', DATE '2023-09-15', 4
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Urine Analysis - No abnormalities detected', DATE '2023-11-25', 5
FROM usertable
WHERE username = 'Shashwat Singh';

INSERT INTO surgeries (user_id, surgery, surgery_date, history_user_id)
SELECT user_id, 'Appendectomy', DATE '2010-08-15', 1
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Knee Replacement', DATE '2015-03-20', 2
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Gallbladder Removal', DATE '2018-10-10', 3
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Hernia Repair', DATE '2019-05-05', 4
FROM usertable
WHERE username = 'Shashwat Singh'
UNION ALL
SELECT user_id, 'Tonsillectomy', DATE '2005-07-01', 5
FROM usertable
WHERE username = 'Shashwat Singh';

INSERT INTO emergencies (user_id, emergency_name, emergency_date, history_user_id)
SELECT user_id, 'Car Accident', DATE '2023-11-25', 5
FROM usertable
WHERE username = 'Shashwat Singh';

-- Insert symptoms with proper diag_id linkage
INSERT INTO diagnosis (user_id, diagnosis, diag_date, history_user_id)
SELECT user_id, 'Hypertension', DATE '2023-03-10', 2
FROM usertable
WHERE username = 'Shashwat Singh'
RETURNING user_id, diag_id;

INSERT INTO symptoms (user_id, diag_id, symptom, symptom_date, history_user_id)
SELECT user_id, diag_id, 'Headaches', DATE '2023-02-01', 2
FROM diagnosis
WHERE user_id = (SELECT user_id FROM usertable WHERE username = 'Shashwat Singh')
UNION ALL
SELECT user_id, diag_id, 'Dizziness', DATE '2023-02-01', 2
FROM diagnosis
WHERE user_id = (SELECT user_id FROM usertable WHERE username = 'Shashwat Singh');

INSERT INTO diagnosis (user_id, diagnosis, diag_date, history_user_id)
SELECT user_id, 'Type 2 Diabetes', DATE '2023-07-20', 3
FROM usertable
WHERE username = 'Shashwat Singh'
RETURNING user_id, diag_id;

INSERT INTO symptoms (user_id, diag_id, symptom, symptom_date, history_user_id)
SELECT user_id, diag_id, 'Frequent urination', DATE '2023-07-01', 3
FROM diagnosis
WHERE user_id = (SELECT user_id FROM usertable WHERE username = 'Shashwat Singh')
UNION ALL
SELECT user_id, diag_id, 'Fatigue', DATE '2023-07-01', 3
FROM diagnosis
WHERE user_id = (SELECT user_id FROM usertable WHERE username = 'Shashwat Singh');

INSERT INTO diagnosis (user_id, diagnosis, diag_date, history_user_id)
SELECT user_id, 'GERD', DATE '2023-09-15', 4
FROM usertable
WHERE username = 'Shashwat Singh'
RETURNING user_id, diag_id;

INSERT INTO symptoms (user_id, diag_id, symptom, symptom_date, history_user_id)
SELECT user_id, diag_id, 'Abdominal pain', DATE '2023-09-15', 4
FROM diagnosis
WHERE user_id = (SELECT user_id FROM usertable WHERE username = 'Shashwat Singh');

INSERT INTO diagnosis (user_id, diagnosis, diag_date, history_user_id)
SELECT user_id, 'Fractured Rib', DATE '2023-11-25', 5
FROM usertable
WHERE username = 'Shashwat Singh'
RETURNING user_id, diag_id;

INSERT INTO symptoms (user_id, diag_id, symptom, symptom_date, history_user_id)
SELECT user_id, diag_id, 'Chest pain', DATE '2023-11-25', 5
FROM diagnosis
WHERE user_id = (SELECT user_id FROM usertable WHERE username = 'Shashwat Singh');
