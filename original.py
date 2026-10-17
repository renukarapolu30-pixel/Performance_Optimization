
def analyze_students(students, marks):
    report = []

    for student in students:
        matched_marks = None

        # Search for each student's marks
        for mark_record in marks:
            if mark_record["student_id"] == student["student_id"]:
                matched_marks = mark_record["marks"]
                break

        # Calculate average
        if matched_marks:
            average = sum(matched_marks) / len(matched_marks)
        else:
            average = 0.0

        # Assign grade
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        report.append({
            "student_id": student["student_id"],
            "name": student["name"],
            "department": student["department"],
            "average": round(average, 2),
            "grade": grade
        })

    # Count students in each grade
    grade_counts = {}

    for grade in ["A", "B", "C", "D", "F"]:
        count = 0

        for row in report:
            if row["grade"] == grade:
                count += 1

        grade_counts[grade] = count

    # Count students in each department
    department_counts = {}
    departments = []

    for row in report:
        if row["department"] not in departments:
            departments.append(row["department"])

    for department in departments:
        count = 0

        for row in report:
            if row["department"] == department:
                count += 1

        department_counts[department] = count

    # Identify topper
    topper = max(report, key=lambda row: row["average"], default=None)

    return {
    "students": report,
    "grade_counts": grade_counts,
    "department_counts": department_counts,
    "topper_id": topper["student_id"] if topper else None
}




if __name__ == "__main__":
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

    result = analyze_students(students, marks)

    print("Student Report:")
    for student in result["students"]:
        print(student)

    print("\nGrade Counts:", result["grade_counts"])
    print("Department Counts:", result["department_counts"])
    print("Topper ID:", result["topper_id"])
