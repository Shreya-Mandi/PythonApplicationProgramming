import mysql.connector

# Connect to the MySQL server
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='snehal123'
)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# Create the database
cursor.execute("CREATE DATABASE IF NOT EXISTS pes_university")
cursor.execute("USE pes_university")

# Create tables: students, faculty, courses
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        student_name VARCHAR(100),
        department VARCHAR(100),
        year INT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS faculty (
        faculty_id INT AUTO_INCREMENT PRIMARY KEY,
        faculty_name VARCHAR(100),
        department VARCHAR(100),
        designation VARCHAR(100)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INT AUTO_INCREMENT PRIMARY KEY,
        course_name VARCHAR(100),
        department VARCHAR(100),
        faculty_id INT,
        FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
    )
""")

# Insert data into tables
students_data = [
    ("John Doe", "Computer Science", 3),
    ("Jane Smith", "Electrical Engineering", 2),
    ("Alice Johnson", "Mechanical Engineering", 4),
    ("Bob Williams", "Civil Engineering", 1),
    ("Eva Davis", "Computer Science", 2)
]

faculty_data = [
    ("Prof. Anderson", "Computer Science", "Professor"),
    ("Dr. Miller", "Electrical Engineering", "Associate Professor"),
    ("Prof. Thompson", "Mechanical Engineering", "Professor"),
    ("Dr. Garcia", "Civil Engineering", "Associate Professor"),
    ("Prof. Lee", "Computer Science", "Professor")
]

courses_data = [
    ("Introduction to Programming", "Computer Science", 1),
    ("Electromagnetics", "Electrical Engineering", 2),
    ("Thermodynamics", "Mechanical Engineering", 3),
    ("Structural Analysis", "Civil Engineering", 4),
    ("Data Structures", "Computer Science", 5)
]

insert_students_query = "INSERT INTO students (student_name, department, year) VALUES (%s, %s, %s)"
insert_faculty_query = "INSERT INTO faculty (faculty_name, department, designation) VALUES (%s, %s, %s)"
insert_courses_query = "INSERT INTO courses (course_name, department, faculty_id) VALUES (%s, %s, %s)"

cursor.executemany(insert_students_query, students_data)
cursor.executemany(insert_faculty_query, faculty_data)
cursor.executemany(insert_courses_query, courses_data)

# Commit changes and close connection
db_connection.commit()
cursor.close()
db_connection.close()