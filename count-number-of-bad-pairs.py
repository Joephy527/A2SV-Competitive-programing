class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        count = defaultdict(int)

        for i in range(len(nums)):
            slope = nums[i] - i
            bad_pairs += i - count[slope]
            count[slope] += 1

        return bad_pairs
