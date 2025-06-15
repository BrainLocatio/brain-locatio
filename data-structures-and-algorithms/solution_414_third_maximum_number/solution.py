class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))

        first = second = third = float("-inf")

        for num in nums:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                third = second
                second = num
            elif second > num > third:
                third = num

        return third if third != float("-inf") else first  # type: ignore
