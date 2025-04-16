class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        same, s = 0, -1
        good = 0
        
        for p in range(n):
            while same < k and s + 1 < n:
                s += 1
                same += count[nums[s]]
                count[nums[s]] += 1
            
            if same >= k:
                good += n - s
            
            count[nums[p]] -= 1
            same -= count[nums[p]]
        
        return good