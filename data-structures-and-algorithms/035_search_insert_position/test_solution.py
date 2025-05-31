"""
Three Laws of TDD (Test-Driven Development)
✔ Does the test exist before the implementation? (Ensures proper TDD flow)
✔ Does the test fail before implementation? (Prevents false positives)
✔ Does the implementation only include the necessary code to pass the test? (Avoids over-engineering)

Don't forget to check:
- Missing Type hinting
- Correct Naming conventions
- if Unit Test fixtures required
- if SetUp and TearDown required
- if Parametrized tests required
- if Context Managers required
- optimization of Time & Space complexity
- SOLID principles violation
- if Refactoring required
- if Documentation/Decision-Comment required
- if Build Operate Check pattern applied
- if Test Double or Mock Object Pattern required
- if When-Given-Then convention and/or Template Method required
- if Behavior Driven Development (extends TDD) required
- F.I.R.S.T principles violation: Fast, Independent, Repeatable, Self-Validating, Timely
"""

import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()

        test_cases = [
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 2, 1),
            ([1, 2, 4, 5, 6, 7], 3, 2),
            ([1, 2, 3, 4, 5, 7], 6, 5),
            ([1, 3, 5, 6], 7, 4),
            ([4, 9, 12], 2, 0),
        ]

        for nums, target, expected_result in test_cases:
            actual_result = solution.searchInsert(nums, target)
            self.assertEqual(expected_result, actual_result)
