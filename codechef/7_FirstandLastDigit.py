# https://www.codechef.com/problems/FLOW004

'''If Give an integer N . Write a program to obtain 
the sum of the first and last digits of this number.

Input
The first line contains an integer T, the total number of test cases.
Then follow T lines, each line contains an integer N.

Output
For each test case, display the sum of first and 
last digits of N in a new line.'''

T = int(input())
SFL = []

for i in range(T):
    N = int(input())
    sfl = []
    while N!=0:
        num = N%10
        sfl.append(num)
        N = N//10
    sumfl = sfl[0] + sfl[len(sfl)-1]
    SFL.append(sumfl)

for j in SFL:
    print(j)
    
    