class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-cnt, word) for word, cnt in count.items()]

        heapify(heap)

        top = []

        while k:
            _, word = heappop(heap)
            top.append(word)
            k -= 1

        return top