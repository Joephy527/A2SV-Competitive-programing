class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 1 : 
            if nums[0] >= k : 
                return 1 

            return -1 

        queue = deque()
        prefix = [0]

        for num in nums :
            prefix.append(prefix[-1] + num)

        minSize = n + 1

        for idx, val in enumerate(prefix) : 
            while queue and val <= prefix[queue[-1]] : 
                queue.pop()

            while queue and val - prefix[queue[0]] >= k : 
                minSize = min(minSize, idx - queue.popleft())

            queue.append(idx)

        if minSize != n + 1 : 
            return minSize

        return -1 
