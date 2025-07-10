class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        bucket = [[] for _ in range(max(count.values()) + 1)]
        top = []

        for word, cnt in count.items():
            bucket[cnt].append(word)

        for i in range(len(bucket) - 1, -1, -1):
            b = sorted(bucket[i], reverse=True)
            while b and k:
                top.append(b.pop())
                k -= 1

        return top