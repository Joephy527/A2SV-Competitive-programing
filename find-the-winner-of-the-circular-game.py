class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = deque([friend + 1 for friend in range(n)])

        while len(friends) > 1:

            for _ in range(k):
                temp = friends.popleft()
                friends.append(temp)

            friends.pop()

        return friends[0]
