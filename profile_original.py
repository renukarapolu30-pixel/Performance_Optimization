
import cProfile
import pstats
from original import analyze_students

students = [
    {
        "student_id": f"S{i}",
        "name": f"Student{i}",
        "department": "Biotechnology"
    }
    for i in range(1000)
]

marks = [
    {
        "student_id": f"S{i}",
        "marks": [80, 85, 90]
    }
    for i in range(1000)
]

profiler = cProfile.Profile()

profiler.enable()
analyze_students(students, marks)
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats(15)
