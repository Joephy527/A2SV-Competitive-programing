def operate(N):
    res = []
    for _ in range(N):
        com = list(map(str, input().split()))
        if com[0] == 'insert':
            res.insert(int(com[1]), int(com[2]))
            
        elif com[0] == 'print':
            print(res)
            
        elif com[0] == 'remove':
            res.remove(int(com[1]))
            
        elif com[0] == 'append':
            res.append(int(com[1]))
            
        elif com[0] == 'sort':
            res.sort()

        elif com[0] == 'pop':
            res.pop()

        elif com[0] == 'reverse':
            res.reverse()

if __name__ == '__main__':
    N = int(input())
    operate(N)
