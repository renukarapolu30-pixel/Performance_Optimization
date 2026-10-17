
import time
from original import analyze_students

students = [
    {"student_id": f"S{i}", "name": f"Student{i}",
     "department": "Biotechnology"}
    for i in range(1000)
]

marks = [
    {"student_id": f"S{i}", "marks": [80, 85, 90]}
    for i in range(1000)
]

start_time = time.perf_counter()

result = analyze_students(students, marks)

end_time = time.perf_counter()

execution_time = end_time - start_time

print("Number of students:", len(students))
print("Topper ID:", result["topper_id"])
print("Execution time:", round(execution_time, 6), "seconds")
