# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, m = int(input()), int(input()), int(input())

print(pow(a, b))

if m and b >= 0:
    print(pow(a, b, m))
