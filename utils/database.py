# utils/database.py

import mysql.connector

# Connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="eduschema1"  # Use the new database name
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Function to execute SQL queries
def execute_query(query, values=None):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            connection.commit()
            return cursor
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
        finally:
            cursor.close()
            connection.close()

# Course Management Functions
def manage_courses():
    print("\nCourse Management Menu:")
    print("1. Add Course")
    print("2. Update Course")
    print("3. Remove Course")
    print("4. Search Courses")
    print("5. Sort Courses")
    print("6. Back to Main Menu")
    
    choice = input("\nEnter your choice: ")
    
    # Implement functionality for each choice

# Instructors Management Functions
def manage_instructors():
    print("\nInstructors Management Menu:")
    print("1. Add Instructor")
    print("2. Update Instructor")
    print("3. Remove Instructor")
    print("4. Assign Instructor to Course")
    print("5. Back to Main Menu")
    
    choice = input("\nEnter your choice: ")
    
    # Implement functionality for each choice

# Student Enrollment Functions
def manage_students():
    print("\nStudent Enrollment Menu:")
    print("1. Enroll Student in Course")
    print("2. Track Student Progress")
    print("3. Back to Main Menu")
    
    choice = input("\nEnter your choice: ")
    
    # Implement functionality for each choice

# Assessment and Grades Functions
def manage_assessments_grades():
    print("\nAssessment and Grades Menu:")
    print("1. Create Assessment")
    print("2. Manage Grades")
    print("3. Back to Main Menu")
    
    choice = input("\nEnter your choice: ")
    
    # Implement functionality for each choice
