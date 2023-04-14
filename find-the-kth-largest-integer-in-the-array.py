class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        a = []
        for i in nums:
            a.append(int(i))
        a = sorted(a, reverse = True)
        return str(a[k - 1])
