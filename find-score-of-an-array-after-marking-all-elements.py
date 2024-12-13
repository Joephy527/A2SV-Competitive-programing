class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(num, idx) for idx, num in enumerate(nums)]
        marked = set()
        score = 0

        heapify(heap)

        while heap:
            minNum, minIdx = heappop(heap)

            if minIdx not in marked:
                score += minNum

                marked.add(minIdx)
                marked.add(minIdx - 1)
                marked.add(minIdx + 1)

        return score
