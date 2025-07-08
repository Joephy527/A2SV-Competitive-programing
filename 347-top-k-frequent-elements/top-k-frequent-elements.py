class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        print(count)

        for num, cnt in count.items():
            heappush(heap, (cnt, num))

            if len(heap) > k:
                heappop(heap)

        return [num for _, num in heap]