import mysql.connector
from utils.database import connect_to_database

# Function to add a new course
def add_course(course_name, course_description, course_credit_hours):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Courses (course_name, course_description, course_credit_hours) VALUES (%s, %s, %s)"
            values = (course_name, course_description, course_credit_hours)
            cursor.execute(sql, values)
            connection.commit()
            print(f"Course '{course_name}' added successfully!")
        else:
            print("Failed to connect to the database.")
    except mysql.connector.Error as e:
        print(f"Error adding course: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to add an instructor
def add_instructor(instructor_name, instructor_email):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Instructors (instructor_name, instructor_email) VALUES (%s, %s)"
            values = (instructor_name, instructor_email)
            cursor.execute(sql, values)
            connection.commit()
            print(f"Instructor {instructor_name} added successfully!")
        else:
            print("Failed to connect to the database.")
    except mysql.connector.Error as e:
        print(f"Error adding instructor: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to enroll a student in a course
def enroll_student(student_id, course_id, enrollment_date, progress_status):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Enrollment (student_id, course_id, enrollment_date, progress_status) VALUES (%s, %s, %s, %s)"
            values = (student_id, course_id, enrollment_date, progress_status)
            cursor.execute(sql, values)
            connection.commit()
            print(f"Student {student_id} enrolled in Course {course_id} successfully!")
        else:
            print("Failed to connect to the database.")
    except mysql.connector.Error as e:
        print(f"Error enrolling student: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Function to create an assessment
def create_assessment(course_id, assessment_name, assessment_description, assessment_date):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO Assessments (course_id, assessment_name, assessment_description, assessment_date) VALUES (%s, %s, %s, %s)"
            values = (course_id, assessment_name, assessment_description, assessment_date)
            cursor.execute(sql, values)
            connection.commit()
            print(f"Assessment '{assessment_name}' created successfully!")
        else:
            print("Failed to connect to the database.")
    except mysql.connector.Error as e:
        print(f"Error creating assessment: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Main function to demonstrate usage
def main():
    # Example usage
    add_course('Database Management', 'Introduction to database systems', 3)
    add_instructor('John Doe', 'john.doe@example.com')
    enroll_student(101, 1, '2024-07-01', 'enrolled')
    create_assessment(1, 'Midterm Exam', 'Midterm assessment for Database Management course', '2024-07-15')

if __name__ == "__main__":
    main()
