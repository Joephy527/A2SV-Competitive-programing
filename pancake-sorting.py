class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def swap(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        def select(arr, index):
            idx = index
            for i in range(index):
                if arr[i] > arr[idx]:
                    idx = i

            return idx

        res = []

        for i in range(len(arr) - 1, -1, -1):
            idx = select(arr, i)

            if idx == i: continue

            if idx != 0:
                swap(arr, 0, idx)
                res.append(idx + 1)
            swap(arr, 0, i)
            res.append(i + 1)

        return res
