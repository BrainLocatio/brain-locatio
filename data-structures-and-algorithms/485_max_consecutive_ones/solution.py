class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Linear search approach

        :param nums: binary array
        :return: int: the maximum number of consecutive 1's in the array
        """
        max_consecutive: int = 0
        current_consecutive: int = 0

        for item in nums:
            if item == 1:
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
                continue

            current_consecutive = 0
        return max_consecutive
