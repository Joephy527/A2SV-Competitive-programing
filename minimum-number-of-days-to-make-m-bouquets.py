class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 0, max(bloomDay)
        bouquets = -1

        def numberOfBouquets(mid):
            bouquets = count = 0

            for day in bloomDay:
                if day <= mid:
                    count += 1
                else:
                    count = 0

                if count == k:
                    bouquets += 1
                    count = 0
            
            return bouquets

        while l <= r:
            mid = (l + r) // 2

            if numberOfBouquets(mid) >= m:
                bouquets = mid
                r = mid - 1
            else:
                l = mid + 1

        return bouquets
