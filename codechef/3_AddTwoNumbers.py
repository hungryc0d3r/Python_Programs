# https://www.codechef.com/problems/FLOW001

'''Shivam is the youngest programmer in the world, he is just 12 years old. 
Shivam is learning programming and today he is writing his first program.

The task is very simple: given two integers A and B, write a program to add 
these two numbers and output it.

Input
The first line contains an integer T, the total number of test cases. Then 
follow T lines, each line contains two Integers A and B.

Output
For each test case, add A and B and display the sum in a new line.
'''

T = int(input('No of input cases: '))

S = []
for i in range(T):
    A = int(input('A: '))
    B = int(input('B: '))
    
    su = A + B
    S.append(su)

for j in S:
    print(j)
    
