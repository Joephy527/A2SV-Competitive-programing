class TimeMap:

    def __init__(self):
        self.map1 = defaultdict(list)
        self.map2 = {}

    def binarySearch(self, arr: List[int], target: int) -> int:
        if target < arr[0]: return -1
        
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m] < target:
                l = m + 1
            elif arr[m] > target:
                r = m - 1
            else: return arr[m]

        return arr[l] if l < len(arr) and arr[l] < target else arr[r]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map1[key].append(timestamp)
        self.map2[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map1: return ""

        arr = self.map1[key]
        ts = self.binarySearch(arr, timestamp)

        return self.map2[ts] if ts in self.map2 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
