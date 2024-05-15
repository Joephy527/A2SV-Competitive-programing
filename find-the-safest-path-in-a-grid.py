class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[float('inf')] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        maxHeap = [(-dist[0][0], 0, 0)]
        maxSafeness = [[-1] * n for _ in range(n)]
        maxSafeness[0][0] = dist[0][0]

        while maxHeap:
            d, r, c = heappop(maxHeap)
            d = -d

            if r == n - 1 and c == n - 1:
                return d

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n:
                    new_safe = min(d, dist[nr][nc])
                    
                    if new_safe > maxSafeness[nr][nc]:
                        maxSafeness[nr][nc] = new_safe
                        heappush(maxHeap, (-new_safe, nr, nc))
