class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        p = subArr = 0

        for s in range(len(nums)):
            count[nums[s]] += 1

            while count[nums[s]] > k:
                count[nums[p]] -= 1
                p += 1

            subArr = max(subArr, s - p + 1)

        return subArr
