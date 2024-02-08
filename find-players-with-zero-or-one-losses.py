class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        loses = defaultdict(int)

        for match in matches:
            wins[match[0]] += 1
            loses[match[1]] += 1

        winners, oneTimeLosers = [], []
        
        for player in wins:
            if player not in loses:
                winners.append(player)

        for player in loses:
            if loses[player] == 1:
                oneTimeLosers.append(player)

        winners.sort(), oneTimeLosers.sort()

        return [winners, oneTimeLosers]
