class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = -1, len(citations)

        while l + 1 < r:
            m = (l + r) // 2

            if citations[m] >= len(citations) - m:
                r = m
            else:
                l = m
        
        return len(citations) - r
