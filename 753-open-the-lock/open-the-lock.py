class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = "0000"
        queue = deque([start])
        visited = {start}
        level = 0

        if start in deadends:
            return -1

        def get_nodes(lock):
            lock = [l for l in lock]
            nodes = []

            for i in range(4):
                inc = (int(lock[i]) + 1) % 10
                dec = (int(lock[i]) - 1) % 10
                node_inc, node_dec = lock[:], lock[:]
                node_inc[i], node_dec[i] = str(inc), str(dec)

                nodes.append("".join(node_inc))
                nodes.append("".join(node_dec))

            return nodes

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur == target:
                    return level

                for node in get_nodes(cur):
                    if node in visited or node in deadends:
                        continue

                    visited.add(node)
                    queue.append(node)

            level += 1

        return -1