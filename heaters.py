class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        maxRadius = 0
        heaters.sort()
        
        for i in range(len(houses)):
            l, r = 0, len(heaters) - 1
            curRadius = float('inf')
            
            while l < r:
                m = (l + r) // 2
                
                if heaters[m] == houses[i]:
                    curRadius = 0
                    break
                elif heaters[m] < houses[i]:
                    curRadius = min(curRadius, abs(heaters[m] - houses[i]))
                    l = m + 1
                else:
                    curRadius = min(curRadius, abs(heaters[m] - houses[i]))
                    r = m
            
            curRadius = min(curRadius, abs(heaters[l] - houses[i]))
            maxRadius = max(maxRadius, curRadius)
        
        return maxRadius
