s1count = Counter(s1)
        s2count = Counter(s2[:len(s1)])
        l = 0
        r = len(s1)
        
        while r < len(s2):
            if s1count == s2count: return True

            s2count[s2[l]] -= 1 
            s2count[s2[r]] = 1 + s2count.get(s2[r], 0)
            l += 1
            r += 1

        return s1count == s2count
