class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # How would I do it as a human
        # probably sort them
        # check if the next one is one more than the last
        # if the cycle has finished set the local max to 0
        if not nums:
            return 0

        nums.sort()
        res = 1
        localMax = 1
        last = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num == last:
                continue
            if num == last + 1:
                localMax += 1
            else:
                localMax = 1
            res = max(localMax, res)
            last = num
        
        return res