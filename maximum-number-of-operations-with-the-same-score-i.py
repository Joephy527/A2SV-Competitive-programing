class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        s = nums[0] + nums[1]
        res = 1

        for i in range(2, len(nums) - 1, 2):
            curSum = nums[i] + nums[i + 1]

            if curSum != s:
                break

            res += 1

        return res
