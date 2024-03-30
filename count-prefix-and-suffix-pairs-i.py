class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairs = 0
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                pairs += words[j].startswith(words[i]) and words[j].endswith(words[i])

        return pairs
