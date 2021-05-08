"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given a string s and t return true if its an anagram and false if not
        s = sorted(s)
        t = sorted(t)

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            if s[i] != t[i]:
                return False
        return True