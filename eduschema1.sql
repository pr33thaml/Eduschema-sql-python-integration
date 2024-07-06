-- Create new database
CREATE DATABASE eduschema1;
USE eduschema1;

-- Create Courses table
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    course_description TEXT,
    course_credit_hours INT
    -- Add more attributes as needed
);

-- Create Instructors table
CREATE TABLE Instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    instructor_name VARCHAR(255) NOT NULL,
    instructor_email VARCHAR(255) UNIQUE
    -- Add more attributes as needed
);

-- Create Students table (assuming you have one)
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255) NOT NULL,
    student_email VARCHAR(255) UNIQUE
    -- Add more attributes as needed
);

-- Create Enrollment table
CREATE TABLE Enrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    progress_status ENUM('enrolled', 'in_progress', 'completed'),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    -- Add more attributes as needed
);

-- Create Assessments table
CREATE TABLE Assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    assessment_name VARCHAR(255) NOT NULL,
    assessment_description TEXT,
    assessment_date DATE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    -- Add more attributes as needed
);

-- Create Grades table (assuming you have one)
CREATE TABLE Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    assessment_id INT,
    student_id INT,
    grade_value DECIMAL(5, 2),
    grade_date DATE,
    FOREIGN KEY (assessment_id) REFERENCES Assessments(assessment_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
    -- Add more attributes as needed
);

-- Example: Enroll a student in a course
INSERT INTO Students (student_id, student_name, student_email)
VALUES (101, 'John Doe', 'john.doe@example.com');

SELECT * FROM Students WHERE student_id = 101;

INSERT INTO Enrollment (enrollment_id, student_id, course_id, enrollment_date, progress_status)
VALUES (1, 101, 1, '2024-07-01', 'enrolled');

SELECT * FROM Enrollment WHERE student_id = 101;

UPDATE Courses
SET course_description = 'Updated course description'
WHERE course_id = 1;

SELECT * FROM Courses WHERE course_name LIKE '%Database%';

DELETE FROM Courses
WHERE course_id = 1;

SELECT * FROM Courses ORDER BY course_name ASC;
