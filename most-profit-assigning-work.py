class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profitMap = defaultdict(int)
        pd = pw = totalProfit = maxProfit = 0

        for p, d in zip(profit, difficulty):
            profitMap[d] = max(profitMap[d], p)
        
        difficulty.sort()
        worker.sort()

        while pd < len(difficulty) and pw < len(worker):
            if difficulty[pd] <= worker[pw]:
                maxProfit = max(maxProfit, profitMap[difficulty[pd]])
                pd += 1
            else:
                totalProfit += maxProfit
                pw += 1

        totalProfit += maxProfit * (len(worker) - pw)

        return totalProfit
