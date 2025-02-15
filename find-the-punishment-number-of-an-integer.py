class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(num, target):
            if target < 0 or num < target:
                return False

            if num == target:
                return True

            return (
                can_partition(num // 10, target - num % 10) or
                can_partition(num // 100, target - num % 100) or
                can_partition(num // 1000, target - num % 1000)
            )

        punishment = 0

        for num in range(1, n + 1):
            square = num * num

            if can_partition(square, num):
                punishment += square

        return punishment
