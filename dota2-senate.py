class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rad = deque()
        dire = deque()

        for i in range(n):
            if senate[i] == "R":
                rad.append(i)
            else:
                dire.append(i)

        while dire and rad:
            r, d = rad.popleft(), dire.popleft()

            if r < d:
                rad.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if rad else "Dire"
            
