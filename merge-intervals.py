class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        nonOverlapping = []
        
        intervals.sort()

        cur = intervals[0] if intervals else 0
        
        for interval in intervals:
            if interval[0] <= cur[1]:
                cur[1] = max(interval[1], cur[1])
            else:
                nonOverlapping.append(cur)
                cur = interval

        nonOverlapping.append(cur)
        
        return nonOverlapping
