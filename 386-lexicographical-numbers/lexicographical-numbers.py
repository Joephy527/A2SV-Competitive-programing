class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        smallest = []

        def dfs(num):
            if num > n:
                return

            smallest.append(num)
            num *= 10

            for i in range(10):
                dfs(num + i)

        for num in range(1, 10):
            dfs(num)

        return smallest