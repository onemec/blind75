# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, this function finds the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.

        Example:
            >>> Solution().lengthOfLongestSubstring("abcabcbb")
            3
            >>> Solution().lengthOfLongestSubstring("bbbbb")
            1
            >>> Solution().lengthOfLongestSubstring("pwwkew")
            3
        """
        left = 0
        sub_elem = set()
        best_len = 0
        for i in range(len(s)):
            if s[i] not in sub_elem:
                sub_elem.add(s[i])
                best_len = max(best_len, len(sub_elem))
            else:
                while s[left] != s[i]:
                    sub_elem.discard(s[left])
                    left += 1
                left += 1
        return best_len
