class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        preSum = 0

        for num in nums:
            preSum += num
            arr.append(preSum)

        return arr
