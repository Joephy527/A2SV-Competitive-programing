class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "": return ""

        countT = Counter(t)
        countW = {}
        l = 0
        have, need = 0, len(countT)
        res, resLen = [-l, -1], float("infinity")
        
        for r in range(len(s)):
            countW[s[r]] = 1 + countW.get(s[r], 0)
            if s[r] in countT and countW[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                countW[s[l]] -= 1
                if s[l] in countT and countW[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""
