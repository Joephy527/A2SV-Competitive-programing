class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        distance = [0] * n
        distance[0] = 0 if seats[0] else n
        
        for i in range(1, n):
            if seats[i]:
                continue
            
            distance[i] = distance[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if seats[i]:
                continue

            distance[i] = min(distance[i + 1] + 1, distance[i])

        if not seats[0]:
            distance[0] = max(distance[0], distance[1] + 1)

        return max(distance)