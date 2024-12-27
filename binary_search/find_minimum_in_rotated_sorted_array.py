# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array.

        Args:
            nums (List[int]): The input list of integers which is a rotated sorted array.

        Returns:
            int: The minimum element in the array.

        Example:
            >>> Solution().findMin([3, 4, 5, 1, 2])
            1
            >>> Solution().findMin([4, 5, 6, 7, 0, 1, 2])
            0
            >>> Solution().findMin([11, 13, 15, 17])
            11
        """
        l_index, r_index = 0, len(nums) - 1
        while l_index < r_index:
            mid_index = (l_index + r_index) // 2
            if nums[mid_index] < nums[r_index]:
                r_index = mid_index
            else:
                l_index = mid_index + 1
        return nums[l_index]
