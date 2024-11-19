class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        maxSum = p = subSum = 0

        for s in range(len(nums)):
            count[nums[s]] += 1
            subSum += nums[s]

            while count[nums[s]] > 1 or s - p + 1 > k:
                count[nums[p]] -= 1
                subSum -= nums[p]
                p += 1

            if s - p + 1 == k:
                maxSum = max(maxSum, subSum)

        return maxSum
