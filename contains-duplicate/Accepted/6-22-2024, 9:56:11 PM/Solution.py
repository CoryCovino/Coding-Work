// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output: {} = {}
        
        for item in nums:
            if item in output:
                return True
            else:
                output[item] = 1
        return False
        
        # return any([v > 1 for v in output.values()])
