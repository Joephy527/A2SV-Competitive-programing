class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))

        while l <= r:
            curr = l ** 2 + r ** 2
            if curr == c:
                return True
            elif curr < c:
                l += 1
            else:
                r -= 1

        return False
        
