class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = defaultdict(int)
        included = p = 0
        substring = float("inf")
        left = right = 0

        for seek in range(len(s)):
            count_s[s[seek]] += 1
            
            if count_s[s[seek]] == count_t[s[seek]]:
                included += 1

            while included == len(count_t):
                if substring > seek - p + 1:
                    substring = seek - p + 1
                    left, right = p, seek
                
                count_s[s[p]] -= 1
                
                if count_s[s[p]] < count_t[s[p]]:
                    included -= 1

                p += 1

        return s[left:right + 1] if substring != float("inf") else ""