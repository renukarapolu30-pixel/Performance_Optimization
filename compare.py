
from original import analyze_students as original_analyze
from optimized import analyze_students as optimized_analyze

students = [
    {"student_id": "S1", "name": "Ravi", "department": "Biotechnology"},
    {"student_id": "S2", "name": "Priya", "department": "Computer Science"},
    {"student_id": "S3", "name": "Anu", "department": "Biotechnology"},
    {"student_id": "S4", "name": "Rahul", "department": "Chemistry"}
]

marks = [
    {"student_id": "S1", "marks": [85, 90, 88]},
    {"student_id": "S2", "marks": [95, 92, 98]},
    {"student_id": "S3", "marks": [70, 75, 72]},
    {"student_id": "S4", "marks": [35, 40, 38]}
]

original_result = original_analyze(students, marks)
optimized_result = optimized_analyze(students, marks)

if original_result == optimized_result:
    print("PASS: Both implementations produce identical output.")
else:
    print("FAIL: Outputs are different.")

print("Original topper:", original_result["topper_id"])
print("Optimized topper:", optimized_result["topper_id"])

