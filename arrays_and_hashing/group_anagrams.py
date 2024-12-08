# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_counts = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for ch in word:
                char_count[ord(ch) - ord("a")] += 1
            anagram_counts[tuple(char_count)].append(word)
        return list(anagram_counts.values())
