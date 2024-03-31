class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        s = sum(cardPoints[r:])
        maxScore = s

        while r < len(cardPoints):
            s = s + cardPoints[l] - cardPoints[r]
            maxScore = max(maxScore, s)
            l += 1
            r += 1

        return maxScore
