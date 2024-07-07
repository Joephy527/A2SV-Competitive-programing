class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes: return k

        k -= numOnes

        if k <= numZeros: return numOnes

        k -= numZeros

        return numOnes - k
