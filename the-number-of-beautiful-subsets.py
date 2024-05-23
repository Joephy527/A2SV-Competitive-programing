class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)

        def backTrack(idx):
            if idx == len(nums):
                return 1

            beautiful = backTrack(idx + 1)
            
            if not count[nums[idx] + k] and not count[nums[idx] - k]:
                count[nums[idx]] += 1
                beautiful += backTrack(idx + 1)
                count[nums[idx]] -= 1

            return beautiful

        return backTrack(0) -   1
