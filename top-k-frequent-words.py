class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-cnt, word) for word, cnt in count.items()]
        sortedWords = []

        heapify(heap)

        while k:
            _, word = heappop(heap)
            sortedWords.append(word)
            k -= 1

        return sortedWords
