import sqlite3


# Connect to the database
connection = sqlite3.connect("student_performance.db")

cursor = connection.cursor()


# -----------------------------
# 1. Students
# -----------------------------

print("\n--- ALL STUDENTS ---")

cursor.execute("""
SELECT *
FROM students;
""")

for row in cursor.fetchall():
    print(row)


# -----------------------------
# 2. Average marks by department
# -----------------------------

print("\n--- AVERAGE MARKS BY DEPARTMENT ---")

cursor.execute("""
SELECT
    department,
    ROUND(AVG(average_marks), 2) AS average_department_marks
FROM student_performance
GROUP BY department;
""")

for row in cursor.fetchall():
    print(row)


# -----------------------------
# 3. Students with low attendance
# -----------------------------

print("\n--- STUDENTS WITH ATTENDANCE BELOW 75% ---")

cursor.execute("""
SELECT
    student_id,
    name,
    attendance_percentage
FROM student_performance
WHERE attendance_percentage < 75;
""")

for row in cursor.fetchall():
    print(row)


# -----------------------------
# 4. Top 5 students
# -----------------------------

print("\n--- TOP 5 STUDENTS ---")

cursor.execute("""
SELECT
    student_id,
    name,
    average_marks,
    performance
FROM student_performance
ORDER BY average_marks DESC
LIMIT 5;
""")

for row in cursor.fetchall():
    print(row)


# -----------------------------
# 5. Performance category count
# -----------------------------

print("\n--- PERFORMANCE CATEGORY COUNT ---")

cursor.execute("""
SELECT
    performance,
    COUNT(*) AS student_count
FROM student_performance
GROUP BY performance;
""")

for row in cursor.fetchall():
    print(row)


# Close database connection
connection.close()

print("\nSQL analysis completed successfully!")
#database ke against analytical queries run karta hai.