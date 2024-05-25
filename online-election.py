class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaderHistoric = {}
        voteCounter = defaultdict(int)
        maxVotes = 0
        leader = -1

        for t, p in zip(times, persons):
            voteCounter[p] += 1
            
            if voteCounter[p] >= maxVotes:
                maxVotes = voteCounter[p]
                leader = p
            
            self.leaderHistoric[t] = leader

    def q(self, t: int) -> int:
        l, r = -1, len(self.times)

        while l + 1 < r:
            m = (l + r) // 2
            
            if self.times[m] > t:
                r = m
            else:
                l = m
        
        return self.leaderHistoric[self.times[l]]
        

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
