class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        win = maxWin = satisfied = p = 0

        for s in range(len(customers)):
            if grumpy[s]:
                win += customers[s]
            else:
                satisfied += customers[s]

            if s - p + 1 > minutes:
                if grumpy[p]:
                    win -= customers[p]

                p += 1

            maxWin = max(maxWin, win)

        return satisfied + maxWin
