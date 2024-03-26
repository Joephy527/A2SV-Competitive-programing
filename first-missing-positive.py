class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        maxNum = max(nums)

        if maxNum < 1:
            return 1

        for num in range(1, maxNum + 2):
            if num not in uniqueNums:
                return num
