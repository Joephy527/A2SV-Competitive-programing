class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        children = set(leftChild).union(set(rightChild))
        root = None

        for i in range(n):
            if i not in children:
                root = i

        if root == None: return
        
        for i in range(n):
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])

            if rightChild[i] != -1:
                graph[i].append(rightChild[i])

        
        visited = {root}
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.pop()

                for child in graph[node]:
                    if child in visited: return

                    queue.append(child)
                    visited.add(child)

        for i in range(n):
            if i not in visited: return

        return True
