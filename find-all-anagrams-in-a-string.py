class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        freqp = Counter(p)
        freqs = Counter(s[:length - 1])
        ans = []
        
        for i in range(length - 1, len(s)):
            freqs[s[i]] += 1
            if freqs == freqp:
                ans.append(i - length + 1)
            
            freqs[s[i - length + 1]] -= 1
            if freqs[s[i - length + 1]] == 0:
                del freqs[s[i - length + 1]]

        return ans
