class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-cnt, char) for char, cnt in count.items()]
        string = []

        heapify(heap)
        print(heap)

        while heap:
            cnt, char = heappop(heap)
            cnt += 1
            
            string.append(char)

            if cnt:
                if not heap: return ""
                cnt_2, char_2 = heappop(heap)
                cnt_2 += 1
                
                string.append(char_2)

                heappush(heap, (cnt, char))
                
                if cnt_2:
                    heappush(heap, (cnt_2, char_2))

        return "".join(string)