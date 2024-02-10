-- SCHEMA: public

-- DROP SCHEMA IF EXISTS public CASCADE;

CREATE SCHEMA IF NOT EXISTS public AUTHORIZATION postgres;

COMMENT ON SCHEMA public IS 'standard public schema';

GRANT ALL ON SCHEMA public TO PUBLIC;

GRANT ALL ON SCHEMA public TO postgres;

CREATE TABLE usertable (
    user_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR (32) UNIQUE NOT NULL,
    user_type SMALLINT NOT NULL
);

CREATE TABLE userpwd (
    pwd_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    pwd VARCHAR (32) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);

CREATE TABLE userinfo (
    info_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    fullname VARCHAR (32) NOT NULL,
    user_height integer NOT NULL,
    user_weight integer NOT NULL,
    race VARCHAR (32) NOT NULL,
    date_of_birth DATE NOT NULL,
    ethnicity VARCHAR(32) NOT NULL,
    sex VARCHAR(32) NOT NULL,
    gender VARCHAR(32) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);

CREATE TABLE notes (
    note_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    note VARCHAR (255) NOT NULL,
    note_date DATE NOT NULL,
    history_user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);

CREATE TABLE medicine (
    med_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    med_name VARCHAR (32) NOT NULL,
    med_dosage VARCHAR (32) NOT NULL,
    med_frequency VARCHAR (32) NOT NULL,
    med_date DATE NOT NULL,
    history_user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);

CREATE TABLE vaccine (
    vac_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    vac_name VARCHAR (32) NOT NULL,
    vac_date DATE NOT NULL,
    history_user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);

CREATE TABLE lab_result (
    lab_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    lab_result VARCHAR (2048) NOT NULL,
    lab_date DATE NOT NULL,
    history_user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);

CREATE TABLE surgeries (
    surgery_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    surgery VARCHAR (255) NOT NULL,
    surgery_date DATE NOT NULL,
    history_user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);

CREATE TABLE emergencies (
    emergency_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    emergency_name VARCHAR (255) NOT NULL,
    emergency_date DATE NOT NULL,
    history_user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);

CREATE TABLE diagnosis (
    diag_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    diagnosis VARCHAR (255) NOT NULL,
    diag_date DATE NOT NULL,
    history_user_id integer NOT NULL,
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);

CREATE TABLE symptoms (
    symptom_id serial GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id integer NOT NULL,
    diag_id integer NOT NULL,
    symptom VARCHAR (255) NOT NULL,
    symptom_date DATE NOT NULL,
    history_user_id integer NOT NULL,
    FOREIGN KEY (diag_id) REFERENCES diagnosis (diag_id),
    FOREIGN KEY (user_id) REFERENCES usertable (user_id)
);