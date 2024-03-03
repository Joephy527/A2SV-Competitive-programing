class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        charCount = Counter(words[0])
        duplicates = []

        for word in words:
            wordCount = Counter(word)
            for char in charCount:
                charCount[char] = min(charCount[char], wordCount[char])

        for char in charCount:
            for _ in range(charCount[char]):
                duplicates.append(char)
        
        return duplicates
