class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res = [(r, c) for r in range(rows) for c in range(cols)]

        res.sort(key=lambda points: (abs(points[0] - rCenter) + abs(points[1] - cCenter)))

        return res
