# https://www.codechef.com/problems/DECINC

'''
Logic:
N%4 == 0 -> N+1
N%4 !=0  -> N-1
'''

N = int(input())
if N%4 == 0:
    print(N+1)
else:
    print(N-1)
