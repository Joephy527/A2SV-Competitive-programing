class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def swap(r, l = 0):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        def select(index):
            idx = index
            for i in range(index):
                if arr[i] > arr[idx]:
                    idx = i

            return idx

        res = []

        for i in range(len(arr) - 1, -1, -1):
            idx = select(i)

            if idx == i: continue

            if idx != 0:
                swap(idx)
                res.append(idx + 1)
            
            swap(i)
            res.append(i + 1)

        return res
