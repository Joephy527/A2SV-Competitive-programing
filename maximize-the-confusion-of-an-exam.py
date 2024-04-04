class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = defaultdict(int)
        p = 0

        for s in range(len(answerKey)):
            count[answerKey[s]] += 1

            if (s - p + 1) - max(count.values()) > k:
                count[answerKey[p]] -= 1
                p += 1

        return s - p + 1
