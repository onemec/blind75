# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Return an array such that each element at index i is the product of all the numbers in the input array except nums[i].

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: A list of products, where each element is the product of all elements in the input list except the one at the same index.

        Example:
            >>> Solution().productExceptSelf([1, 2, 3, 4])
            [24, 12, 8, 6]
        """
        n = len(nums)
        result = [1] * n
        left_prod, right_prod = 1, 1

        for i in range(n - 1):
            left_prod *= nums[i]
            result[i + 1] *= left_prod
            right_prod *= nums[n - i - 1]
            result[n - i - 2] *= right_prod

        return result
