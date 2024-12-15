// https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_size: int = len(nums)
        k %= nums_size

        if k <= nums_size:
            items_to_move: [int] = nums[-k:]
            items_to_delete: [int] = nums[:-k]
            print(f"items to move: {items_to_move}")
            print(f"items to delete: {items_to_delete}")

            del nums[:-k]
            print(f"nums: {nums}")
            nums.extend(items_to_delete)
        # else:
        #     # Needs a mod here
        #     inc: int = nums_size % k
        #     print(inc)
        #     items_to_move: [int] = nums[-inc:]
        #     items_to_delete: [int] = nums[:-inc]
        #     del nums[:-inc]
        #     nums.extend(items_to_delete)
