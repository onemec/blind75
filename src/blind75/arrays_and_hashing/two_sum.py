# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Find two numbers in the list that add up to the target.

        Args:
            nums (list[int]): A list of integers.
            target (int): The target sum.

        Returns:
            list[int]: Indices of the two numbers such that they add up to the target.

        Example:
            >>> Solution.twoSum([2, 7, 11, 15], 9)
            [0, 1]
        """
        prev_seen = {}
        for i, num in enumerate(nums):
            if (diff := target - num) in prev_seen:
                return [prev_seen[diff], i]
            prev_seen[num] = i
