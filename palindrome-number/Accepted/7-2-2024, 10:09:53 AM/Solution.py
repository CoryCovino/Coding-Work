// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        ugly: str = str(x)
        reversed_str: str = ugly[::-1]

        return ugly == reversed_str

        # 56 ms, 47.21%
        # 16.47, 83.26%