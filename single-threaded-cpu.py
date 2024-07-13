class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, task in enumerate(tasks):
            task.append(idx)

        tasks.sort()

        heap = []
        time = tasks[0][0]
        i = 0
        order = []

        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not heap:
                time = tasks[i][0]
            
            else:
                processTime, idx = heapq.heappop(heap)
                
                time += processTime
                order.append(idx)

        return order
