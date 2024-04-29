class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        
        for num in nums:
            ans ^= num
        
        ans ^= k
        op = 0
        
        while ans > 0:
            if (ans & 1) != 0:
                op += 1
        
            ans >>= 1
        
        return op
