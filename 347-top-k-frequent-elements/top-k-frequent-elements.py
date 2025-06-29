class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        k_freq = []

        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                k_freq.append(num)
                k -= 1

            if not k:
                break
        
        return k_freq