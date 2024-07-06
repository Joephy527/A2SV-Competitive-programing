class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if (time // (n - 1)) % 2:
            return n - (time % (n - 1))
        
        return (time % (n - 1)) + 1
