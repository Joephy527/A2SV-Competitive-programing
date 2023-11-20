class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        sus = 0
        def select(index):
            idx = index
            for i in range(index):
                if arr[i] > arr[idx]:
                    idx = i

            return idx

        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        for i in range(len(arr) - 1, -1, -1):
            idx = select(i)
            
            if idx == i:
                sus += 1
                continue

            reverse(arr, 0, idx)
            reverse(arr, 0, i)
            res.append(idx + 1)
            res.append(i + 1)

            print(arr)

        return res if sus != len(arr) else []
