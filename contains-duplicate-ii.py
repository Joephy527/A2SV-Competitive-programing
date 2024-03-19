class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        valIdxMap = {}

        for idx, num in enumerate(nums):
            if (num in valIdxMap and
                abs(valIdxMap[num] - idx) <= k):
                return True

            valIdxMap[num] = idx
