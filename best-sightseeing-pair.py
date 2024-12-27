class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curMax = values[0] - 1
        score = 0

        for i in range(1, len(values)):
            score = max(score, curMax + values[i])
            curMax = max(curMax - 1, values[i] - 1)

        return score
