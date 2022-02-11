def swap_case(s):
    newline = ''
    for letter in s:
        if letter.islower():
            newline += letter.upper()
        elif letter.isupper:
            newline += letter.lower()
        else:
            newline += letter
        
    return newline

    # return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
