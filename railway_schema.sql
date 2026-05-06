CREATE TABLE IF NOT EXISTS companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255),
    job_role VARCHAR(255),
    ctc DECIMAL(10,2),
    cgpa FLOAT,
    branches VARCHAR(255),
    backlogs INT,
    deadline DATETIME,
    drive_date DATE,
    reporting_time TIME,
    venue VARCHAR(255),
    google_form_link TEXT
);

CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

INSERT IGNORE INTO admins (username, password)
VALUES ('admin', 'scrypt:32768:8:1$khjNQW718UBs7VWl$23a80b53ed5fef5e9dd72105890787ecd00e12e2ba53d35021536be6c477adf39ca0c92dd97b2038025113f1843f1ad4ef3231c36b85f7c0c24a325b682f2e09');

INSERT INTO companies
(company_name, job_role, ctc, cgpa, branches, backlogs, deadline, drive_date, reporting_time, venue, google_form_link)
VALUES
('Infosys', 'Systems Engineer', 3.60, 6.0, 'CSE,IT,ENTC', 0, '2026-05-12 23:59:00', '2026-05-18', '09:30:00', 'Main Auditorium', 'https://forms.gle/infosys123'),
('Wipro', 'Project Engineer', 3.50, 6.5, 'CSE,IT', 0, '2026-05-14 23:59:00', '2026-05-20', '10:00:00', 'Seminar Hall A', 'https://forms.gle/wipro456'),
('Accenture', 'Associate Software Engineer', 4.50, 6.5, 'CSE,IT,ENTC', 0, '2026-05-11 23:59:00', '2026-05-17', '09:00:00', 'Auditorium', 'https://forms.gle/accenture789'),
('Capgemini', 'Analyst', 4.00, 6.0, 'CSE,IT,MECH', 1, '2026-05-15 23:59:00', '2026-05-22', '09:30:00', 'Seminar Hall B', 'https://forms.gle/capgemini321'),
('Cognizant', 'Programmer Analyst Trainee', 4.25, 6.0, 'CSE,IT,ENTC', 0, '2026-05-13 23:59:00', '2026-05-19', '10:30:00', 'Main Auditorium', 'https://forms.gle/cognizant654'),
('HCLTech', 'Graduate Engineer Trainee', 3.80, 6.0, 'CSE,IT,EEE', 1, '2026-05-16 23:59:00', '2026-05-23', '09:00:00', 'Seminar Hall C', 'https://forms.gle/hcl987'),
('Tech Mahindra', 'Software Engineer', 3.25, 6.0, 'CSE,IT,ENTC', 0, '2026-05-17 23:59:00', '2026-05-25', '10:00:00', 'Auditorium', 'https://forms.gle/techm111'),
('L&T Infotech', 'Graduate Engineer Trainee', 4.20, 6.5, 'CSE,IT,MECH', 0, '2026-05-18 23:59:00', '2026-05-26', '09:30:00', 'Seminar Hall A', 'https://forms.gle/lti222'),
('Persistent Systems', 'Software Developer', 5.00, 7.0, 'CSE,IT', 0, '2026-05-19 23:59:00', '2026-05-27', '09:00:00', 'Innovation Lab', 'https://forms.gle/persistent333'),
('Zensar Technologies', 'Software Engineer', 4.00, 6.0, 'CSE,IT,ENTC', 0, '2026-05-20 23:59:00', '2026-05-28', '10:00:00', 'Seminar Hall B', 'https://forms.gle/zensar444');
