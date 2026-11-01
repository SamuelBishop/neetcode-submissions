class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store the difference
        # Look for the difference
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i