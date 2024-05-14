class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(capacity) -> bool:
            current = 0
            d = 1

            for weight in weights:
                current += weight

                if current > capacity:
                    d += 1
                    current = weight
                    
                    if d > days: return

            return True

        l, r = max(weights), sum(weights)
        
        while l < r:
            m = l + (r - l) // 2 
            
            if helper(m):
                r = m
            else:
                l = m + 1
        
        return l
