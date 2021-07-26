# https://www.codechef.com/problems/FCTRL2

'''You are asked to calculate factorials of some small positive integers.

Input
An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, 
each containing a single integer n, 1<=n<=100.

Output
For each integer n given at input, display a line with the value of n!'''

t = int(input())
F = []

for i in range(t):
    f = int(input())
    fact = 1
    for i in range(1,f+1):
        fact *= i
    F.append(fact)

for j in F:
    print(j)
    