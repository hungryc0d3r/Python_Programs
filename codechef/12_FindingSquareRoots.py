# https://www.codechef.com/problems/FSQRT

'''finding the square root of any given integer using in-built functions. So here's your chance.

Input
The first line of the input contains an integer T, the number of test cases. T lines follow. 
Each line contains an integer N whose square root needs to be computed.

Output
For each line of the input, output the square root of the input integer, rounded down to the 
nearest integer, in a new line.'''

import math

T = int(input())
SQ = []

for i in range(T):
    N = int(input())
    sq = int(math.sqrt(N))
    SQ.append(sq)

for j in SQ:
    print(j)