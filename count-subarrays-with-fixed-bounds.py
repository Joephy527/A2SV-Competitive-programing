class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxK: int) -> int:
        subArr = 0
        badIdx = l = r = -1

        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                badIdx = i

            if num == mink:
                l = i

            if num == maxK:
                r = i

            subArr += max(0, min(l, r) - badIdx)

        return subArr
