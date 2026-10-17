
import unittest

from original import analyze_students as original_analyze
from optimized import analyze_students as optimized_analyze


class TestStudentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.students = [
            {"student_id": "S1", "name": "Ravi",
             "department": "Biotechnology"},
            {"student_id": "S2", "name": "Priya",
             "department": "Computer Science"},
        ]

        self.marks = [
            {"student_id": "S1", "marks": [85, 90, 88]},
            {"student_id": "S2", "marks": [95, 92, 98]},
        ]

    def test_outputs_are_identical(self):
        original = original_analyze(self.students, self.marks)
        optimized = optimized_analyze(self.students, self.marks)
        self.assertEqual(original, optimized)

    def test_topper_is_correct(self):
        result = optimized_analyze(self.students, self.marks)
        self.assertEqual(result["topper_id"], "S2")

    def test_empty_input(self):
        self.assertEqual(
            original_analyze([], []),
            optimized_analyze([], [])
        )

    def test_missing_marks(self):
        students = [
            {"student_id": "S3", "name": "Anu",
             "department": "Biotechnology"}
        ]

        self.assertEqual(
            original_analyze(students, []),
            optimized_analyze(students, [])
        )


if __name__ == "__main__":
    unittest.main()
