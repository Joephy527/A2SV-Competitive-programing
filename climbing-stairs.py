class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        one = 1
        two = 1
        total = 0

        for i in range(n-1):
            total = one + two
            two = one
            one = total

        return total
