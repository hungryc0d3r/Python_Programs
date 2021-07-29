# https://www.codechef.com/problems/FLOW013

'''
Logic:
A, B, C -> Angles of triangle
A+B+C = 180 -> Print YES
A+B+C != 180 -> Print NO'''

T = int(input())
O = []

for i in range(T):
    A,B,C = map(int, input().split())
    if A+B+C == 180:
        Out = 'YES'
    else:
        Out = 'NO'
    O.append(Out)

for j in O:
    print(j)    
        