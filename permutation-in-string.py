class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        j = len(s2)
        dic_s1 = Counter(s1)
        l2 = [i for i in s2]
        s3 = deque(l2[:k])
        l = 0
        r = k

        if k > j:
            return False

        while r <= j:
            dic_s3 = Counter(s3)    

            if dic_s1 == dic_s3:
                return True
            
            s3.popleft()

            if r != j:
                s3.append(l2[r])
                
            l += 1
            r += 1
        
        return False
