class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        idx = 0

        while 3 ** idx <= n:
            idx += 1

        while n > 0:
            power = 3 ** idx

            if power <= n:
                n -= power

            if n >= 3 ** idx:
                return False

            idx -= 1

        return n == 0
