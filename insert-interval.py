class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        
        for start, end in intervals:
            if newInterval[0] > end:
                newIntervals.append([start, end])
            elif newInterval[1] < start:
                newIntervals.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(newInterval[1], end)

        newIntervals.append(newInterval); 
        
        return newIntervals
