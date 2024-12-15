// https://leetcode.com/problems/majority-element

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output = collections.Counter(nums)

        print(output)
        print(type(output))
        return max(output.keys(), key = output.get)