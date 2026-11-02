class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # will always be in ascending order

        # iterate though looking for one of the diffs
        # diff = target - actual
        # store diff in a map
        # map the diff to the index
        seen = {}

        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return [seen[diff] + 1, i + 1]
            seen[num] = i
            