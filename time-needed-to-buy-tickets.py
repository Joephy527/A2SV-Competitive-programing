class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        timeTaken = 0

        for i in range(len(tickets)):
            queue.append(i)

        while queue:
            idx = queue.popleft()
            tickets[idx] -= 1
            timeTaken += 1

            if tickets[idx] == 0 and idx == k:
                return timeTaken
            if tickets[idx] > 0:
                queue.append(idx)

        return timeTaken
