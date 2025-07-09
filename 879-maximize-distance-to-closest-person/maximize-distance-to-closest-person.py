class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        distance = [0] * n

        for i in range(1, n):
            if seats[i]:
                continue

            if seats[i - 1]:
                distance[i] = 1
            else:
                if distance[i - 1]:
                    distance[i] = distance[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if seats[i]:
                continue

            if seats[i + 1]:
                distance[i] = 1
            else:
                if distance[i]:
                    distance[i] = min(distance[i], distance[i + 1] + 1)
                else:
                    distance[i] = distance[i + 1] + 1

        return max(distance)