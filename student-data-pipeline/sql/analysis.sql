-- 1. View all students
SELECT *
FROM students;


-- 2. View student performance
SELECT *
FROM student_performance;


-- 3. Average marks by department
SELECT
    department,
    AVG(average_marks) AS average_department_marks
FROM student_performance
GROUP BY department;


-- 4. Students with attendance below 75%
SELECT
    student_id,
    name,
    attendance_percentage
FROM student_performance
WHERE attendance_percentage < 75;


-- 5. Top performing students
SELECT
    student_id,
    name,
    average_marks,
    performance
FROM student_performance
ORDER BY average_marks DESC
LIMIT 5;


-- 6. Performance category count
SELECT
    performance,
    COUNT(*) AS student_count
FROM student_performance
GROUP BY performance;


-- 7. Department-wise student count
SELECT
    department,
    COUNT(*) AS total_students
FROM students
GROUP BY department;


-- 8. Students with both good attendance and good marks
SELECT
    student_id,
    name,
    attendance_percentage,
    average_marks,
    performance
FROM student_performance
WHERE attendance_percentage >= 75
AND average_marks >= 70;