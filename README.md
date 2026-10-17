# Performance Optimization in Python Applications

## Project Overview
This project focuses on improving the performance of a Student Performance Analyzer application using Python. The original implementation is analyzed to identify performance bottlenecks, and an optimized implementation is developed to reduce execution time while maintaining the same output.

## Objectives
- Identify performance bottlenecks in Python code.
- Optimize algorithms and data structures.
- Profile program execution using `cProfile`.
- Measure execution time using `timeit`.
- Compare the original and optimized implementations.
- Verify correctness through automated unit tests.

## Technologies Used
- Python
- cProfile
- timeit
- unittest
- Git and GitHub

## Optimization Techniques
1. **Dictionary-based lookup:** Replaced repeated searches through marks records with dictionary lookups.
2. **Single-pass processing:** Combined grade and department counting into fewer iterations.
3. **Performance profiling:** Used `cProfile` to examine function execution.
4. **Benchmarking:** Compared execution times across multiple runs.
5. **Automated testing:** Checked that both implementations produce identical results.

## Performance Results

The application was benchmarked using 1,000 student records.

| Metric | Result |
|---|---:|
| Original average execution time | 0.209379 seconds |
| Optimized average execution time | 0.004076 seconds |
| Speedup | 51.37× |
| Execution time reduction | 98.05% |

*Note: Benchmark timings may vary depending on the system and execution environment.*

## Testing
Four automated tests were executed successfully:

- `test_empty_input`
- `test_missing_marks`
- `test_outputs_are_identical`
- `test_topper_is_correct`

**Test result:** All 4 tests passed.

## Project Files
- `original.py` — Original implementation
- `optimized.py` — Optimized implementation
- `compare.py` — Output comparison
- `test_app.py` — Automated
- `benchmark.py` — Execution-time benchmarking
- `profile_comparison.py` — Profiling utility
- `profile_original.txt` — Original profiling results
- `profile_optimized.txt` — Optimized profiling results
- `Performance_Optimization_Report.docx` — Detailed project report

## How to Run

Run these commands from the project directory:

- python original.py
- python optimized.py
- python compare.py
- python -m unittest -v
- python benchmark.py
- python profile_comparison.py

Use python or your configured Python executable, depending on your installation.

## Conclusion

This project demonstrates how algorithmic improvements and suitable data structures can significantly improve Python application performance. The optimized implementation achieved a measured 51.37× speedup in the benchmark while preserving the original output and passing all four automated tests.

## Author

## Renuka Rapolu
