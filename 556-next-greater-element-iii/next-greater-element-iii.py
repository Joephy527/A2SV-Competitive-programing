class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 12:
            return -1
        
        digits = list(str(n))
        max_int = (2 ** 31)
        pivot = -1

        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pivot = i
                break

        if pivot == -1:
            return -1

        for i in range(len(digits) - 1, -1, -1):
            if digits[pivot] < digits[i]:
                digits[pivot], digits[i] = digits[i], digits[pivot]
                break

        digits[pivot + 1:] = reversed(digits[pivot + 1:])
        num = int("".join(digits))

        return num if num < max_int else -1