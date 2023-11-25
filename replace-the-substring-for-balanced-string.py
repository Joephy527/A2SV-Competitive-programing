class Solution:
    def balancedString(self, s: str) -> int:
        maxAmount = len(s) // 4
        count = Counter(s)
        remove = {}
        
        for key, val in count.items():
            if val > maxAmount:
                remove[key] = val - maxAmount

        p = 0
        ans = float("inf")

        for seek in range(len(s)):
            if s[seek] in remove:
                remove[s[seek]] -= 1

                while max(remove.values()) <= 0:
                    ans = min(ans, seek - p + 1)
                    
                    if s[p] in remove:
                        remove[s[p]] += 1

                    p += 1

        return ans if ans != float("inf") else 0
