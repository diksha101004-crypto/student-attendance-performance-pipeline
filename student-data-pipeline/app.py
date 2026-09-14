import streamlit as st
import pandas as pd


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("data/student_performance.csv")


# -----------------------------
# TITLE
# -----------------------------

st.title("🎓 Student Attendance & Performance Dashboard")

st.write(
    "This dashboard provides insights into student attendance "
    "and academic performance."
)


# -----------------------------
# KEY METRICS
# -----------------------------

total_students = df["student_id"].nunique()
average_marks = df["average_marks"].mean()
average_attendance = df["attendance_percentage"].mean()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Students",
    total_students
)

col2.metric(
    "Average Marks",
    f"{average_marks:.2f}"
)

col3.metric(
    "Average Attendance",
    f"{average_attendance:.2f}%"
)


# -----------------------------
# PERFORMANCE DISTRIBUTION
# -----------------------------

st.subheader("📊 Performance Distribution")

performance_count = (
    df["performance"]
    .value_counts()
)

st.bar_chart(performance_count)


# -----------------------------
# DEPARTMENT PERFORMANCE
# -----------------------------

st.subheader("🏫 Department-wise Average Marks")

department_marks = (
    df.groupby("department")["average_marks"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(department_marks)


# -----------------------------
# ATTENDANCE ANALYSIS
# -----------------------------

st.subheader("📅 Student Attendance")

attendance_data = (
    df[["name", "attendance_percentage"]]
    .set_index("name")
)

st.bar_chart(attendance_data)


# -----------------------------
# TOP STUDENTS
# -----------------------------

st.subheader("🏆 Top Performing Students")

top_students = (
    df[
        [
            "student_id",
            "name",
            "department",
            "attendance_percentage",
            "average_marks",
            "performance"
        ]
    ]
    .sort_values(
        "average_marks",
        ascending=False
    )
    .head(5)
)

st.dataframe(
    top_students,
    use_container_width=True
)


# -----------------------------
# LOW ATTENDANCE STUDENTS
# -----------------------------

st.subheader("⚠️ Students with Low Attendance")

low_attendance = df[
    df["attendance_percentage"] < 75
][
    [
        "student_id",
        "name",
        "department",
        "attendance_percentage",
        "average_marks"
    ]
]

st.dataframe(
    low_attendance,
    use_container_width=True
)


# -----------------------------
# FOOTER
# -----------------------------

st.write("---")

st.caption(
    "Student Attendance & Performance Data Pipeline | "
    "Python • Pandas • SQL • SQLite • Streamlit"
)