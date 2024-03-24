class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse=True)
        place = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        scoreRankMap = {}
        answer = []

        for i in range(len(sortedScore)):
            if i < 3:
                scoreRankMap[sortedScore[i]] = place[i]
            else:
                scoreRankMap[sortedScore[i]] = str(i + 1)

        for s in score:
            answer.append(scoreRankMap[s])

        return answer
