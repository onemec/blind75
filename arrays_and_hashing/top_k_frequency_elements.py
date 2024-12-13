# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements in the input list.

        Args:
            nums (List[int]): A list of integers.
            k (int): The number of top frequent elements to return.

        Returns:
            List[int]: A list of the k most frequent elements.

        Example:
            >>> Solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
            [1, 2]
            >>> Solution.topKFrequent([1], 1)
            [1]
        """
        # Get counts of numbers: O(n)
        num_counts = Counter(nums)
        # Put numbers in "buckets" based on their counts
        bucket_sorted = [[] for _ in range(len(nums) + 1)]
        for num, count in num_counts.items():
            bucket_sorted[count - 1].append(num)
        # Create the top K by looking through the buckets from most frequently occurring to least
        results = []
        for i in range(len(bucket_sorted) - 1, -1, -1):
            for num in bucket_sorted[i]:
                results.append(num)
                if len(results) >= k:
                    return results
