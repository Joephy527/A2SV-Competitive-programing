n = int(input())
minCapacity = capacity = 0

for _ in range(n):
    off, on = map(int, input().split())
    capacity = capacity + on - off
    minCapacity = max(minCapacity, capacity)
    
print(minCapacity)
