# https://leetcode.com/problems/minimum-window-substring/
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Given two strings s and t, this function finds the minimum window substring in s
        that contains all the characters in t, including duplicates.

        Args:
            s (str): The input string in which to find the window.
            t (str): The string containing the characters to be included in the window.

        Returns:
            str: The minimum window substring in s that contains all characters in t.
                 If no such window exists, returns an empty string.

        Example:
            >>> Solution().minWindow("ADOBECODEBANC", "ABC")
            "BANC"
        """
        l_index = 0
        needed = defaultdict(int)
        for ch in t:
            needed[ch] += 1
        found = defaultdict(int)
        cond_needed = len(needed)
        cond_matched = 0
        best_l, best_r = None, None

        for r_index in range(len(s)):
            if s[r_index] in needed:
                found[s[r_index]] += 1
                if found[s[r_index]] == needed[s[r_index]]:
                    cond_matched += 1
                while cond_matched == cond_needed:
                    if best_l is None or (r_index - l_index) < (best_r - best_l):
                        best_l, best_r = l_index, r_index
                    if s[l_index] in found:
                        found[s[l_index]] -= 1
                        if found[s[l_index]] < needed[s[l_index]]:
                            cond_matched -= 1
                    l_index += 1
        return "" if best_l is None else s[best_l : best_r + 1]
