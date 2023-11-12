class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        l = r = 0
        ans = 1

        if length == 1:	return 1

        while r < length:
            while l < length - 1 and arr[l] == arr[l+1]:
                l += 1
        
            while r < length - 1 and (arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
                r += 1
        
            ans=max(ans, r - l + 1)
            l = r
            r += 1
        
        return ans
