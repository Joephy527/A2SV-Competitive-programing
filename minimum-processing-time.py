class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        maxProcessTime = 0

        for i in range(len(processorTime)):
            idx = ((i + 1) * 4) - 1
            curMaxProcessTime = tasks[idx] + processorTime[i]
            maxProcessTime = max(maxProcessTime, curMaxProcessTime)

        return maxProcessTime
