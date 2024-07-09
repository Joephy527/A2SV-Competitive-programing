class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef = customers[0][0]
        waitingTime = 0

        for arrive, time in customers:
            chef = chef if chef >= arrive else arrive
            chef += time
            waitingTime += chef - arrive

        return waitingTime / len(customers)
