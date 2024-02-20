class Solution:
    def similarPairs(self, words: List[str]) -> int:
        uniqueWords = ["".join(sorted(set(word))) for word in words]
        pairs = 0
        uniqueWordCount = Counter(uniqueWords)

        for word in uniqueWordCount:
            for i in range(uniqueWordCount[word]):
                pairs += i

        return pairs
