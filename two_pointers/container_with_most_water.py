# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Given a list of non-negative integers representing the heights of vertical lines drawn on the x-axis,
        this function calculates the maximum area of water that can be contained between two lines.

        Args:
            height (List[int]): List of non-negative integers representing the heights of the lines.

        Returns:
            int: The maximum area of water that can be contained.

        Example:
            >>> Solution().maxArea([1,8,6,2,5,4,8,3,7])
            49
            >>> Solution().maxArea([1,1])
            1
        """
        len_height = len(height)
        l_index, r_index = 0, len_height - 1
        max_area = 0
        while l_index < r_index:
            max_area = max(
                max_area, min(height[l_index], height[r_index]) * (r_index - l_index)
            )
            if height[l_index] < height[r_index]:
                l_index += 1
            else:
                r_index -= 1
        return max_area
