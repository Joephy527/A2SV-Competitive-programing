class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapify(heap)

        while heap and k:
            maxNum = -heappop(heap)
            heappush(heap, -int(sqrt(maxNum)))

            k -= 1

        return -sum(heap)
