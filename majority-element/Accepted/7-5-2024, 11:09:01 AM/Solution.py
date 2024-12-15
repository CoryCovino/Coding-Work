// https://leetcode.com/problems/majority-element

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output: {int: int} = defaultdict(int)

        for num in nums:
            output[num] += 1

        combined_output: [] = [(v, k) for k, v in output.items() if v >= len(nums) / 2]

        combined_output.sort(reverse=True)
        
        return combined_output[0][1]