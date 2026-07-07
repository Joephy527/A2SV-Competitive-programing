class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        merged = [intervals[0]]
        print(intervals)

        for i in range(1, len(intervals)):
            x, y = intervals[i]

            if merged[-1][1] >= x:
                merged[-1][1] = max(merged[-1][1], y)
            else:
                merged.append([x, y])

        return merged