class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        runningSum = 0

        for idx, num in enumerate(chalk):
            runningSum += num

            if runningSum > k:
                return idx
