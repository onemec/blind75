# https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len_s != len(t):
            return False

        count = {}
        for i in range(len_s):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1

        return not any(val != 0 for val in count.values())
