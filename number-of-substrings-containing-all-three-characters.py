class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = defaultdict(int)
        p = sub = 0

        for i in range(len(s)):
            count[s[i]] += 1

            while len(count) >= 3:
                sub += len(s) - i
                count[s[p]] -= 1
                
                if not count[s[p]]:
                    del count[s[p]]

                p += 1

        return sub
