class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def is_min_zero(l, r):
            prefix = [0] * (len(nums) + 1)

            for i in range(l, r):
                start, end, val = queries[i]
                prefix[start] += val
                prefix[end + 1] -= val

            for i in range(len(nums)):
                prefix[i + 1] += prefix[i]

                if prefix[i] < nums[i]:
                    return

            return True

        left, right = 0, len(queries)
        k = -1

        while left <= right:
            mid = (left + right) // 2

            if is_min_zero(0, mid):
                k = mid
                right = mid - 1
            else:
                left = mid + 1

        return k
