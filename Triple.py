def find_value_appearing_three_times(arr):
    freq_map = {}
    
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
            if freq_map[num] >= 3:
                return num
        else:
            freq_map[num] = 1
    
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_value_appearing_three_times(arr)
    print(result)
