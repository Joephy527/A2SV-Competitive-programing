class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for n in count:
            freq[count[n]].append(n)

        topK = []
        
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                topK.append(n)
                
                if len(topK) == k:
                    return topK
