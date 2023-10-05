class Solution: 
    def select(self, arr, i):
        # code here
        idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[idx]:
                idx = j
        return idx
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            idx = self.select(arr, i)
            arr[i], arr[idx] = arr[idx], arr[i]
        return arr
