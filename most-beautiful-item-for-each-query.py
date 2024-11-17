class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        sortedQueries = sorted([(q, i) for i, q in enumerate(queries)])
        maxBeauty = j = 0
        result = [0] * len(queries)

        for query, idx in sortedQueries:
            while j < len(items) and items[j][0] <= query:
                maxBeauty = max(maxBeauty, items[j][1])
                j += 1

            result[idx] = maxBeauty

        return result
