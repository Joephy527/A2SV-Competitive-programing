def swap_case(s):
    newS = ""
    for c in s:
        if c.islower():
            newS += c.upper()
        else:
            newS += c.lower()
    
    return newS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
