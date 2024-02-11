--insert new user
INSERT INTO usertable (username, user_type) VALUES ('user1', 1);
INSERT INTO usertable (username, user_type) VALUES ('user2', 2);

-- Insert into userpwd
INSERT INTO userpwd (user_id, pwd) VALUES (1, 'password1');
INSERT INTO userpwd (user_id, pwd) VALUES (2, 'password2');

-- Insert into userinfo
INSERT INTO userinfo (user_id, fullname, user_height, user_weight, race, date_of_birth, ethnicity, sex, gender) 
VALUES (1, 'John Doe', 180, 75, 'White', '1980-01-01', 'Non-Hispanic', 'Male', 'Male');
INSERT INTO userinfo (user_id, fullname, user_height, user_weight, race, date_of_birth, ethnicity, sex, gender) 
VALUES (2, 'Jane Doe', 165, 60, 'White', '1985-01-01', 'Non-Hispanic', 'Female', 'Female');

-- Insert into notes
INSERT INTO notes (user_id, note, note_date, history_user_id) VALUES (1, 'First note', '2022-01-01', 1);
INSERT INTO notes (user_id, note, note_date, history_user_id) VALUES (2, 'Second note', '2022-01-02', 2);

-- Insert into medicine
INSERT INTO medicine (user_id, med_name, med_dosage, med_frequency, med_date, history_user_id) 
VALUES (1, 'Medicine1', '1 pill', 'Once a day', '2022-01-01', 1);
INSERT INTO medicine (user_id, med_name, med_dosage, med_frequency, med_date, history_user_id) 
VALUES (2, 'Medicine2', '2 pills', 'Twice a day', '2022-01-02', 2);

--Insert into vitals
INSERT INTO vitals (user_id, vital_name, vital_value, vital_date, history_user_id) VALUES (5, 'blood pressure', 180, '2023-01-02', 5);
INSERT INTO vitals (user_id, vital_name, vital_value, vital_date, history_user_id) VALUES (6, 'blood pressure', 180, '2023-01-02', 6);

-- Insert into vaccine
INSERT INTO vaccine (user_id, vac_name, vac_date, history_user_id) VALUES (1, 'Vaccine1', '2022-01-01', 1);
INSERT INTO vaccine (user_id, vac_name, vac_date, history_user_id) VALUES (2, 'Vaccine2', '2022-01-02', 2);

-- Insert into lab_result
INSERT INTO lab_result (user_id, lab_result, lab_date, history_user_id) 
VALUES (1, 'Lab result 1', '2022-01-01', 1);
INSERT INTO lab_result (user_id, lab_result, lab_date, history_user_id) 
VALUES (2, 'Lab result 2', '2022-01-02', 2);

-- Insert into surgeries
INSERT INTO surgeries (user_id, surgery, surgery_date, history_user_id) 
VALUES (1, 'Surgery 1', '2022-01-01', 1);
INSERT INTO surgeries (user_id, surgery, surgery_date, history_user_id) 
VALUES (2, 'Surgery 2', '2022-01-02', 2);

-- Insert into emergencies
INSERT INTO emergencies (user_id, emergency_name, emergency_date, history_user_id) 
VALUES (1, 'Emergency 1', '2022-01-01', 1);
INSERT INTO emergencies (user_id, emergency_name, emergency_date, history_user_id) 
VALUES (2, 'Emergency 2', '2022-01-02', 2);

-- Insert into diagnosis
INSERT INTO diagnosis (user_id, diagnosis, diag_date, history_user_id) 
VALUES (1, 'Diagnosis 1', '2022-01-01', 1);
INSERT INTO diagnosis (user_id, diagnosis, diag_date, history_user_id) 
VALUES (2, 'Diagnosis 2', '2022-01-02', 2);

-- Insert into symptoms
INSERT INTO symptoms (user_id, diag_id, symptom, symptom_date, history_user_id) 
VALUES (1, 1, 'Symptom 1', '2022-01-01', 1);
INSERT INTO symptoms (user_id, diag_id, symptom, symptom_date, history_user_id) 
VALUES (2, 2, 'Symptom 2', '2022-01-02', 2);