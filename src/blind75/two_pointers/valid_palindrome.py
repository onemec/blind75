# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determine if the given string is a palindrome, considering only alphanumeric characters and ignoring cases.

        Args:
            s (str): The input string to be checked.

        Returns:
            bool: True if the input string is a palindrome, False otherwise.

        Example:
            >>> Solution().isPalindrome("A man, a plan, a canal: Panama")
            True
            >>> Solution().isPalindrome("race a car")
            False
        """
        filtered = ""
        for ch in s:
            if ch.isalnum():
                filtered += ch.lower()
        return filtered == filtered[::-1]
