import mysql.connector

# Connect to the MySQL server
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='snehal123',
    database='pes_university'
)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# Query 1: Retrieve all student names and their departments
query1 = "SELECT student_name, department FROM students;"
cursor.execute(query1)
result1 = cursor.fetchall()
print("Query 1 - All student names and departments:")
for row in result1:
    print(row)
print()

# Query 2: Find faculty teaching in the Computer Science department
query2 = "SELECT * FROM faculty WHERE department = 'Computer Science';"
cursor.execute(query2)
result2 = cursor.fetchall()
print("Query 2 - Faculty teaching in Computer Science department:")
for row in result2:
    print(row)
print()

# Query 3: List courses offered by a particular faculty (e.g., faculty_id = 1)
query3 = "SELECT * FROM courses WHERE faculty_id = 1;"
cursor.execute(query3)
result3 = cursor.fetchall()
print("Query 3 - Courses offered by faculty with ID 1:")
for row in result3:
    print(row)
print()

# Query 4: Retrieve students in a specific department (e.g., Computer Science) and their years
query4 = "SELECT student_name, year FROM students WHERE department = 'Computer Science';"
cursor.execute(query4)
result4 = cursor.fetchall()
print("Query 4 - Students in Computer Science department and their years:")
for row in result4:
    print(row)
print()

# Query 5: Find the faculty teaching a particular course (e.g., course_id = 3)
query5 = """
    SELECT faculty.faculty_name, courses.course_name
    FROM faculty
    INNER JOIN courses ON faculty.faculty_id = courses.faculty_id
    WHERE courses.course_id = 3;
"""
cursor.execute(query5)
result5 = cursor.fetchall()
print("Query 5 - Faculty teaching course with ID 3:")
for row in result5:
    print(row)
print()

# Query 6: Count the number of students in each department
query6 = "SELECT department, COUNT(*) AS num_students FROM students GROUP BY department;"
cursor.execute(query6)
result6 = cursor.fetchall()
print("Query 6 - Number of students in each department:")
for row in result6:
    print(row)

# Close the cursor and connection
cursor.close()
db_connection.close()