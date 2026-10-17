
import time
import statistics

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


def benchmark(function, students, marks, repeats=5):
    times = []

    for _ in range(repeats):
        start = time.perf_counter()
        result = function(students, marks)
        end = time.perf_counter()

        times.append(end - start)

    return result, times


original_result, original_times = benchmark(
    original_analyze, students, marks
)

optimized_result, optimized_times = benchmark(
    optimized_analyze, students, marks
)

assert original_result == optimized_result, "Outputs do not match!"

original_avg = statistics.mean(original_times)
optimized_avg = statistics.mean(optimized_times)

improvement = (
    (original_avg - optimized_avg) / original_avg
) * 100

speedup = original_avg / optimized_avg

print("Correctness: PASS")
print("Number of students:", len(students))

print("\nOriginal timings:", original_times)
print("Original average:", round(original_avg, 6), "seconds")

print("\nOptimized timings:", optimized_times)
print("Optimized average:", round(optimized_avg, 6), "seconds")

print("\nSpeedup:", round(speedup, 2), "x")
print("Execution time reduction:", round(improvement, 2), "%")
