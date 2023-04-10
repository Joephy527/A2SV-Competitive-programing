n, m = map(int, input().split())
 
if (n * m) % 2 == 0:
    print ((n * m) // 2)
else:
    print ((((n * m) - 1) // 2))
