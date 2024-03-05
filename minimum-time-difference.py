class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        timePoints.sort()

        for i in range(n):
            temp = timePoints[i].split(":")
            timePoints[i] = (int(temp[0]) * 60) + int(temp[1])

        minMinutes = timePoints[0] + (24 * 60) - timePoints[-1]

        for i in range(n - 1):
            diff = timePoints[i + 1] - timePoints[i]
            minMinutes = min(minMinutes, diff)

        return minMinutes
