class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        consecutiveIntegersSum = []

        if num % 3 == 0:
            middle = num // 3
            consecutiveIntegersSum = [middle - 1, middle, middle + 1]

        return consecutiveIntegersSum
