# https://leetcode.com/problems/longest-repeating-character-replacement/
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given a string s and an integer k, this function finds the length of the longest substring
        that can be obtained by replacing at most k characters with any other character.

        Args:
            s (str): The input string.
            k (int): The maximum number of character replacements allowed.

        Returns:
            int: The length of the longest substring after at most k replacements.

        Example:
            >>> Solution().characterReplacement("AABABBA", 1)
            4
        """
        l_index = 0
        max_freq = 0
        best = 0
        counts = defaultdict(int)
        for r_index in range(len(s)):
            counts[s[r_index]] += 1
            max_freq = max(max_freq, counts[s[r_index]])
            if (r_index - l_index + 1 - max_freq) > k:
                counts[s[l_index]] -= 1
                l_index += 1
            best = max(best, r_index - l_index + 1)
        return best
