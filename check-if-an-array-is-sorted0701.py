class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        l = 0
        r = 1
        while r < n:
            if arr[l] > arr[r]:
                return 0
            l += 1
            r += 1
        
        return 1
