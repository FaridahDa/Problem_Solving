"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # panagram contains every letter of the alphabet
        # if sentence is panagram return true
        # if sentence is not panagram return false
        # sort sentence, so it is the same as alpha
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            if char not in sentence:
                return False
        return True