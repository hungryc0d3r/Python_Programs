# https://www.codechef.com/problems/FLOW006

'''You're given an integer N. Write a program to calculate the sum of all the digits of N.

Input
The first line contains an integer T, the total number of testcases. Then follow T lines,
each line contains an integer N.

Output
For each test case, calculate the sum of digits of N, and display it in a new line.'''

T = int(input())
SD = []

for i in range(T):
    N = int(input())
    SumD = 0
    while N != 0:
        SumD = SumD + N%10
        N = N//10
    SD.append(SumD)
    
for j in SD:
    print(j)
    
    