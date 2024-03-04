class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        increasing = True

        for i in range(n - 1):
            if increasing and arr[i] >= arr[i + 1]:
                if i == 0:
                    return False

                increasing = False
            
            if not increasing and arr[i] <= arr[i + 1]:
                return False

        return not increasing
