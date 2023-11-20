class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])
        dropOff = set()
        s = 0

        for i in range(len(trips)):
            s += trips[i][0]
            j = i - 1
            
            while j >= 0:
                if trips[j][2] <= trips[i][1] and j not in dropOff:
                    s -= trips[j][0]
                    dropOff.add(j)
                j -= 1

            if s > capacity: return False

        return True
