# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determine if two strings are anagrams of each other.

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if the strings are anagrams, False otherwise.

        Example:
            >>> Solution.isAnagram("anagram", "nagaram")
            True
            >>> Solution.isAnagram("rat", "car")
            False
        """
        if len(s) != len(t):
            return False

        count = {}
        for char_s, char_t in zip(s, t):
            count[char_s] = count.get(char_s, 0) + 1
            count[char_t] = count.get(char_t, 0) - 1

        return all(val == 0 for val in count.values())
