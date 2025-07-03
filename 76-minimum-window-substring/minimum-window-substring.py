class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_s = defaultdict(int)
        count = defaultdict(int)
        p = 0
        minimum = float("inf")
        start = end = 0

        def is_substring():
            return all(
                count_s[c] >= count_t[c] for c in count_t
            )

        for seek in range(len(s)):
            count_s[s[seek]] += 1

            while p <= seek and count_s[s[p]] > count_t[s[p]]:
                count_s[s[p]] -= 1
                p += 1

            if is_substring() and minimum > seek - p + 1:
                minimum = seek - p + 1
                start, end = p, seek + 1

        return s[start:end] if minimum != float("inf") else ""