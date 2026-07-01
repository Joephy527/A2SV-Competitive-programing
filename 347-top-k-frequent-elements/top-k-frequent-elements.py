class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_heap = [(-c, num) for num, c in count.items()]
        top_k = []

        heapify(max_heap)

        while k:
            _, num = heappop(max_heap)
            top_k.append(num)
            k -= 1

        return top_k