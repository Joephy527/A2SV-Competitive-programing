class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric = 0
        
        for a in range(low, high + 1):
            if a < 100 and not a % 11:
                symmetric += 1
            elif 1000 <= a:
                left = a // 1000 + a % 1000 // 100
                right = a % 100 // 10 + a % 10
                
                if left == right:
                    symmetric += 1
        
        return symmetric