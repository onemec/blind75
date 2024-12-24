# https://leetcode.com/problems/encode-and-decode-strings/
from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encode a list of strings to a single string.

        Args:
            strs (List[str]): A list of strings to be encoded.

        Returns:
            str: A single encoded string representing the list of input strings.
            The encoded format is a comma-separated list of string lengths followed by a '#' character,
            and then the concatenated original strings.

        Example:
            >>> Solution.encode(["hello", "world"])
            '5,5#helloworld'
        """
        if not strs:
            return ""
        return ",".join(str(len(s)) for s in strs) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.

        Args:
            s (str): A single encoded string representing a list of strings.
            The encoded format is a comma-separated list of string lengths followed by a '#' character,
            and then the concatenated original strings.

        Returns:
            List[str]: A list of decoded strings.

        Example:
            >>> Solution.decode('5,5#helloworld')
            ['hello', 'world']
        """
        if not s:
            return []
        i = s.find("#") + 1
        resp = []
        for num_str in s[: i - 1].split(","):
            str_len = int(num_str)
            resp.append(s[i : i + str_len])
            i += str_len
        return resp
