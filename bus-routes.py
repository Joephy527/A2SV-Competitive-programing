class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        
        for bus , busStops in enumerate(routes):
            for busRoute in busStops:
                graph[busRoute].append(bus)
        
        queue = deque(graph[source])
        visited = set(graph[source])
        count = 0
        
        if source == target:
            return 0
        
        while queue:
            count+=1
            
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                if target in routes[cur]:
                    return count
                
                for route in routes[cur]:
                    for nextBus in graph[route]:
                        if nextBus not in visited:
                            visited.add(nextBus)
                            queue.append(nextBus)
        
        return -1
