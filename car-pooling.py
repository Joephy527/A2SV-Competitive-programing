class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])
        dropOff = set()
        s = trips[0][0]
        
        if s > capacity: return False

        for i in range(1, len(trips)):
            j = i - 1
            while j >= 0:
                if trips[j][2] <= trips[i][1] and j not in dropOff:
                    s -= trips[j][0]
                    dropOff.add(j)
                j -= 1

            s += trips[i][0]

            if s > capacity: return False

        return True
