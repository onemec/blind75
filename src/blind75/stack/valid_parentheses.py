# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string s containing only the characters '(', ')', '{', '}', '[' and ']'
        is valid. An input string is valid if:
        1. Open brackets are closed by the same type of brackets.
        2. Open brackets are closed in the correct order.

        Args:
            s (str): The input string containing the brackets.

        Returns:
            bool: True if the string is valid, False otherwise.

        Example:
            >>> Solution().isValid("()")
            True
            >>> Solution().isValid("()[]{}")
            True
            >>> Solution().isValid("(]")
            False
        """
        queue = []
        match = {"(": ")", "{": "}", "[": "]"}
        for ch in s:
            if ch in match:
                queue.append(ch)
            elif not queue or match[queue.pop()] != ch:
                return False
        return not queue
