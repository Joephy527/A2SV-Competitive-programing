class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bannedSet = set(banned)
        maxIntegers = 0

        for num in range(1, n + 1):
            if num not in bannedSet:
                maxSum -= num

                if maxSum < 0:
                    break

                maxIntegers += 1

        return maxIntegers
