# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1

        while l + 1 < r:
            m = (l + r) // 2

            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = m
            else:
                r = m

        p = r

        l, r = 0, p

        while l <= r:
            m = (l + r) // 2
            mid = mountain_arr.get(m)

            if mid == target:
                return m
            elif mid > target:
                r = m - 1
            else:
                l = m + 1

        l, r = p + 1, mountain_arr.length() - 1

        while l <= r:
            m = (l + r) // 2
            mid = mountain_arr.get(m)

            if mid == target:
                return m
            elif mid > target:
                l = m + 1
            else:
                r = m - 1

        return -1
