# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}

for _ in range(n):
    name, phoneNumber = input().split()
    phoneBook[name] = int(phoneNumber)

for _ in range(n):
    try:
        lookupName = input()

        if lookupName in phoneBook:
            print(f"{lookupName}={phoneBook[lookupName]}")
        else:
            print("Not found")
    except EOFError:
        break
