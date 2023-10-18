class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        av = nums[l:k]
        sum1 = sum(av)
        count = sum1
        while r < len(nums):
            sum1 = sum1 - nums[l] + nums[r]
            if sum1 > count:
                count = sum1
            l += 1
            r += 1
        return count / k
