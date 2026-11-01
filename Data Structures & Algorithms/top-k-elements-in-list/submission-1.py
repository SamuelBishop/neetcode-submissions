class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a dict to store the occurrences of the nums list
        # Return the highest values

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # now somehow get back the top k
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res