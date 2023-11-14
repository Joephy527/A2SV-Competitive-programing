class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        
        if target < 0 or min(nums) > x: return -1
        
        if target == 0: return len(nums)

        p = 0
        sum1 = maxWin = 0

        for s in range(len(nums)):
            sum1 += nums[s]

            while sum1 > target and p <= s:
                sum1 -= nums[p]
                p += 1

            if sum1 == target:
                maxWin = max(maxWin, s - p + 1)

        return len(nums) - maxWin
