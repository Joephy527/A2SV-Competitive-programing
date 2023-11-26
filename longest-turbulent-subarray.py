class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 3: return len(set(arr))
        
        p = ans = 0
        while p < len(arr) - 1 and arr[p] == arr[p + 1]:
            p += 1
        
        if p == len(arr) - 1: return 1

        sign = -1 if arr[p] > arr[p + 1] else 1

        for s in range(p + 2, len(arr)):
            if arr[s - 1] == arr[s]:
                ans = max(ans, s - p)
                p = s
                continue

            if arr[s - 1] > arr[s]:
                currSign = -1
            else:
                currSign = 1

            if currSign == sign:
                ans = max(ans, s - p)
                p = s - 1
            else:
                if s == len(arr) - 1:
                    ans = max(ans, s - p + 1)
                sign = currSign

        return ans if ans != 0 else len(set(arr))
