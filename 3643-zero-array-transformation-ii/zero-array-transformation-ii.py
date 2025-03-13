class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if not sum(nums):
            return 0

        def is_sum_zero(idx):
            prefix = [0] * (len(nums) + 1)

            for i in range(idx + 1):
                l, r, val = queries[i]
                
                prefix[l] += val
                prefix[r + 1] -= val

            for i in range(1, len(prefix)):
                prefix[i] += prefix[i - 1]

            for num, val in zip(nums, prefix):
                if num > val:
                    return

            return True

        left, right = 0, len(queries) - 1

        while left <= right:
            mid = (left + right) // 2

            if is_sum_zero(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left + 1 if left < len(queries) else -1