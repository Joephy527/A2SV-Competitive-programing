class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        count_t = Counter(t)
        count_s = defaultdict(int)
        p = valid = start = 0
        end = n + 1

        for seek in range(n):
            char = s[seek]
            count_s[char] += 1
            
            if count_s[char] == count_t[char]:
                valid += 1

            while (
                p <= seek and
                count_s[s[p]] > count_t[s[p]]
            ):
                count_s[s[p]] -= 1
                p += 1

            if (
                valid == len(count_t) and
                end - start > seek - p
            ):
                start, end = p, seek

        return s[start:end + 1] if end != n + 1 else ""