class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = [0 for _ in range(len(code))]
        
        if k == 0:
            return result
        
        left, right, s = 1, k, 0
        
        if k < 0:
            left = len(code) - abs(k)
            right = len(code) - 1
        
        for i in range(left, right + 1):
            s += code[i]
        
        for i in range(len(code)):
            result[i] = s
            
            s -= code[left % len(code)]
            s += code[(right + 1) % len(code)]
            
            left += 1
            right += 1
        
        return result
