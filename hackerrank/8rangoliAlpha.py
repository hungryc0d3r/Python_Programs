"""
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""

import string

def print_rangoli(size):
    # your code goes here
    al = string.ascii_lowercase
    res = []
    for i in range(size):
        s = "-".join(al[i:size])
        res.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(res[:0:-1]+res))
        
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
