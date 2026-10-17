
import cProfile
import pstats
import io

from original import analyze_students as original_analyze
from optimized import analyze_students as optimized_analyze

students = [
    {
        "student_id": f"S{i}",
        "name": f"Student{i}",
        "department": ["Biotechnology", "Computer Science", "Chemistry"][i % 3]
    }
    for i in range(1000)
]

marks = [
    {"student_id": f"S{i}", "marks": [80, 85, 90]}
    for i in range(1000)
]


def save_profile(function, filename):
    profiler = cProfile.Profile()

    profiler.enable()
    function(students, marks)
    profiler.disable()

    output = io.StringIO()
    stats = pstats.Stats(profiler, stream=output)
    stats.sort_stats("cumulative")
    stats.print_stats(15)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(output.getvalue())

    print(f"Profile saved: {filename}")


save_profile(original_analyze, "profile_original.txt")
save_profile(optimized_analyze, "profile_optimized.txt")
