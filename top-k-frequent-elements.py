class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        b = a.most_common(k)
        c = [i[0] for i in b]
        return c
