class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        start = -1
        distance = 0

        for i in range(n):
            if seats[i]:
                if start == -1:
                    distance = i
                else:
                    cur = (i - start) // 2
                    distance = max(distance, cur)

                start = i

        return max(distance, n - start - 1)