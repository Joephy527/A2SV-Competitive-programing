class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        c = Counter(changed)
        a = []
        for i in changed:
            if i in c and c[i] >= 1:
                c[i] -= 1
                if (i * 2) in c and c[(i * 2)] >= 1:
                    a.append(i)
                    c[i * 2] -= 1
            if len(a) == len(changed) // 2:
                return a
        return []
