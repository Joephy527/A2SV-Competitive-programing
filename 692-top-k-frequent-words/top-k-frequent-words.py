class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-cnt, word) for word, cnt in count.items()]
        idx = 0
        top = [""] * k

        heapify(heap)

        while idx < k:
            _, word = heappop(heap)
            top[idx] = word
            idx += 1

        return top