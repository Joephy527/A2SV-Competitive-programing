class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        haveGreatestCandies = []
        maxCandy = max(candies)

        for candy in candies:
            if candy + extraCandies >= maxCandy:
                haveGreatestCandies.append(True)
            else:
                haveGreatestCandies.append(False)

        return haveGreatestCandies
