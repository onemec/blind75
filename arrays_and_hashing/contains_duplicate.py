# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the input list contains any duplicates.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            bool: True if there are duplicate integers in the list, False otherwise.

        Example:
            >>> Solution.containsDuplicate([1, 2, 3, 1])
            True
            >>> Solution.containsDuplicate([1, 2, 3, 4])
            False
        """
        return len(set(nums)) != len(nums)
