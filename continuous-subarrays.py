class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        deDq = deque()
        inDq = deque()
        idx = 0
        total = 0
        
        for i, num in enumerate(nums):
            while deDq and nums[deDq[-1]] < num:
                deDq.pop()
        
            while inDq and nums[inDq[-1]] > num:
                inDq.pop()

            deDq.append(i)
            inDq.append(i)

            while nums[deDq[0]] - nums[inDq[0]] > 2:
                if deDq[0] == idx: deDq.popleft()
        
                if inDq[0] == idx: inDq.popleft()
        
                idx += 1

            total += i - idx + 1

        return total
