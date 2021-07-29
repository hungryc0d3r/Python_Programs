# https://www.codechef.com/problems/CHOPRT

'''
Logic:
>  10 20
<  20 10
=  10 10
'''

T = int(input())
Out = []
for i in range(T):
    A,B = map(int, input().split())
    if A>B:
        O = '>'
    elif A<B:
        O = '<'
    else:
        O = '='
    Out.append(O)

for j in Out:
    print(j)