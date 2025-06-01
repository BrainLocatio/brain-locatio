import unittest

from solution import Solution  # type: ignore


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()
        test_cases = [
            ([0], 0),
            ([1], 1),
            ([1, 1, 0, 1, 1, 1], 3),
            ([1, 0, 1, 1, 0, 1], 2),
        ]

        for input_value, expected_result in test_cases:
            self.assertEqual(expected_result, solution.findMaxConsecutiveOnes(input_value))
