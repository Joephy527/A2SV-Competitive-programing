class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        queries = sorted(enumerate(queries), key=lambda query: query[1])
        active = left = right = 0
        window = [0] * (n + 1)
        in_active = [0] * len(queries)

        for idx, end in queries:
            start = end - x

            while (
                right < len(logs) and
                logs[right][1] <= end
            ):
                window[logs[right][0]] += 1
                active += (window[logs[right][0]] == 1)
                right += 1

            while (
                left < len(logs) and
                logs[left][1] < start
            ):
                window[logs[left][0]] -= 1
                active -= (window[logs[left][0]] == 0)
                left += 1

            in_active[idx] = n - active

        return in_active