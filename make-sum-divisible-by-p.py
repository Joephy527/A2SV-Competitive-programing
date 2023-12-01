class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        wholeSum = sum(nums)

        if wholeSum < p: return -1

        target = wholeSum % p
        
        if target == 0: return 0

        count = defaultdict(int)
        count[0] = -1
        ans = len(nums)
        s = 0

        for i, num in enumerate(nums):
            s = (s + num) % p
            diff = (s - target) % p
            
            if diff in count:
                ans = min(ans, i - count[diff])

            count[s] = i

        return ans if ans != len(nums) else -1
