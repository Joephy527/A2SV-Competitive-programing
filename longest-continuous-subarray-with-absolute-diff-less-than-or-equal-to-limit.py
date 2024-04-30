class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lo = deque() 
        hi = deque()
        l = 0
        
        for r, n in enumerate(nums):
            while lo and lo[-1][1] >= n:
                lo.pop()
            
            lo.append((r, n))

            while hi and hi[-1][1] <= n:
                hi.pop()
            
            hi.append((r, n))

            if hi[0][1] - lo[0][1] > limit:
                if lo[0][0] == l:
                    lo.popleft()
                
                if hi[0][0] == l:
                    hi.popleft()
                
                l += 1

        return len(nums) - l

            
