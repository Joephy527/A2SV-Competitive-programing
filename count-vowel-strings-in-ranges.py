class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        vowelCount = []
        s = 0
        res = []

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                s += 1
            
            vowelCount.append(s)

        for l, r in queries:
            curVowels = vowelCount[r] - vowelCount[l - 1] if l > 0 else vowelCount[r]
            res.append(curVowels)

        return res
