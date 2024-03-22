class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        p = 0
        count = defaultdict(int)

        for s in range(len(nums)):
            count[nums[s]] += 1

            if count[0] > 1:
                count[nums[p]] -= 1
                p += 1

        return s - p
