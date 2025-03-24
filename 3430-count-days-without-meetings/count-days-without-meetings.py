class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev = 0
        no_meetings = 0

        for i in range(len(meetings)):
            start, end = meetings[i]

            if start - 1 > prev:
                no_meetings += start - prev - 1

            prev = max(prev, end)

        return no_meetings + days - prev