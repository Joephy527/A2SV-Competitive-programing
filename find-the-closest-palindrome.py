class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def convertToPalindrom(num):
            digits = [char for char in str(num)]
            l, r = 0, len(digits) - 1

            while l < r:
                digits[r] = digits[l]
                l += 1
                r -= 1

            return int("".join(digits))
        
        def findPrevAndNext(num):
            left, right = 0, num
            previous = float("-inf")

            while left <= right:
                mid = (left + right) // 2
                pal = convertToPalindrom(mid)

                if pal < num:
                    previous = pal
                    left = mid + 1
                else:
                    right = mid - 1

            left, right = num, int(1e18)
            nxt = float("-inf")

            while left <= right:
                mid = (left + right) // 2
                pal = convertToPalindrom(mid)

                if pal > num:
                    nxt = pal
                    right = mid - 1
                else:
                    left = mid + 1

            return (previous, nxt)

        num = int(n)
        prev, nxt = findPrevAndNext(num)

        if abs(prev - num) <= abs(nxt - num):
            return str(prev)
        
        return str(nxt)
