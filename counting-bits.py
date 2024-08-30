class Solution:
    def countBits(self, n: int) -> List[int]:
        binaryRep = [0] * (n + 1)
        
        for i in range(n + 1):
            count, num = 0, i
            
            while num > 0:
                if num & 1:
                    count += 1
                
                num  >>= 1
                
            binaryRep[i] = count  
        
        return binaryRep
