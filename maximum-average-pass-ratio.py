class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t
        
        heap = []

        for p, t in classes:
            heap.append((-gain(p, t), p, t))

        heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heappop(heap)

            p += 1
            t += 1

            heappush(heap, (-gain(p, t), p, t))

        return sum([p / t for _, p, t in heap]) / len(heap)
