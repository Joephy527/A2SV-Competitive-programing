class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def helper(value):
            smallestFraction = 0
            num = arr[0]
            den = arr[-1]

            slow = 0
            
            for fast in range(1, len(arr)):
                while slow < fast and arr[slow] / arr[fast] < value:
                    if arr[slow] / arr[fast] > num / den:
                        num, den = arr[slow], arr[fast]

                    slow += 1

                smallestFraction += slow

            return smallestFraction, num, den

        l = arr[0] / arr[-1]
        r = 1

        while l < r:
            m = (l+r) / 2
            count, num, den = helper(m)

            if count == k:
                return [num, den]

            if count > k:
                r = m
            else:
                l = m
