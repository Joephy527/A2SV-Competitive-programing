class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        maxQueue = deque()
        maxVals = []

        while r < len(nums):

            while maxQueue and nums[maxQueue[-1]] < nums[r]:
                maxQueue.pop()

            maxQueue.append(r)

            if maxQueue[0] < l:
                maxQueue.popleft()

            if r + 1 >= k:
                maxVals.append(nums[maxQueue[0]])
                l += 1

            r += 1

        return maxVals
