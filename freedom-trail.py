class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        pos = defaultdict(list)
        
        for i, ch in enumerate(ring):
            pos[ch].append(i) 
        
        pos = dict(pos)
        state = [(0,0)]
        
        def cost(p, state):
            min_cost = inf
            
            for p1, c1 in state:
                d = abs(p1-p)
                cost = min(d, n-d)+c1
                if min_cost > cost:
                    min_cost = cost
        
            return min_cost

        for ch in key:
            state =[(p, cost(p, state)) for p in pos[ch]]

        return len(key) + min(cost for _, cost in state)
