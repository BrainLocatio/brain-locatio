class Solution:
    @staticmethod
    def search_insert(nums: list[int], target: int) -> int:
        """
        Iterative Binary Search Approach

        :param nums: a sorted array of distinct integers
        :param target: value to be found
        :return: int: return the index if the target is found. If not, return the index where it would be if it were inserted in order.
        """
        if target > nums[-1]:
            return len(nums)

        if target < nums[0]:
            return 0

        low_index, high_index = 0, len(nums) - 1

        while low_index <= high_index:
            mid_index = (low_index + high_index) // 2

            if nums[mid_index] == target:
                return mid_index
            elif target < nums[mid_index]:
                high_index = mid_index - 1
            else:
                low_index = mid_index + 1

        return low_index
