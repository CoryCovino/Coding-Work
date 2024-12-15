// https://leetcode.com/problems/remove-duplicates-from-sorted-array

from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        int_counts: {int: int} = defaultdict(int)

        for item in reversed(nums):
            if int_counts.get(item, 0) > 0:
                nums.remove(item)
            
            int_counts[item] += 1
            
        return len(nums)

        