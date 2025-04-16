class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        pair = p = good = 0
        
        for s in range(n):
            pair += count[nums[s]]
            count[nums[s]] += 1

            while pair >= k:
                good += n - s
                count[nums[p]] -= 1
                pair -= count[nums[p]]
                p += 1

        return good