// https://leetcode.com/problems/contains-duplicate

from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output: {str: int} = defaultdict(int)
        for item in nums:
            output[item] += 1
        
        return any([v > 1 for v in output.values()])
