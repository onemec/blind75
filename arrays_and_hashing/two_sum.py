# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_seen = {}
        for i, num in enumerate(nums):
            if (diff := target - num) in prev_seen:
                return [prev_seen[diff], i]
            prev_seen[num] = i
