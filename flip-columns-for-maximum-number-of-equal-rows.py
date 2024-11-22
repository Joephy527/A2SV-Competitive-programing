class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int)

        for row in matrix:
            hashedRow = tuple([0 if n else 1 for n in row]) if row[0] else tuple(row)
            count[hashedRow] += 1

        return max(count.values())
