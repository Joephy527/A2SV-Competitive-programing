class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums) + 1
        p = 0
        Sum = 0

        for s in range(len(nums)):
            if nums[s] >= target:
                return 1

            Sum += nums[s]
            while Sum >= target:
                length = min(length, s - p + 1)
                Sum -= nums[p]
                p += 1

        return length if length != len(nums) + 1 else 0
