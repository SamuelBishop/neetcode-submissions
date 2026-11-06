class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Use prefixes, store the product of everything to the left
        # Use suffixes, store the product of everything to the right
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        res = [1] * len(nums)

        # Can do it in O(n) time and O(n) space
        for i in range(1, len(nums)):
           prefixes[i] = prefixes[i - 1] * nums[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if i + 1 <= len(nums) - 1:
                suffixes[i] = suffixes[i + 1] * nums[i + 1]
            res[i] = prefixes[i] * suffixes[i]

        return res