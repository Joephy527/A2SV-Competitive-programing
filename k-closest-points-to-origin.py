class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = []
        b = []
        for i in range(len(points)):
            distance =  math.sqrt( ( points[i][0] ) **2 + ( points[i][1] ) **2  )
            d.append([distance,points[i]])
        d.sort()
        for i in range(k):
            b.append(d[i][1])
        return b
