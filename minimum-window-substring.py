class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        countS = defaultdict(int)
        p = have = 0
        ans = [0,0,float("inf")]

        for seek in range(len(s)):
            countS[s[seek]] += 1
            
            if s[seek] in countT and countS[s[seek]] == countT[s[seek]]:
                have += 1

            while len(countT) == have:
                if ans[2] > seek - p + 1:
                    ans = [seek + 1, p , seek - p + 1]

                countS[s[p]] -= 1
                
                if s[p] in countT and countS[s[p]] < countT[s[p]]:
                    have -= 1
                
                p += 1

        return s[ans[1]:ans[0]] if ans[2] != float("inf") else ""
