class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(lambda: inf)
        s = 0
        maxSum = float("-inf")

        for num in nums:
            s += num
            dif = num - k
            difNeg = num + k

            if dif in prefix:
                maxSum = max(maxSum, s - prefix[dif])
            
            if difNeg in prefix:
                maxSum = max(maxSum, s - prefix[difNeg])

            prefix[num] = min(prefix[num], s - num)

        return maxSum if maxSum != float("-inf") else 0
