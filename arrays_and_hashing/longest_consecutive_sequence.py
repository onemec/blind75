# https://leetcode.com/problems/longest-consecutive-sequence/
from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Find the length of the longest consecutive elements sequence in an unsorted array of integers.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            int: The length of the longest consecutive elements sequence.

        Example:
            >>> Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
            4
        """
        run_counts = defaultdict(int)
        max_length = 0

        for num in nums:
            if not run_counts[num]:
                length = run_counts[num - 1] + run_counts[num + 1] + 1
                run_counts[num] = length
                run_counts[num - run_counts[num - 1]] = length
                run_counts[num + run_counts[num + 1]] = length
                max_length = max(max_length, length)

        return max_length
