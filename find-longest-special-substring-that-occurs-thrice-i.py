class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(int)
        ans = 0

        for start in range(len(s)):
            character = s[start]
            substringLength = 0
            
            for end in range(start, len(s)):
                if character == s[end]:
                    substringLength += 1
                    count[(character, substringLength)] += 1
                else:
                    break

        for (char, length), freq in count.items():
            if freq >= 3 and length > ans:
                ans = length

        return ans if ans != 0 else -1
