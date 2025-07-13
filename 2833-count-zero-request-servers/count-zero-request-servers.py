class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        
        queries= sorted([(q,i) for i, q in enumerate(queries)])
        window = defaultdict(int)
        active = left = right = 0
        in_active = [0] * len(queries)

        for end, idx in queries:
            start = end - x
            
            while right < len(logs) and logs[right][1] <= end:
                window[logs[right][0]] += 1
                active += (window[logs[right][0]] == 1)
                right += 1
            
            while left < len(logs) and logs[left][1] < start:
                window[logs[left][0]] -= 1
                active -= (window[logs[left][0]] == 0)
                left += 1
            
            in_active[idx] = n - active
        
        return in_active