# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array using binary search.

        Args:
            nums (List[int]): The rotated sorted array of integers.
            target (int): The integer value to search for.

        Returns:
            int: The index of the target value if found, otherwise -1.

        Example:
            >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
            4
            >>> Solution().search([4, 5, 6, 7, 0, 1, 2], 3)
            -1
            >>> Solution().search([1], 0)
            -1
        """
        l_index = 0
        r_index = len(nums) - 1
        while l_index <= r_index:
            mid_index = (l_index + r_index) // 2
            if target == nums[mid_index]:
                return mid_index
            if nums[l_index] <= nums[mid_index]:
                if nums[l_index] <= target < nums[mid_index]:
                    r_index = mid_index - 1
                else:
                    l_index = mid_index + 1
            else:
                if nums[mid_index] < target <= nums[r_index]:
                    l_index = mid_index + 1
                else:
                    r_index = mid_index - 1
        return -1
