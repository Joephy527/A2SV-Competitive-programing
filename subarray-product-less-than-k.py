class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        p = subArray = 0

        for s in range(len(nums)):
            product *= nums[s]

            while product >= k and p <= s:
                product //= nums[p]
                p += 1

            subArray += s - p + 1

        return subArray
