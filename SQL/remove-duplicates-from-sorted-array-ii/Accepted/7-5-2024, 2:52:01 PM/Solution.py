// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 1, 1

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
            
                if count > 2:
                    nums.pop(i)
                    i -= 1
            else:
                count = 1
            i += 1
        return len(nums)