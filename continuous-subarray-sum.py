class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        idMap = {0: -1}
        s = 0

        for idx, num in enumerate(nums):
            s += num
            s %= k

            if s not in idMap:
                idMap[s] = idx
                
            if idx - idMap[s] >= 2:
                return True
