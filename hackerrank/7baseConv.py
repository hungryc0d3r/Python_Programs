"""
Given an integer, , print the following values for each integer i from 1 to n:
Decimal
Octal
Hexadecimal (capitalized)
Binary

The four values must be printed on a single line in the order specified above for each i from 1 to n. 
Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.
"""

'''
Output sample:
  1     1     1     1
  2     2     2    10
  3     3     3    11
  4     4     4   100
  5     5     5   101
  6     6     6   110
  7     7     7   111
  8    10     8  1000
  9    11     9  1001
 10    12     A  1010
 11    13     B  1011
 12    14     C  1100
 13    15     D  1101
 14    16     E  1110
 15    17     F  1111
 16    20    10 10000
 17    21    11 10001
'''

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
