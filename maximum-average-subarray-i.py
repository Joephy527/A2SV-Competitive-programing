class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        subArr = nums[:k]
        subArrSum = sum(subArr)
        maxSum = subArrSum

        while r < len(nums):
            subArrSum = subArrSum - nums[l] + nums[r]
            maxSum = max(maxSum, subArrSum)
            l += 1
            r += 1

        average = maxSum / k
        
        return average
