class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2: return 1

        p = sign = 0
        ans = 1

        for s in range(1, len(arr)):
            if arr[s - 1] < arr[s]:
                currSign = 1
            elif arr[s - 1] > arr[s]:
                currSign = -1
            else:
                currSign = sign

            if currSign == sign:
                p = s - 1 if arr[s - 1] != arr[s] else s

            sign = currSign
            ans = max(ans, s - p + 1)

        return ans
