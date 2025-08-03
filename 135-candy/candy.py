class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = candy = inc = 1
        dec = 0

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                candy = 1 if ratings[i] == ratings[i - 1] else candy + 1
                candies += candy
                inc = candy
            else:
                dec += 1
                dec += dec == inc
                candies += dec
                candy = 1

        return candies