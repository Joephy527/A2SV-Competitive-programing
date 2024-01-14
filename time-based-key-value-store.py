class TimeMap:

    def __init__(self):
        self.timeStamps = defaultdict(list)
        self.values = {}

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
        self.timeStamps[key].append(timestamp)
        self.values[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeStamps: return ""

        arr = self.timeStamps[key]
        ts = self.binarySearch(arr, timestamp)

        return self.values[ts] if ts in self.values else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
