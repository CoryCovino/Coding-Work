// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x: str = str(x)
        reversed_str: str = str_x[::-1]

        return str_x == reversed_str