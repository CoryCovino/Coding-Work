// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output = set()
        
        for item in nums:
            if item in output:
                return True
            else:
                output.add(item)
        return False
        
        # return any([v > 1 for v in output.values()])
