# https://www.codechef.com/problems/FLOW002

'''Write a program to find the remainder when an integer A is divided by an integer B.

Input
The first line contains an integer T, the total number of test cases. Then 
T lines follow, each line contains two Integers A and B.

Output
For each test case, find the remainder when A is divided by B, and display it in a new line.'''

T = int(input())
Rem = []

for i in range(T):
    A = int(input())
    B = int(input())
    R = A % B
    Rem.append(R)

for j in Rem:
    print(j)
    
    