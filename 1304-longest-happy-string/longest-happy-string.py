class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        happy = []

        if a != 0:
            heappush(heap, (-a, "a"))
        
        if b != 0:
            heappush(heap, (-b, "b"))
        
        if c != 0:
            heappush(heap, (-c, "c"))

        while heap:
            cnt1, chr1 = heappop(heap)

            if (
                len(happy) > 1 and
                happy[-1] == happy[-2] == chr1
            ):
                if not heap: break

                cnt2, chr2 = heappop(heap)
                happy.append(chr2)
                cnt2 += 1
                
                if cnt2 < 0:
                    heappush(heap, (cnt2, chr2))

            happy.append(chr1)
            cnt1 += 1

            if cnt1 < 0:
                heappush(heap, (cnt1, chr1))

        return "".join(happy)