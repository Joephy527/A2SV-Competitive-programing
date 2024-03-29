class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        p = subArr = countMax = 0

        for s in range(len(nums)):
            if nums[s] == maxNum:
                countMax += 1

            while countMax >= k:
                subArr += len(nums) - s
                
                if nums[p] == maxNum:
                    countMax -= 1

                p += 1

        return subArr
