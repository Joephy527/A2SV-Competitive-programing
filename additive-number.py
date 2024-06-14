class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        sub = []
        
        def backTrack(idx):
            if len(sub) > 2 and not sub[-1] == sub[-2] + sub[-3]:
                return

            if idx == len(num) and len(sub) > 2:
                return True
            
            for i in range(idx, len(num)):
                n = num[idx:i + 1]

                if len(n) > 1 and n[0] == "0":
                    continue

                sub.append(int(n))
                
                if backTrack(i + 1):
                    return True
                
                sub.pop()

        return backTrack(0)
