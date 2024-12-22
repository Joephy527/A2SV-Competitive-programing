class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        groups = [[] for _ in range(len(heights))]
        heap = []
        leftMost = [-1] * len(queries)

        for idx, query in enumerate(queries):
            l, r = sorted(query)

            if l == r or heights[r] > heights[l]:
                leftMost[idx] = r
            else:
                h = max(heights[r], heights[l])
                groups[r].append((h, idx))

        for idx, height in enumerate(heights):
            for query in groups[idx]:
                heappush(heap, query)

            while heap and heap[0][0] < height:
                _, queryIdx = heappop(heap)
                leftMost[queryIdx] = idx

        return leftMost
