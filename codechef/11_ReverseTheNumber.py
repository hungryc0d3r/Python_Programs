# https://www.codechef.com/problems/FLOW007

'''Given an Integer N, write a program to reverse it.

Input
The first line contains an integer T, total number of testcases. 
Then follow T lines, each line contains an integer N.

Output
For each test case, display the reverse of the given number N, in a new line.'''

T = int(input())
RTN = []

for i in range(T):
    N = int(input())
    revNum = 0
    while N!=0:
        revNum = (revNum * 10) + N%10
        N=N//10
    RTN.append(revNum)

for j in RTN:
    print(j)
    