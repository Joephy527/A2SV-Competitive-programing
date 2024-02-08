class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = set()
        loses = set()
        oneTimeLoses = set()

        for winner, loser in matches:
            if loser in loses:
                oneTimeLoses.discard(loser)
            else:
                oneTimeLoses.add(loser)
            
            loses.add(loser)

            if winner not in loses:
                wins.add(winner)

            if loser in wins:
                wins.remove(loser)

        return [sorted(wins), sorted(oneTimeLoses)]
