class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        prev, cur = 1, 2
        
        for i in range(3, n + 1):
            temp = cur
            cur = prev + cur
            prev = temp
        
        return cur
