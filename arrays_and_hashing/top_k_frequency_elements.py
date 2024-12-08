# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get counts of numbers: O(n)
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        # Put numbers in "buckets" based on their counts
        bucket_sorted = [[] for _ in range(len(nums) + 1)]
        for num, count in num_counts.items():
            bucket_sorted[count - 1].append(num)
        # Create the top K by looking through the buckets from most frequently occurring to least
        results = []
        for i in range(len(bucket_sorted) - 1, 0, -1):
            if bucket_sorted[i - 1]:
                for num in bucket_sorted[i - 1]:
                    results.append(num)
                    if len(results) >= k:
                        return results
