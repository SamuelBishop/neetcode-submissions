class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Just do the same forwards as backwards
        
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

        # lenS = len(s)
        # lenT = len(t)

        # if lenS != lenT:
        #     return False

        # tIndex = lenT - 1

        # for char in s:
        #     if char == t[tIndex]:
        #         tIndex -= 1
        #     if tIndex == 0:
        #         return True

        # return False