class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0

        for num in range(n + 1):
            xor ^= num

        for num in nums:
            xor ^= num

        return xor
