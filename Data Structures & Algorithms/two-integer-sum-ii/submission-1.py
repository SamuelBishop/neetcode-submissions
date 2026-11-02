class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using the two pointer approach

        # start with pointers to the left and right
        # if the target is > l + r, r - 1
        # if the target is < l + r, l + 1
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif target < numbers[l] + numbers[r]:
                r -= 1
            elif target > numbers[l] + numbers[r]:
                l += 1
        return []
            