# https://www.codechef.com/problems/REMISS

'''
Logic:
G1 G2 -> counts the entry of person
when G1 sleeps G2 is awake vice-versa
chef count -> G1 gives A G2 gives B integer times
so, find min and max
if A > B:
    A , A+B
if A < B:
    B, A+B
A is greater then G1 woken up long time than G2 vice versa
'''

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    if A > B:
        print(A, (A+B))
    elif A < B:
        print(B, (A+B))
        