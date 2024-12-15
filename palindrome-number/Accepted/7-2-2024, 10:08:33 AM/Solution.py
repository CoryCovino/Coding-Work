// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # ugly: str = str(x)
        # reversed_str: str = ugly[::-1]

        return str(x) == str(x)[::-1]