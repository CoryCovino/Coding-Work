// https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.strip_chars(s) == self.strip_chars(s[::-1])

    def strip_chars(self, s: str) -> str:
        return "".join(c.lower() for c in s if c.isalnum())
        