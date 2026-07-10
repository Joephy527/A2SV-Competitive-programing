class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        count_t = Counter(t)
        count_s = defaultdict(int)
        p = start = valid = 0
        end = n

        for seek in range(n):
            char = s[seek]
            count_s[char] += 1

            valid += int(count_s[char] == count_t[char])

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

        return s[start:end + 1] if end < n else ""