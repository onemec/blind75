# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of n integers, this function finds all unique triplets
        in the array which gives the sum of zero.

        Args:
            nums (List[int]): List of integers.

        Returns:
            List[List[int]]: A list of lists containing triplets that sum up to zero.

        Example:
            >>> Solution().threeSum([-1, 0, 1, 2, -1, -4])
            [[-1, -1, 2], [-1, 0, 1]]
            >>> Solution().threeSum([])
            []
        """
        nums.sort()
        results = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # If the smallest of the 3 numbers is >0, the sum can't equal 0
                break
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip duplicates
                continue
            l_index, r_index = i + 1, len(nums) - 1
            while l_index < r_index:
                sum_nums = nums[i] + nums[l_index] + nums[r_index]
                if sum_nums > 0:
                    # Reduce the sum
                    r_index -= 1
                elif sum_nums < 0:
                    # Increase the sum
                    l_index += 1
                else:
                    # Append a match
                    results.append([nums[i], nums[l_index], nums[r_index]])
                    r_index -= 1
                    l_index += 1
                    # Skip duplicates for the left pointer
                    while l_index < r_index and nums[l_index] == nums[l_index - 1]:
                        l_index += 1
        return results
