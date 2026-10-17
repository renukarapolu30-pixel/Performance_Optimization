
def analyze_students(students, marks):
    marks_by_id = {
        record["student_id"]: record["marks"]
        for record in marks
    }

    report = []
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    department_counts = {}
    topper = None

    for student in students:
        student_marks = marks_by_id.get(
            student["student_id"], []
        )

        if student_marks:
            average = sum(student_marks) / len(student_marks)
        else:
            average = 0.0

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

        row = {
            "student_id": student["student_id"],
            "name": student["name"],
            "department": student["department"],
            "average": round(average, 2),
            "grade": grade
        }

        report.append(row)

        # Count grades without scanning the report again
        grade_counts[grade] += 1

        # Count departments in the same pass
        department = student["department"]
        department_counts[department] = (
            department_counts.get(department, 0) + 1
        )

        # Track the topper while processing students
        if topper is None or row["average"] > topper["average"]:
            topper = row

    return {
        "students": report,
        "grade_counts": grade_counts,
        "department_counts": department_counts,
        "topper_id": topper["student_id"] if topper else None
    }
