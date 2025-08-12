class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        ends = []
        memo = []

        def binary_search(target, ends):
            left, right = 0, len(ends)

            while left < right:
                mid = (left + right) // 2

                if ends[mid] > target:
                    right = mid
                else:
                    left = mid + 1

            return left

        for s, e, p in jobs:
            j = binary_search(s, ends) - 1
            take = p + (memo[j] if j > -1 else 0)
            skip = memo[-1] if memo else 0
            best = max(take, skip)

            memo.append(best)
            ends.append(e)

        return memo[-1] if memo else 0