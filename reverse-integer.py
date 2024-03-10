class Solution:
    def reverse(self, x: int) -> int:
        if x > -1 and x < 10:
            return x

        maxInt = 2 ** 31 - 1
        minInt = -2 ** 31

        isNegative = x < 0
        reversedInt = -1 * int(str(x)[1:][::-1]) if isNegative else int(str(x)[::-1])

        if reversedInt > maxInt or reversedInt < minInt:
            return 0

        return reversedInt
