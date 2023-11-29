class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passangers = [0] * (max(trip[2] for trip in trips) + 1)

        for trip in trips:
            passangers[trip[1]] += trip[0]
            passangers[trip[2]] -= trip[0]

        s = 0

        for passanger in passangers:
            s += passanger
            if s > capacity:
                return False
        
        return True
