// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in reversed(nums):
            if num == val:
                nums.remove(num)
        return len(nums)