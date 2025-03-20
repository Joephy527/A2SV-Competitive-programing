class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                for j in range(3):
                    nums[i + j] = 0 if nums[j + i] else 1

                op += 1

        if not nums[-1] or not nums[-2]:
            return -1

        return op