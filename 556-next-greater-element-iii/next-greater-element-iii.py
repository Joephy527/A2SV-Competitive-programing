class Solution:
    def nextGreaterElement(self, n: int) -> int:
        max_int = 2 ** 31
        digits = list(str(n))
        i, j = len(digits) - 2, len(digits) - 1

        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i == -1: return -1

        while j > i and digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = reversed(digits[i + 1:])

        num = int("".join(digits))

        if num >= max_int:
            return -1

        return num