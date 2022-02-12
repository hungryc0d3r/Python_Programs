"""
Given an integer, , print the following values for each integer i from 1 to n:
Decimal
Octal
Hexadecimal (capitalized)
Binary
"""

def print_formatted(number):
    # your code goes here
    w = len(str(bin(number)).replace('0b',''))

    for i in range(1, number+1):
        b = bin(int(i)).replace('0b','').rjust(w, ' ')           # converting into binary
        o = oct(int(i)).replace('0o','', 1).rjust(w, ' ')        # converting into octal
        h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')   # converting into hexa
        j = str(i).rjust(w, ' ')
        print(j, o, h, b)
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
