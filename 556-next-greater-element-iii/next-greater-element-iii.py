class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(map(int, str(n)))
        n = len(digits)
        pivot = -1

        for i in range(n - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pivot = i

                break

        if pivot == -1:
            return -1

        for i in range(n - 1, -1, -1):
            if digits[i] > digits[pivot]:
                digits[i], digits[pivot] = digits[pivot], digits[i]
                
                break

        l, r = pivot + 1, n  - 1

        while l < r:
            digits[l], digits[r] = digits[r], digits[l]
            l += 1
            r -= 1

        num = 0

        for digit in digits:
            num *= 10
            num += digit

        return num if num < 2 ** 31 else -1