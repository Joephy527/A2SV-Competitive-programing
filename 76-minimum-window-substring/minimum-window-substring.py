class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = defaultdict(int)
        p = start = end = valid = 0
        minimum = float("inf")

        for seek in range(len(s)):
            if s[seek] in count_t:
                count_s[s[seek]] += 1
                
                if count_s[s[seek]] == count_t[s[seek]]:
                    valid += 1

            while valid == len(count_t):
                if minimum > seek - p + 1:
                    minimum = seek - p + 1
                    start, end = p, seek + 1

                if s[p] in count_t:
                    count_s[s[p]] -= 1
                    
                    if count_s[s[p]] < count_t[s[p]]:
                        valid -= 1

                p += 1

        return s[start:end] if minimum != float("inf") else ""