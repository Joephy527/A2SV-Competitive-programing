class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(c), f) for c, f in Counter(s).items()]
        maxString = []

        heapify(heap)

        while heap:
            c, freq = heappop(heap)
            char = chr(-c)
            use = min(freq, repeatLimit)
            
            maxString.append(char * use)

            if freq > use and heap:
                nextC, nextFreq = heappop(heap)
            
                maxString.append(chr(-nextC))
                
                if nextFreq > 1:
                    heappush(heap, (nextC, nextFreq - 1))
                
                heappush(heap, (c, freq - use))

        return "".join(maxString)
