class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        count = 0
        for i in nums:
            diff = k - i
            if diff in hashMap and hashMap[diff] > 0:
                count += 1
                hashMap[diff] -= 1
            else:
                hashMap[i] += 1

        return count
        
