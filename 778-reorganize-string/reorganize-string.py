class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = [(-count, char) for char, count in counts.items()]
        rearrangement = []

        heapify(max_heap)

        while max_heap:
            cnt, char = heappop(max_heap)
            
            if not cnt:
                continue
            
            rearrangement.append(char)

            if cnt < -1:
                if not max_heap:
                    return ""

                cnt_2, char_2 = heappop(max_heap)
                
                if not cnt_2:
                    return ""
                
                rearrangement.append(char_2)
                heappush(max_heap, (cnt_2 + 1, char_2))
                heappush(max_heap, (cnt + 1, char))

        return "".join(rearrangement)