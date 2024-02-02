def swap_case(s):
    swapedString = ""

    for char in s:
        if char.islower():
            swapedString += char.upper()
        else:
            swapedString += char.lower()
    
    return swapedString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
