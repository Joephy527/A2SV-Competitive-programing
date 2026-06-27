class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = [(-count, char) for char, count in counts.items()]
        rearrangement = []
        prev_count, prev_char = 0, ""

        heapify(max_heap)

        while max_heap:
            cnt, char = heappop(max_heap)
            
            if char == prev_char:
                return ""

            rearrangement.append(char)

            if prev_count < 0:
                heappush(max_heap, (prev_count, prev_char))
            
            if cnt <= -1:
                prev_count, prev_char = cnt + 1, char

        if prev_count <= -1:
            return ""

        return "".join(rearrangement)