import pandas as pd


# -----------------------------
# 1. EXTRACT
# -----------------------------

print("Starting data pipeline...")

students = pd.read_csv("data/students.csv")
attendance = pd.read_csv("data/attendance.csv")
marks = pd.read_csv("data/marks.csv")

print("\nData extracted successfully!")

print("Students:", len(students))
print("Attendance records:", len(attendance))
print("Marks records:", len(marks))


# -----------------------------
# 2. TRANSFORM - STUDENTS
# -----------------------------

students = students.drop_duplicates()

students["name"] = students["name"].str.strip()
students["department"] = students["department"].str.strip()

print("\nStudent data cleaned.")


# -----------------------------
# 3. TRANSFORM - ATTENDANCE
# -----------------------------

attendance = attendance.drop_duplicates()

attendance["date"] = pd.to_datetime(attendance["date"])

attendance["status"] = attendance["status"].str.strip().str.title()

print("Attendance data cleaned.")


# -----------------------------
# 4. CALCULATE ATTENDANCE
# -----------------------------

attendance_summary = (
    attendance.groupby("student_id")["status"]
    .apply(lambda x: (x == "Present").sum() / len(x) * 100)
    .reset_index(name="attendance_percentage")
)

print("\nAttendance percentage calculated.")


# -----------------------------
# 5. TRANSFORM - MARKS
# -----------------------------

marks = marks.drop_duplicates()

marks["subject"] = marks["subject"].str.strip()

print("Marks data cleaned.")


# -----------------------------
# 6. CALCULATE AVERAGE MARKS
# -----------------------------

marks_summary = (
    marks.groupby("student_id")["marks"]
    .mean()
    .reset_index(name="average_marks")
)

print("Average marks calculated.")


# -----------------------------
# 7. COMBINE DATA
# -----------------------------

student_performance = students.merge(
    attendance_summary,
    on="student_id",
    how="left"
)

student_performance = student_performance.merge(
    marks_summary,
    on="student_id",
    how="left"
)


# -----------------------------
# 8. PERFORMANCE CATEGORY
# -----------------------------

def performance_category(marks):
    if marks >= 85:
        return "Excellent"
    elif marks >= 70:
        return "Good"
    elif marks >= 50:
        return "Average"
    else:
        return "Needs Improvement"


student_performance["performance"] = (
    student_performance["average_marks"]
    .apply(performance_category)
)


# -----------------------------
# 9. LOAD - SAVE CLEAN DATA
# -----------------------------

student_performance.to_csv(
    "data/student_performance.csv",
    index=False
)

print("\nPipeline completed successfully!")

print("\nFinal Student Performance Data:")
print(student_performance)

# -----------------------------
# 10. LOAD DATA INTO SQLITE
# -----------------------------

import sqlite3

connection = sqlite3.connect("student_performance.db")

students.to_sql(
    "students",
    connection,
    if_exists="replace",
    index=False
)

attendance.to_sql(
    "attendance",
    connection,
    if_exists="replace",
    index=False
)

marks.to_sql(
    "marks",
    connection,
    if_exists="replace",
    index=False
)

student_performance.to_sql(
    "student_performance",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("\nData loaded into SQLite database successfully!")
#ETL karta hai.