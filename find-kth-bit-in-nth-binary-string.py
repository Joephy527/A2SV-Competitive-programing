class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n):
            if n == 1:
                return "0"
            
            previous = helper(n-1)
            inverted = "".join(reversed([ "0" if c == "1" else "1" for c in previous]))

            return previous + "1" + inverted
        
        return helper(n)[k-1]
