class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-count[c], c) for c in count]
        rearangedStr = []
        
        heapify(heap)

        def helper(character, frequency):
            rearangedStr.append(character)

            if frequency < -1:
                heappush(heap, (frequency + 1, character))
        
        while heap:
            freq, char = heappop(heap)
            
            if rearangedStr and char == rearangedStr[-1]:
                if not heap:
                    return ""
                
                f, c = heappop(heap)

                helper(c, f)

            helper(char, freq)

        return "".join(rearangedStr)
