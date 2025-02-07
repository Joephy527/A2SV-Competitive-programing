class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_count = {}
        color_count = defaultdict(int)
        distinct = [0] * len(queries)

        for idx, (ball, color) in enumerate(queries):
            if ball in ball_count:
                prev_color = ball_count[ball]
                color_count[prev_color] -= 1

                if not color_count[prev_color]:
                    del color_count[prev_color]
            
            ball_count[ball] = color
            color_count[color] += 1

            distinct[idx] = len(color_count)

        return distinct
