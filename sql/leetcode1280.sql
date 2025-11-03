SELECT st.student_id, student_name, sb.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students AS st CROSS JOIN Subjects AS sb LEFT JOIN Examinations AS e
ON e.student_id = st.student_id AND e.subject_name = sb.subject_name
GROUP BY student_id, subject_name
ORDER BY student_id, subject_name