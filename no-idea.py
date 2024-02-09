# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
arr = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

happy = 0

for num in arr:
    if num in setA:
        happy += 1
    if num in setB:
        happy -= 1
        
print(happy)
