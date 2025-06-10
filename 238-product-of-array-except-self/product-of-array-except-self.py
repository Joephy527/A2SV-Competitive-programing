class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1] * n
        prefix = suffix = 1

        for i in range(n):
            product[i] = prefix
            prefix *= nums[i]

        for i in range(n - 1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]

        return product