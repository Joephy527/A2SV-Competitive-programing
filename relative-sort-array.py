class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        rest, ans = [], []

        for num in arr2:
            count[num] = 0

        for num in arr1:
            if num in count:
                count[num] += 1
            else:
                rest.append(num)

        for val, amt in count.items():
            while amt:
                ans.append(val)
                amt -= 1

        rest.sort()
        for num in rest:
            ans.append(num)

        return ans
