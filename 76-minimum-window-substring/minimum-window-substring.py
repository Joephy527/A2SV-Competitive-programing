class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        count_t = Counter(t)
        count_s = defaultdict(int)
        p = start = 0
        end = n

        if m > n:
            return ""

        def checkChars():
            valid = 0
            
            for char, count in count_t.items():
                valid += int(count_s[char] >= count)

            return valid == len(count_t)

        for seek in range(n):
            char = s[seek]
            count_s[char] += 1

            while (
                p <= seek and
                count_s[s[p]] > count_t[s[p]]
            ):
                count_s[s[p]] -= 1
                p += 1

            if (
                checkChars() and
                end - start > seek - p
            ):
                start, end = p, seek

        return s[start:end + 1] if end < n else ""