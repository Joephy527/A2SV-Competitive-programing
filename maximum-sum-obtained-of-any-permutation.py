class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        totalSum = [0 for _ in nums]

        for req in requests:
            totalSum[req[0]] += 1
            if req[1] != len(nums) - 1:
                totalSum[req[1] + 1] -= 1

        for idx in range(1, len(totalSum)):
            totalSum[idx] += totalSum[idx - 1]

        totalSum.sort(reverse=True)

        s = 0
        for num, ts in zip(nums, totalSum):
            s += num * ts

        return s % (10**9 + 7)
