import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)

    # 
    def binary_search(self, l:int, r:int, nums: List[int], target: int) -> int:
        # no need for while, instead recurse down
        if l > r:
            return - 1
        idx = (l + r) // 2
        if nums[idx] == target:
            return idx
        if nums[idx] < target:
            return self.binary_search(idx + 1, r, nums, target)
        if nums[idx] > target:
            return self.binary_search(l, idx - 1, nums, target)