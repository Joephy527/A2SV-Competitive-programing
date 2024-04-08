class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        arrSum = sum(nums)
        rotations = (target // arrSum) * len(nums)
        target = target % arrSum
        
        if not target:
            return rotations
        
        s = 0
        idxMap = {0: -1}
        minSub = float("inf")

        for idx, num in enumerate(nums + nums):
            s += num
            dif = s - target

            if dif in idxMap:
                minSub = min(minSub, idx - idxMap[dif])

            idxMap[s] = idx

        return minSub + rotations if minSub != float("inf") else -1
