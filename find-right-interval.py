class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted(intervals, key=lambda x: x[0])
        ends = sorted(intervals, key=lambda x: x[1])
        startMap = {intervals[idx][0]: idx for idx in range(len(intervals))}
        startMap2 = {}
        res = []

        for end in ends:
            l, r = - 1, len(intervals)

            while l + 1 < r:
                m = (l + r) // 2
                
                if starts[m][0] < end[1]:
                    l = m
                else:
                    r = m

            if r < len(intervals):
                startMap2[end[0]] = startMap[starts[r][0]]
            else:
                l = l - 1

        for interval in intervals:
            if interval[0] in startMap2:
                res.append(startMap2[interval[0]])
            else:
                res.append(-1)

        return res
