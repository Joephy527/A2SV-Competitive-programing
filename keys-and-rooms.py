class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]
        queue = deque([0])
        visited[0] = True

        while queue:
            key = queue.popleft()

            for k in rooms[key]:
                if not visited[k]:
                    visited[k] = True
                    queue.append(k)

        return all(visited)
