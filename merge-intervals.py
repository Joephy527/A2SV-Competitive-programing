class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        b = []
        if len(intervals) == 0:
            return b
        intervals.sort()
        a = intervals[0]
        for i in intervals:
            if i[0] <= a[1]:
                a[1] = max(i[1], a[1])
            else:
                b.append(a)
                a = i
        b.append(a)
        return b
