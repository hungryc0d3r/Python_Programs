# https://www.codechef.com/problems/FLOW017

'''Three numbers A, B and C are the inputs. Write a program to find second largest among them.

Input
The first line contains an integer T, the total number of testcases. Then T lines follow, 
each line contains three integers A, B and C.

Output
For each test case, display the second largest among A, B and C, in a new line.'''

T = int(input())
I = []

for i in range(T):
    A,B,C = map(int, input().split())

    l = [A,B,C]   # storing into list
    l.sort()
    SL = l[-2]
    I.append(SL)

for j in I:
    print(j)
    