
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_string = [""] 
        count = [0]

        def back_track(cur):
            if count[0] == k: 
                return

            if len(cur) == n:
                happy_string[0] = cur
                count[0] += 1 
                
                return

            for c in ['a', 'b', 'c']:
                if len(cur) > 0 and cur[-1] == c:
                    continue
                back_track(cur + c)

        back_track("")
        return happy_string[0] if count[0] == k else ""
